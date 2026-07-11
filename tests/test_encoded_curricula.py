"""Every encoded curriculum must load, validate, and match its declared totals."""

from pathlib import Path

import networkx as nx
import pytest

from curricnet import load_curriculum, curriculum_summary
from curricnet.ingest import structural_graph

REPO = Path(__file__).resolve().parents[1]
CURRICULA = sorted(p.parent for p in (REPO / "curricula").glob("*/curriculum.yaml"))


@pytest.mark.parametrize("path", CURRICULA, ids=lambda p: p.name)
class TestEveryCurriculum:
    def test_loads_and_validates(self, path):
        curriculum = load_curriculum(path)
        report = curriculum.validate()
        assert report.ok, report.errors

    def test_units_match_declared_total(self, path):
        curriculum = load_curriculum(path)
        assert curriculum.credit_units() == float(curriculum.meta["total_units"])

    def test_prerequisites_acyclic(self, path):
        graph = structural_graph(load_curriculum(path))
        assert nx.is_directed_acyclic_graph(graph)

    def test_summary_computes(self, path):
        row = curriculum_summary(load_curriculum(path))
        assert row["structural_complexity"] >= 0
        assert row["courses"] > 0


@pytest.fixture()
def bshrim_2018():
    return load_curriculum(REPO / "curricula" / "updiliman-bshrim-2018")


class TestBshrim2018:
    """Pinned values for the 2018 fast-track encoding (Appendix H)."""

    def test_shape(self, bshrim_2018):
        assert len(bshrim_2018.nodes) == 50
        assert bshrim_2018.credit_units() == 138
        assert len(bshrim_2018.prerequisite_edges) == 21
        assert len(bshrim_2018.corequisite_edges) == 1  # HRIM 104 - HRIM 109

    def test_reform_contrast_computable(self, bshrim_2018):
        """The 2021 reform added units AND structure: the revised curriculum
        must show strictly higher structural complexity and a longer
        quantitative chain than the 2018 fast-track it replaced."""
        before = curriculum_summary(bshrim_2018)
        after = curriculum_summary(
            load_curriculum(REPO / "curricula" / "updiliman-bshrim-2021")
        )
        assert after["credit_units"] - before["credit_units"] == 18
        assert after["structural_complexity"] > before["structural_complexity"]
        assert after["quantitative_chain_length"] > before["quantitative_chain_length"]
