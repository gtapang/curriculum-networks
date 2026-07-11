"""The standard curriculum authoring format (courses.csv).

A curriculum is authored as ONE spreadsheet-friendly table, `courses.csv`,
with one row per course, alongside a `curriculum.yaml` metadata file. This is
the format to use for all new curricula going forward; see
docs/CURRICULUM_FORMAT.md for the full specification.

`courses.csv` columns (header names are case-insensitive; aliases accepted):

    id            required  unique short course code (network node id)
    title         required  human-readable course name
    units         required  credit units; negative marks non-credit (PE, NSTP)
    category      optional  GE / Core / Elective / PE / NSTP / Non-Credit / ...
    year          optional  year level (1..N)
    sem           optional  1, 2, or M (midyear)
    prerequisites optional  requirement expression (see grammar below)
    corequisites  optional  ';'-separated ids taken concurrently
    standing      optional  class-standing / milestone gate (NOT a course edge)
    notes         optional  free text

Prerequisite grammar (conjunctive normal form):

    ';'  separates AND clauses     -> "MATH21; STAT101" needs both
    '|'  separates OR alternatives -> "BA101 | IE31"     needs either
    the word "or" is accepted as a synonym for '|'
    parentheses are allowed for readability: "MATH21; (BA101 | IE31)"

Every id referenced in prerequisites/corequisites must be a row in the same
file (validation enforces this). Class-standing requirements such as
"Junior Standing" go in the `standing` column, not `prerequisites`, because
they are not edges between courses.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Union

import pandas as pd

from curricnet.schema import COREQUISITE, PREREQUISITE

PathLike = Union[str, Path]

#: canonical edge columns produced by this module (superset of the required 5)
EDGE_COLUMNS = ["Source", "Target", "Type", "Label", "Weight", "Requirement", "Group"]

#: authoring header -> canonical column name (compared case-insensitively)
COLUMN_ALIASES = {
    "id": "Id", "course": "Id", "code": "Id", "course code": "Id",
    "title": "Label", "label": "Label", "name": "Label", "course title": "Label",
    "units": "Units", "unit": "Units", "credits": "Units",
    "category": "Category", "class": "Category",
    "year": "Year", "yr": "Year", "year level": "Year",
    "sem": "Semester", "semester": "Semester", "term": "Semester",
    "prerequisites": "Prerequisites", "prerequisite": "Prerequisites", "prereqs": "Prerequisites",
    "corequisites": "Corequisites", "corequisite": "Corequisites", "coreqs": "Corequisites",
    "standing": "Standing", "notes": "Notes", "note": "Notes",
}

NODE_PASSTHROUGH = ["Semester", "Year", "Standing", "Notes"]
MIDYEAR_CODES = {"M", "MID", "MIDYEAR", "MY"}
_OR_SPLIT = re.compile(r"\s*\|\s*|\s+or\s+", flags=re.IGNORECASE)


def parse_requirements(cell) -> list[list[str]]:
    """Parse a prerequisite/corequisite expression into clauses.

    Returns a list of AND-clauses; each clause is a list of OR-alternatives.
    A single-course clause is a one-element list. Empty / NaN -> [].

        "A; B"          -> [["A"], ["B"]]        (A AND B)
        "A | B"         -> [["A", "B"]]          (A OR B)
        "A; (B | C)"    -> [["A"], ["B", "C"]]   (A AND (B OR C))
    """
    if cell is None or (isinstance(cell, float) and pd.isna(cell)):
        return []
    text = str(cell).strip()
    if not text or text.lower() in {"none", "nan", "-"}:
        return []
    clauses: list[list[str]] = []
    for raw_clause in text.split(";"):
        clause = raw_clause.strip()
        if not clause:
            continue
        alternatives = [
            part.strip().strip("()").strip()
            for part in _OR_SPLIT.split(clause)
        ]
        alternatives = [a for a in alternatives if a]
        if alternatives:
            clauses.append(alternatives)
    return clauses


def _normalize_columns(table: pd.DataFrame) -> pd.DataFrame:
    renamed = {}
    for col in table.columns:
        key = str(col).strip().lower()
        renamed[col] = COLUMN_ALIASES.get(key, str(col).strip().title())
    out = table.rename(columns=renamed)
    if "Semester" in out.columns:
        out["Semester"] = out["Semester"].map(_normalize_semester)
    return out


def _normalize_semester(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return value
    token = str(value).strip()
    return "M" if token.upper() in MIDYEAR_CODES else token


def courses_to_frames(table: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Convert an authored course table into (nodes, edges) DataFrames.

    Used both by `read_courses_csv` and by the legacy `from_checklist_table`
    helper so the two share one grammar.
    """
    table = _normalize_columns(table)
    missing = [c for c in ("Id", "Label", "Units") if c not in table.columns]
    if missing:
        raise ValueError(f"courses table missing required column(s): {missing}")
    if "Category" not in table.columns:
        table["Category"] = ""

    node_cols = ["Id", "Label", "Category", "Units"] + [
        c for c in NODE_PASSTHROUGH if c in table.columns
    ]
    nodes = table[node_cols].copy()
    nodes["Id"] = nodes["Id"].astype(str).str.strip()
    nodes["Units"] = pd.to_numeric(nodes["Units"], errors="coerce")

    rows = []
    for _, row in table.iterrows():
        target = str(row["Id"]).strip()
        for index, clause in enumerate(parse_requirements(row.get("Prerequisites"))):
            requirement = "AND" if len(clause) == 1 else "OR"
            group = "" if len(clause) == 1 else f"{target}#{index}"
            for source in clause:
                rows.append((source, target, PREREQUISITE, "Prerequisite", 2, requirement, group))
        for clause in parse_requirements(row.get("Corequisites")):
            for source in clause:
                rows.append((source, target, COREQUISITE, "Corequisite", 1, "CO", ""))
    edges = pd.DataFrame(rows, columns=EDGE_COLUMNS)
    return nodes, edges


def read_courses_csv(path: PathLike) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Read a standard-format courses.csv into (nodes, edges) DataFrames."""
    table = pd.read_csv(path, dtype=str)
    return courses_to_frames(table)
