"""Tests for the standard courses.csv authoring format and grammar."""

from pathlib import Path

import networkx as nx
import pandas as pd
import pytest

from curricnet import load_curriculum, parse_requirements, courses_to_frames
from curricnet.ingest import structural_graph

REPO = Path(__file__).resolve().parents[1]
EXAMPLE = REPO / "templates" / "example"


class TestGrammar:
    @pytest.mark.parametrize("cell,expected", [
        ("", []),
        (None, []),
        ("none", []),
        ("A", [["A"]]),
        ("A; B", [["A"], ["B"]]),
        ("A; B; C", [["A"], ["B"], ["C"]]),
        ("A | B", [["A", "B"]]),
        ("A or B", [["A", "B"]]),
        ("A; (B | C)", [["A"], ["B", "C"]]),
        ("MATH21 ; STAT101", [["MATH21"], ["STAT101"]]),
    ])
    def test_parse_requirements(self, cell, expected):
        assert parse_requirements(cell) == expected


class TestCoursesToFrames:
    def _frames(self):
        table = pd.DataFrame({
            "id": ["A", "B", "C", "D"],
            "title": ["A", "B", "C", "D"],
            "units": [3, 3, 3, 3],
            "prerequisites": ["", "A", "A | B", "A; B"],
            "corequisites": ["", "", "", "A"],
        })
        return courses_to_frames(table)

    def test_and_prerequisite_edges(self):
        _, edges = self._frames()
        d_prereqs = edges[(edges["Target"] == "D") & (edges["Type"] == "Directed")]
        assert set(d_prereqs["Source"]) == {"A", "B"}
        assert set(d_prereqs["Requirement"]) == {"AND"}

    def test_or_prerequisite_shares_group(self):
        _, edges = self._frames()
        c_prereqs = edges[(edges["Target"] == "C") & (edges["Type"] == "Directed")]
        assert set(c_prereqs["Source"]) == {"A", "B"}
        assert set(c_prereqs["Requirement"]) == {"OR"}
        assert c_prereqs["Group"].nunique() == 1  # both alternatives, one group

    def test_corequisite_is_undirected(self):
        _, edges = self._frames()
        coreqs = edges[edges["Type"] == "Undirected"]
        assert len(coreqs) == 1
        assert coreqs.iloc[0]["Source"] == "A" and coreqs.iloc[0]["Target"] == "D"

    def test_missing_required_column_raises(self):
        with pytest.raises(ValueError, match="required column"):
            courses_to_frames(pd.DataFrame({"id": ["A"], "title": ["A"]}))


@pytest.fixture()
def curriculum():
    return load_curriculum(EXAMPLE)


class TestExampleCurriculum:
    def test_loads_and_validates(self, curriculum):
        assert curriculum.validate().ok

    def test_credit_units_excludes_non_credit(self, curriculum):
        assert curriculum.credit_units() == 28  # PE1 (-2) excluded

    def test_or_prerequisite_gives_two_edges(self, curriculum):
        graph = structural_graph(curriculum)
        assert graph.in_degree("MGMT") == 2  # ECON1 and ECON2 alternatives
        assert nx.is_directed_acyclic_graph(graph)

    def test_midyear_semester_normalized(self, curriculum):
        cap = curriculum.nodes.set_index("Id").loc["CAP"]
        assert cap["Semester"] == "M"

    def test_standing_recorded_but_not_an_edge(self, curriculum):
        graph = structural_graph(curriculum)
        assert graph.nodes["MGMT"]["Standing"] == "Junior"
        # "Junior" is not a node, so it produced no edge
        assert "Junior" not in graph
