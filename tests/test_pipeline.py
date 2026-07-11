"""Unit tests for the curricnet pipeline on synthetic data."""

import networkx as nx
import pandas as pd
import pytest

from curricnet import curriculum_from_frames, compare_curricula, load_curriculum
from curricnet.cohort import build_progression_network
from curricnet.ingest import from_checklist_table, structural_graph
from curricnet.metrics import blocking_factor, delay_factor
from curricnet.viz import milestone_sankey_table


def tiny_curriculum():
    """A -> B -> C chain plus isolated D; B has coreq E."""
    nodes = pd.DataFrame(
        {
            "Id": ["A", "B", "C", "D", "E"],
            "Label": ["Course A", "Course B", "Course C", "Course D", "Course E"],
            "Category": ["Core"] * 5,
            "Units": [3, 3, 3, 3, 3],
        }
    )
    edges = pd.DataFrame(
        [
            ("A", "B", "Directed", "Prerequisite", 2),
            ("B", "C", "Directed", "Prerequisite", 2),
            ("E", "B", "Undirected", "Corequisite", 1),
        ],
        columns=["Source", "Target", "Type", "Label", "Weight"],
    )
    meta = {"program": "Test", "institution": "Test U", "country": "PH",
            "catalog_year": 2026, "total_units": 15}
    return curriculum_from_frames(meta, nodes, edges)


class TestSchema:
    def test_valid_curriculum_passes(self):
        assert tiny_curriculum().validate().ok

    def test_cycle_detected(self):
        curriculum = tiny_curriculum()
        cyclic = pd.concat(
            [
                curriculum.edges,
                pd.DataFrame(
                    [("C", "A", "Directed", "Prerequisite", 2)],
                    columns=curriculum.edges.columns,
                ),
            ]
        )
        with pytest.raises(ValueError, match="cycle"):
            curriculum_from_frames(curriculum.meta, curriculum.nodes, cyclic)

    def test_unknown_endpoint_detected(self):
        curriculum = tiny_curriculum()
        bad = pd.concat(
            [
                curriculum.edges,
                pd.DataFrame(
                    [("GHOST", "A", "Directed", "Prerequisite", 2)],
                    columns=curriculum.edges.columns,
                ),
            ]
        )
        with pytest.raises(ValueError, match="GHOST"):
            curriculum_from_frames(curriculum.meta, curriculum.nodes, bad)


class TestMetrics:
    def test_blocking_and_delay_on_chain(self):
        graph = structural_graph(tiny_curriculum())
        assert blocking_factor(graph, "A") == 2  # B, C
        assert blocking_factor(graph, "C") == 0
        assert delay_factor(graph, "A") == 3  # A-B-C
        assert delay_factor(graph, "B") == 3
        assert delay_factor(graph, "D") == 1

    def test_coreqs_excluded_from_structural_graph(self):
        graph = structural_graph(tiny_curriculum())
        assert not graph.has_edge("E", "B")
        with_coreqs = structural_graph(tiny_curriculum(), include_coreqs=True)
        assert with_coreqs.has_edge("E", "B")


class TestIngest:
    def test_from_checklist_table(self):
        table = pd.DataFrame(
            {
                "Id": ["A", "B", "C"],
                "Label": ["Course A", "Course B", "Course C"],
                "Category": ["Core", "Core", "Core"],
                "Units": [3, 3, 3],
                "Prerequisites": [None, "A", "A; B"],
                "Corequisites": [None, None, None],
            }
        )
        curriculum = from_checklist_table(table, meta={"program": "X"})
        assert len(curriculum.prerequisite_edges) == 3
        assert curriculum.validate().ok

    def test_load_curriculum_roundtrip(self, tmp_path):
        curriculum = tiny_curriculum()
        target = tmp_path / "test-curriculum"
        target.mkdir()
        (target / "curriculum.yaml").write_text(
            "program: Test\ninstitution: Test U\ncountry: PH\ncatalog_year: 2026\ntotal_units: 15\n"
        )
        curriculum.nodes.to_csv(target / "nodes.csv", index=False)
        curriculum.edges.to_csv(target / "edges.csv", index=False)
        loaded = load_curriculum(target)
        assert loaded.slug == "test-curriculum"
        assert len(loaded.nodes) == 5


class TestCohort:
    def test_progression_network_attributes_and_self_loops(self):
        records = pd.DataFrame(
            [
                # student S1 fails MATH in term 0, retakes in term 1 (self-loop), passes
                ("S1", 0, "MATH", 5.0, None),
                ("S1", 1, "MATH", 3.0, None),
                ("S1", 2, "STAT", 2.0, None),
                # student S2 passes MATH then STAT
                ("S2", 0, "MATH", 2.0, None),
                ("S2", 1, "STAT", 1.75, None),
            ],
            columns=["student", "term", "course", "grade", "status"],
        )
        graph = build_progression_network(records)
        math = graph.nodes["MATH"]
        assert math["total_attempts"] == 3
        assert math["student_count"] == 2
        assert math["fail_count"] == 1
        assert graph.get_edge_data("MATH", "MATH")["weight"] == 1
        assert graph.get_edge_data("MATH", "STAT")["weight"] == 2


class TestCompareAndViz:
    def test_compare_curricula(self):
        table = compare_curricula([tiny_curriculum()])
        assert len(table) == 1
        assert table.iloc[0]["courses"] == 5
        assert table.iloc[0]["structural_complexity"] > 0

    def test_milestone_sankey_flows_conserve_students(self):
        milestones = pd.DataFrame(
            {"Passed MATH": [True, True, False], "Passed STAT": [True, False, False]}
        )
        flows = milestone_sankey_table(milestones, ["Passed MATH", "Passed STAT"])
        enrolled_out = flows[flows["source"] == "Enrolled"]["value"].sum()
        assert enrolled_out == 3
