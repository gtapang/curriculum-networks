"""Loading and converting curricula.

Entry points:

    load_curriculum(path)        read a curriculum directory (yaml + courses.csv,
                                 or legacy yaml + nodes.csv + edges.csv)
    curriculum_from_frames(...)  build from in-memory DataFrames
    from_checklist_table(df)     convert an encoder's flat spreadsheet
                                 (course, prereqs, coreqs, units, ...) into
                                 the canonical node/edge tables
    structural_graph(curr)       networkx DiGraph of the prerequisite network
    write_gexf / read_gexf       Gephi round-trip

The standard authoring format is a single `courses.csv` per curriculum
(see curricnet.format and docs/CURRICULUM_FORMAT.md). The older split
`nodes.csv` + `edges.csv` pair is still read for provenance-preserving
imports such as the BSHRIM reference curriculum.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

import networkx as nx
import pandas as pd
import yaml

from curricnet.format import courses_to_frames, read_courses_csv
from curricnet.schema import Curriculum

PathLike = Union[str, Path]


def load_curriculum(path: PathLike, validate: bool = True) -> Curriculum:
    """Read a curriculum directory.

    Prefers the standard `courses.csv` authoring format; falls back to the
    legacy `nodes.csv` + `edges.csv` pair when no courses.csv is present.
    """
    path = Path(path)
    with open(path / "curriculum.yaml") as fh:
        meta = yaml.safe_load(fh) or {}
    meta.setdefault("slug", path.name)
    if (path / "courses.csv").exists():
        nodes, edges = read_courses_csv(path / "courses.csv")
    else:
        nodes = pd.read_csv(path / "nodes.csv", dtype={"Id": str})
        edges = pd.read_csv(path / "edges.csv", dtype={"Source": str, "Target": str})
    curriculum = Curriculum(meta=meta, nodes=nodes, edges=edges)
    if validate:
        curriculum.validate().raise_if_errors()
    return curriculum


def curriculum_from_frames(
    meta: dict, nodes: pd.DataFrame, edges: pd.DataFrame, validate: bool = True
) -> Curriculum:
    curriculum = Curriculum(meta=meta, nodes=nodes.copy(), edges=edges.copy())
    if validate:
        curriculum.validate().raise_if_errors()
    return curriculum


def from_checklist_table(table: pd.DataFrame, meta: Optional[dict] = None) -> Curriculum:
    """Convert an in-memory course table into a Curriculum.

    Columns and the prerequisite grammar are the standard authoring format
    (see curricnet.format): case-insensitive headers Id, Label, Units, and
    optionally Category, Year, Semester, Prerequisites, Corequisites,
    Standing, Notes. Prerequisites use ';' for AND and '|' for OR.
    """
    nodes, edges = courses_to_frames(table)
    return Curriculum(meta=meta or {}, nodes=nodes, edges=edges)


def structural_graph(curriculum: Curriculum, include_coreqs: bool = False) -> nx.DiGraph:
    """Directed prerequisite network with node attributes from the node table.

    Corequisites are excluded by default (they are not precedence
    constraints); pass include_coreqs=True to add them as directed edges with
    their table weight, matching how the BSHRIM Gephi network was built.
    """
    graph = nx.DiGraph()
    for _, row in curriculum.nodes.iterrows():
        graph.add_node(row["Id"], **{k: row[k] for k in curriculum.nodes.columns if k != "Id"})
    edge_table = curriculum.edges if include_coreqs else curriculum.prerequisite_edges
    for _, row in edge_table.iterrows():
        graph.add_edge(row["Source"], row["Target"], weight=row["Weight"], kind=row["Type"])
    return graph


def write_gexf(graph: nx.Graph, path: PathLike) -> None:
    """Write a Gephi-compatible GEXF, dropping NaN attribute values."""
    clean = graph.copy()
    for _, data in clean.nodes(data=True):
        for key in [k for k, v in data.items() if pd.isna(v)]:
            del data[key]
    nx.write_gexf(clean, str(path))


def read_gexf(path: PathLike) -> nx.Graph:
    return nx.read_gexf(str(path))
