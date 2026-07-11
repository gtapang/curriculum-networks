"""Course-prerequisite-network metrics.

Implements the Curricular Analytics vertex metrics of Heileman et al. (2018,
arXiv:1811.09676) on the prerequisite DAG:

    blocking factor  b(v)  = number of courses unreachable until v is passed
                             (descendants of v)
    delay factor     d(v)  = number of vertices on the longest source-to-sink
                             prerequisite path passing through v
    cruciality       c(v)  = b(v) + d(v)
    structural complexity  = sum of c(v) over all courses

plus whole-graph descriptors used in comparative CPN studies
(Stavrinides & Zuev 2023; Yang et al. 2024/2025): density, depth (longest
chain), width (largest antichain level), Louvain modularity, and the length
of the longest chain through quantitatively-tagged courses.
"""

from __future__ import annotations

from typing import Iterable, Optional

import networkx as nx
import pandas as pd

from curricnet.ingest import structural_graph
from curricnet.schema import Curriculum


def blocking_factor(graph: nx.DiGraph, node) -> int:
    return len(nx.descendants(graph, node))


def _longest_path_lengths(graph: nx.DiGraph) -> tuple[dict, dict]:
    """Vertex counts of the longest path ending at v (into) and starting at v (outof)."""
    order = list(nx.topological_sort(graph))
    into = {v: 1 for v in order}
    for v in order:
        for u in graph.predecessors(v):
            into[v] = max(into[v], into[u] + 1)
    outof = {v: 1 for v in order}
    for v in reversed(order):
        for w in graph.successors(v):
            outof[v] = max(outof[v], outof[w] + 1)
    return into, outof


def delay_factor(graph: nx.DiGraph, node) -> int:
    into, outof = _longest_path_lengths(graph)
    return into[node] + outof[node] - 1


def cruciality(graph: nx.DiGraph, node) -> int:
    return blocking_factor(graph, node) + delay_factor(graph, node)


def course_metrics(curriculum: Curriculum) -> pd.DataFrame:
    """Per-course metric table for the prerequisite network."""
    graph = structural_graph(curriculum)
    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("prerequisite network must be acyclic; run validation first")
    into, outof = _longest_path_lengths(graph)
    betweenness = nx.betweenness_centrality(graph)
    rows = []
    for node in graph.nodes:
        blocking = len(nx.descendants(graph, node))
        delay = into[node] + outof[node] - 1
        rows.append(
            {
                "Id": node,
                "Label": graph.nodes[node].get("Label", node),
                "in_degree": graph.in_degree(node),
                "out_degree": graph.out_degree(node),
                "betweenness": betweenness[node],
                "blocking_factor": blocking,
                "delay_factor": delay,
                "cruciality": blocking + delay,
            }
        )
    return pd.DataFrame(rows).sort_values("cruciality", ascending=False).reset_index(drop=True)


def quantitative_chain_length(
    curriculum: Curriculum, quantitative_ids: Iterable[str]
) -> int:
    """Number of courses on the longest prerequisite chain that includes at
    least one quantitatively-tagged course (generalizes the BSHRIM
    PRECALC->CALC->ORM->CONTROL gate chain)."""
    graph = structural_graph(curriculum)
    tagged = [q for q in quantitative_ids if q in graph]
    if not tagged:
        return 0
    into, outof = _longest_path_lengths(graph)
    return max(into[q] + outof[q] - 1 for q in tagged)


def curriculum_summary(
    curriculum: Curriculum, quantitative_ids: Optional[Iterable[str]] = None
) -> dict:
    """One row of the cross-curriculum master table."""
    graph = structural_graph(curriculum)
    per_course = course_metrics(curriculum)
    into, _ = _longest_path_lengths(graph)
    depth = max(into.values()) if into else 0
    # width = the largest number of courses at the same longest-path level
    levels = pd.Series(into)
    width = int(levels.value_counts().max()) if len(levels) else 0

    undirected = nx.Graph()
    undirected.add_nodes_from(graph.nodes)
    undirected.add_edges_from(graph.edges)
    for _, row in curriculum.corequisite_edges.iterrows():
        if row["Source"] in undirected and row["Target"] in undirected:
            undirected.add_edge(row["Source"], row["Target"])
    if undirected.number_of_edges():
        communities = nx.community.louvain_communities(undirected, seed=42)
        modularity = nx.community.modularity(undirected, communities)
    else:
        communities, modularity = [], float("nan")

    quantitative = list(quantitative_ids or curriculum.meta.get("quantitative_courses") or [])
    summary = {
        "slug": curriculum.slug,
        "program": curriculum.meta.get("program"),
        "institution": curriculum.meta.get("institution"),
        "country": curriculum.meta.get("country"),
        "catalog_year": curriculum.meta.get("catalog_year"),
        "courses": graph.number_of_nodes(),
        "prerequisite_edges": graph.number_of_edges(),
        "corequisite_edges": len(curriculum.corequisite_edges),
        "credit_units": curriculum.credit_units(),
        "density": nx.density(graph),
        "depth": depth,
        "width": width,
        "structural_complexity": int(per_course["cruciality"].sum()),
        "max_blocking_factor": int(per_course["blocking_factor"].max()),
        "max_delay_factor": int(per_course["delay_factor"].max()),
        "top_blocking_course": per_course.sort_values("blocking_factor", ascending=False)["Label"].iloc[0],
        "modularity": modularity,
        "communities": len(communities),
        "quantitative_chain_length": quantitative_chain_length(curriculum, quantitative),
    }
    return summary
