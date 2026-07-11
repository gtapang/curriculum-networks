"""Empirical progression networks from student records.

Two entry points:

    build_progression_network(records)  aggregate long-format enrollment
        records into a course-transition network with the same node/edge
        attribute schema as the published BSHRIM network
        (data/course_network.gexf)

    empirical_summary(gexf_path)        read an existing progression network
        (e.g. the published GEXF) and extract per-course performance and
        bottleneck indicators

Long-format record columns (one row per enrollment attempt):

    student   anonymized student id (e.g. BSHRIM-001)
    term      sortable term index (0, 1, 2, ...) or "2021-1" style strings
    course    normalized course label
    grade     numeric grade (UP scale: 1.00 best, 3.00 pass, 4.00/5.00 fail)
    status    optional: PASS / FAIL / INC / DRP (derived from grade if absent)
"""

from __future__ import annotations

from collections import defaultdict
from typing import Optional, Union

import networkx as nx
import pandas as pd

FAIL_GRADES = {4.0, 5.0}


def _derive_status(row) -> str:
    status = str(row.get("status") or "").strip().upper()
    if status:
        return status
    grade = row.get("grade")
    if pd.isna(grade):
        return "INC"
    return "FAIL" if float(grade) in FAIL_GRADES else "PASS"


def build_progression_network(records: pd.DataFrame) -> nx.DiGraph:
    """Aggregate enrollment records into a weighted course-transition network.

    Nodes carry: avg_grade, student_count, fail_rate, inc_rate,
    total_attempts, fail_count, inc_count, drp_count (matching the published
    BSHRIM GEXF schema). A directed edge A->B with weight w means students
    moved from course A in one term to course B in the next term w times;
    self-loops are retakes of the same course in a later term.
    """
    df = records.copy()
    df["status"] = df.apply(_derive_status, axis=1)
    df["term_order"] = pd.factorize(df["term"].astype(str), sort=True)[0]

    graph = nx.DiGraph()
    for course, group in df.groupby("course"):
        graded = pd.to_numeric(group["grade"], errors="coerce").dropna()
        attempts = len(group)
        fails = int((group["status"] == "FAIL").sum())
        incs = int((group["status"] == "INC").sum())
        graph.add_node(
            course,
            label=course,
            avg_grade=round(float(graded.mean()), 4) if len(graded) else float("nan"),
            student_count=int(group["student"].nunique()),
            fail_rate=round(fails / attempts, 4) if attempts else 0.0,
            inc_rate=round(incs / attempts, 4) if attempts else 0.0,
            total_attempts=attempts,
            fail_count=fails,
            inc_count=incs,
            drp_count=int((group["status"] == "DRP").sum()),
        )

    transitions: dict[tuple[str, str], int] = defaultdict(int)
    for _, history in df.sort_values("term_order").groupby("student"):
        terms = [term_df["course"].tolist() for _, term_df in history.groupby("term_order")]
        for previous, current in zip(terms, terms[1:]):
            for source in previous:
                for target in current:
                    transitions[(source, target)] += 1

    for (source, target), weight in transitions.items():
        graph.add_edge(source, target, weight=weight, is_self_loop=source == target)
    return graph


def empirical_summary(
    network: Union[str, nx.DiGraph], top: Optional[int] = None
) -> pd.DataFrame:
    """Bottleneck table from a progression network (path to GEXF or graph).

    Returns one row per course with performance attributes plus the retake
    self-loop weight, sorted by fail_rate. This reproduces the BSHRIM
    bottleneck analysis (Math 21/CALC on top) from the published network.
    """
    graph = nx.read_gexf(network) if isinstance(network, str) else network
    rows = []
    for node, data in graph.nodes(data=True):
        self_loop = graph.get_edge_data(node, node) or {}
        rows.append(
            {
                "course": data.get("label", node),
                "total_attempts": data.get("total_attempts"),
                "student_count": data.get("student_count"),
                "avg_grade": data.get("avg_grade"),
                "fail_rate": data.get("fail_rate"),
                "inc_rate": data.get("inc_rate"),
                "fail_count": data.get("fail_count"),
                "retake_self_loop": self_loop.get("weight", 0),
            }
        )
    table = pd.DataFrame(rows).sort_values("fail_rate", ascending=False).reset_index(drop=True)
    return table.head(top) if top else table


def structural_empirical_divergence(
    structural: nx.DiGraph, empirical: nx.DiGraph
) -> dict:
    """Quantify the design-reality gap between the prerequisite network and
    the observed progression network (Paper 2 headline metrics)."""
    struct_edges = set(structural.edges)
    label_of = {n: d.get("label", n) for n, d in empirical.nodes(data=True)}
    emp_edges = {(label_of[u], label_of[v]) for u, v in empirical.edges if u != v}
    realized = struct_edges & emp_edges
    return {
        "structural_edges": len(struct_edges),
        "empirical_edges": len(emp_edges),
        "realized_prerequisite_edges": len(realized),
        "prerequisite_realization_rate": (
            len(realized) / len(struct_edges) if struct_edges else float("nan")
        ),
        "emergent_edge_fraction": (
            (len(emp_edges) - len(realized)) / len(emp_edges) if emp_edges else float("nan")
        ),
    }
