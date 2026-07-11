"""Visualization exports: Gephi GEXF, Sankey flow tables, summary tables."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Sequence, Union

import networkx as nx
import pandas as pd

from curricnet.ingest import structural_graph, write_gexf
from curricnet.schema import Curriculum


def export_structural_gexf(curriculum: Curriculum, path: Union[str, Path]) -> None:
    """Write the prerequisite network (with coreq edges) for layout in Gephi."""
    write_gexf(structural_graph(curriculum, include_coreqs=True), path)


def milestone_sankey_table(
    milestones: pd.DataFrame, stages: Sequence[str]
) -> pd.DataFrame:
    """Build a SankeyMATIC/plotly-ready flow table from student milestones.

    `milestones` has one row per student and one boolean column per stage
    (True = milestone reached), `stages` gives the pipeline order. Each
    student is placed at the furthest consecutive stage reached; the flow
    table counts students moving stage[i] -> stage[i+1] and the drop-off at
    each stage ("Stalled at <stage>").
    """
    placement = []
    for _, row in milestones.iterrows():
        reached = 0
        for stage in stages:
            if bool(row.get(stage)):
                reached += 1
            else:
                break
        placement.append(reached)
    counts = pd.Series(placement).value_counts().sort_index()

    rows = []
    remaining = len(milestones)
    for i, stage in enumerate(stages):
        stalled = int(counts.get(i, 0))
        advancing = remaining - stalled
        if stalled:
            source = stages[i - 1] if i else "Enrolled"
            rows.append({"source": source, "target": f"Stalled at {stage}", "value": stalled})
        if advancing:
            source = stages[i - 1] if i else "Enrolled"
            rows.append({"source": source, "target": stage, "value": advancing})
        remaining = advancing
    return pd.DataFrame(rows)


def plot_sankey(flow_table: pd.DataFrame, title: Optional[str] = None):
    """Render a flow table with plotly if available (optional dependency)."""
    import plotly.graph_objects as go  # deferred: plotly is optional

    labels = pd.unique(flow_table[["source", "target"]].values.ravel()).tolist()
    index = {label: i for i, label in enumerate(labels)}
    figure = go.Figure(
        go.Sankey(
            node={"label": labels},
            link={
                "source": [index[s] for s in flow_table["source"]],
                "target": [index[t] for t in flow_table["target"]],
                "value": flow_table["value"].tolist(),
            },
        )
    )
    if title:
        figure.update_layout(title=title)
    return figure


def top_bottlenecks_table(course_table: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Manuscript-ready top-N bottleneck table from cohort.empirical_summary."""
    cols = [c for c in (
        "course", "total_attempts", "student_count", "fail_rate", "retake_self_loop"
    ) if c in course_table.columns]
    return course_table[cols].head(n)
