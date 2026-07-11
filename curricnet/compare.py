"""Cross-curriculum comparison: the Paper 1 master table."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Union

import pandas as pd

from curricnet.ingest import load_curriculum
from curricnet.metrics import curriculum_summary
from curricnet.schema import Curriculum


def compare_curricula(curricula: Iterable[Curriculum]) -> pd.DataFrame:
    """One row per curriculum: identification + structural metrics."""
    return pd.DataFrame([curriculum_summary(c) for c in curricula])


def compare_directory(root: Union[str, Path]) -> pd.DataFrame:
    """Load every curriculum under `root` (any subdir with curriculum.yaml)
    and build the master comparison table."""
    root = Path(root)
    curricula = [
        load_curriculum(candidate.parent)
        for candidate in sorted(root.glob("*/curriculum.yaml"))
    ]
    if not curricula:
        raise FileNotFoundError(f"no curricula found under {root}")
    return compare_curricula(curricula)
