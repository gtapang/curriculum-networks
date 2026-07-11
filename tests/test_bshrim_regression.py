"""Regression tests: the pipeline must reproduce the published BSHRIM results.

Reference values come from the APacCHRIE 2026 paper/presentation and the
published network files in data/:
  - structural network: 55 course slots, 156 credit units, acyclic
  - empirical course network (data/course_network.gexf): 56 nodes, 1633 edges
  - Math 21 (CALC): 295 attempts, 194 students, 37.29% failure, retake
    self-loop weight 71
  - Stat 101 (STAT): 13.25% failure, retake self-loop weight 21
  - student sequence network (data/student_sequences.gexf): 501 nodes, 7866 edges
"""

from pathlib import Path

import networkx as nx
import pandas as pd
import pytest

from curricnet import load_curriculum, course_metrics, curriculum_summary, structural_graph
from curricnet.cohort import empirical_summary, structural_empirical_divergence

REPO = Path(__file__).resolve().parents[1]
BSHRIM = REPO / "curricula" / "updiliman-bshrim-2021"


@pytest.fixture(scope="module")
def curriculum():
    return load_curriculum(BSHRIM)


@pytest.fixture(scope="module")
def course_gexf():
    return nx.read_gexf(REPO / "data" / "course_network.gexf")


class TestStructural:
    def test_loads_and_validates(self, curriculum):
        report = curriculum.validate()
        assert report.ok, report.errors

    def test_course_slots_and_units(self, curriculum):
        assert len(curriculum.nodes) == 55
        assert curriculum.nodes["Id"].is_unique
        assert curriculum.credit_units() == 156

    def test_prerequisite_network_shape(self, curriculum):
        graph = structural_graph(curriculum)
        assert graph.number_of_nodes() == 55
        assert graph.number_of_edges() == len(curriculum.prerequisite_edges)
        assert nx.is_directed_acyclic_graph(graph)

    def test_quantitative_gate_metrics(self, curriculum):
        """Pinned Curricular Analytics values for the quantitative chain.

        Note the design-reality gap: structurally CALC ranks only ~8th by
        cruciality (the MACRO/MICRO hubs dominate), yet empirically it is the
        #1 bottleneck — the core Paper 2 contrast.
        """
        table = course_metrics(curriculum).set_index("Id")
        assert table.loc["PRECALC", "blocking_factor"] == 9
        assert table.loc["CALC", "blocking_factor"] == 8
        assert table.loc["STAT", "blocking_factor"] == 8
        assert table.loc["CALC", "delay_factor"] == 7  # sits on a longest chain
        assert table.loc["CALC", "cruciality"] == 15
        # the structural top blockers are the intro hub courses, not CALC
        assert table["blocking_factor"].idxmax() == "MACRO"
        assert table.loc["MACRO", "blocking_factor"] == 25
        assert table.index.get_loc("CALC") < 10  # still a top-10 crucial course

    def test_summary_row(self, curriculum):
        row = curriculum_summary(curriculum)
        assert row["courses"] == 55
        assert row["credit_units"] == 156
        assert row["quantitative_chain_length"] >= 5  # PRECALC->CALC->ORM->CONTROL->FIN...
        assert row["structural_complexity"] > 0


class TestEmpirical:
    def test_course_network_shape(self, course_gexf):
        assert course_gexf.number_of_nodes() == 56
        assert course_gexf.number_of_edges() == 1633

    def test_math21_bottleneck(self, course_gexf):
        table = empirical_summary(course_gexf).set_index("course")
        math21 = table.loc["Math 21"]
        assert math21["total_attempts"] == 295
        assert math21["student_count"] == 194
        assert math21["fail_rate"] == pytest.approx(0.3729, abs=1e-4)
        assert math21["retake_self_loop"] == 71

    def test_stat101_bottleneck(self, course_gexf):
        table = empirical_summary(course_gexf).set_index("course")
        stat101 = table.loc["Stat 101"]
        assert stat101["fail_rate"] == pytest.approx(0.1325, abs=1e-4)
        assert stat101["retake_self_loop"] == 21

    def test_math21_is_worst_high_volume_course(self, course_gexf):
        """Among courses with >=100 attempts, Math 21 has the highest failure rate."""
        table = empirical_summary(course_gexf)
        high_volume = table[pd.to_numeric(table["total_attempts"]) >= 100]
        assert high_volume.iloc[0]["course"] == "Math 21"

    def test_student_sequences_shape(self):
        graph = nx.read_gexf(REPO / "data" / "student_sequences.gexf")
        assert graph.number_of_nodes() == 501
        assert graph.number_of_edges() == 7866

    def test_divergence_metrics_computable(self, curriculum, course_gexf):
        result = structural_empirical_divergence(structural_graph(curriculum), course_gexf)
        assert result["structural_edges"] > 0
        assert result["empirical_edges"] > 0
        assert 0 <= result["emergent_edge_fraction"] <= 1
