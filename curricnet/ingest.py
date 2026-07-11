"""Loading and converting curricula.

Entry points:

    load_curriculum(path)        read a curriculum directory (yaml + 2 CSVs)
    curriculum_from_frames(...)  build from in-memory DataFrames
    from_checklist_table(df)     convert an encoder's flat spreadsheet
                                 (course, prereqs, coreqs, units, ...) into
                                 the canonical node/edge tables
    structural_graph(curr)       networkx DiGraph of the prerequisite network
    write_gexf / read_gexf       Gephi round-trip
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

import networkx as nx
import pandas as pd
import yaml

from curricnet.schema import (
    COREQUISITE,
    EDGE_REQUIRED_COLUMNS,
    PREREQUISITE,
    Curriculum,
)

PathLike = Union[str, Path]


def load_curriculum(path: PathLike, validate: bool = True) -> Curriculum:
    """Read a curriculum directory containing curriculum.yaml, nodes.csv, edges.csv."""
    path = Path(path)
    with open(path / "curriculum.yaml") as fh:
        meta = yaml.safe_load(fh) or {}
    meta.setdefault("slug", path.name)
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
    """Convert an encoder-friendly flat table into a Curriculum.

    Expected columns (case-insensitive): Id, Label, Category, Units,
    Prerequisites, Corequisites, and optionally Semester, Year.
    Prerequisites/Corequisites are semicolon- or comma-separated lists of Ids.
    This is the format used to transcribe catalogs and CHED PSG tables.
    """
    table = table.rename(columns={c: c.strip().title() for c in table.columns})
    node_cols = ["Id", "Label", "Category", "Units"] + [
        c for c in ("Semester", "Year") if c in table.columns
    ]
    nodes = table[node_cols].copy()
    nodes["Id"] = nodes["Id"].astype(str).str.strip()

    def _split(cell) -> list[str]:
        if pd.isna(cell) or not str(cell).strip():
            return []
        text = str(cell).replace(",", ";")
        return [part.strip() for part in text.split(";") if part.strip()]

    rows = []
    for _, row in table.iterrows():
        target = str(row["Id"]).strip()
        for source in _split(row.get("Prerequisites")):
            rows.append((source, target, PREREQUISITE, "Prerequisite", 2))
        for source in _split(row.get("Corequisites")):
            rows.append((source, target, COREQUISITE, "Corequisite", 1))
    edges = pd.DataFrame(rows, columns=EDGE_REQUIRED_COLUMNS)
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
