"""Data schema and validation for encoded curricula.

A curriculum on disk is a directory containing:

    curriculum.yaml   metadata (program, institution, country, catalog_year,
                      total_units, source, notes, tags)
    nodes.csv         Id,Label,Category,Units[,Semester,Year]
    edges.csv         Source,Target,Type,Label,Weight

This is the same format as the BSHRIM APacCHRIE 2026 tables
(data/nodes_table_anon.csv, data/edges_table_anon.csv), with node Ids made
unique (repeated slots numbered, e.g. PHYSED1..PHYSED4) and optional
Semester/Year placement columns used by term-based metrics.

Edge Type is "Directed" for prerequisites and "Undirected" for corequisites
(mirroring the Gephi convention already used in the BSHRIM tables).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import pandas as pd

NODE_REQUIRED_COLUMNS = ["Id", "Label", "Category", "Units"]
NODE_OPTIONAL_COLUMNS = ["Semester", "Year"]
EDGE_REQUIRED_COLUMNS = ["Source", "Target", "Type", "Label", "Weight"]

PREREQUISITE = "Directed"
COREQUISITE = "Undirected"

META_REQUIRED_KEYS = ["program", "institution", "country", "catalog_year"]


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def raise_if_errors(self) -> None:
        if self.errors:
            raise ValueError("curriculum validation failed:\n- " + "\n- ".join(self.errors))


@dataclass
class Curriculum:
    """An encoded curriculum: metadata plus node and edge tables."""

    meta: dict
    nodes: pd.DataFrame
    edges: pd.DataFrame

    @property
    def slug(self) -> str:
        return self.meta.get("slug") or "{}-{}".format(
            self.meta.get("institution", "unknown"), self.meta.get("program", "unknown")
        ).lower().replace(" ", "-")

    @property
    def prerequisite_edges(self) -> pd.DataFrame:
        return self.edges[self.edges["Type"] == PREREQUISITE]

    @property
    def corequisite_edges(self) -> pd.DataFrame:
        return self.edges[self.edges["Type"] == COREQUISITE]

    def credit_units(self) -> float:
        """Sum of positive Units (negative units mark non-credit courses
        such as PE/NSTP in the UP convention)."""
        units = pd.to_numeric(self.nodes["Units"], errors="coerce").fillna(0)
        return float(units[units > 0].sum())

    def validate(self, declared_total: Optional[float] = None) -> ValidationReport:
        return validate_curriculum(self, declared_total=declared_total)


def validate_curriculum(
    curriculum: Curriculum, declared_total: Optional[float] = None
) -> ValidationReport:
    """Check structural integrity of a curriculum.

    Errors: missing columns, duplicate node Ids, edge endpoints missing from
    the node table, prerequisite cycles.
    Warnings: unit-total mismatch against the declared total, missing metadata.
    """
    import networkx as nx

    report = ValidationReport()
    nodes, edges = curriculum.nodes, curriculum.edges

    for col in NODE_REQUIRED_COLUMNS:
        if col not in nodes.columns:
            report.errors.append(f"nodes: missing required column {col!r}")
    for col in EDGE_REQUIRED_COLUMNS:
        if col not in edges.columns:
            report.errors.append(f"edges: missing required column {col!r}")
    if report.errors:
        return report

    dupes = nodes["Id"][nodes["Id"].duplicated()].unique().tolist()
    if dupes:
        report.errors.append(
            f"nodes: duplicate Ids {dupes} (number repeated slots, e.g. PHYSED1..PHYSED4)"
        )

    known = set(nodes["Id"])
    for col in ("Source", "Target"):
        missing = sorted(set(edges[col]) - known)
        if missing:
            report.errors.append(f"edges: {col} endpoints not in node table: {missing}")

    bad_types = sorted(set(edges["Type"]) - {PREREQUISITE, COREQUISITE})
    if bad_types:
        report.errors.append(
            f"edges: unknown Type values {bad_types} (expected {PREREQUISITE!r}/{COREQUISITE!r})"
        )

    if not report.errors:
        graph = nx.DiGraph()
        graph.add_nodes_from(nodes["Id"])
        prereq = edges[edges["Type"] == PREREQUISITE]
        graph.add_edges_from(zip(prereq["Source"], prereq["Target"]))
        if not nx.is_directed_acyclic_graph(graph):
            cycle = nx.find_cycle(graph)
            report.errors.append(f"prerequisite graph has a cycle: {cycle}")

    for key in META_REQUIRED_KEYS:
        if not curriculum.meta.get(key):
            report.warnings.append(f"meta: missing {key!r}")

    declared = declared_total if declared_total is not None else curriculum.meta.get("total_units")
    if declared is not None:
        total = curriculum.credit_units()
        if abs(total - float(declared)) > 1e-9:
            report.warnings.append(
                f"credit units in node table ({total:g}) != declared total_units ({declared:g})"
            )

    return report
