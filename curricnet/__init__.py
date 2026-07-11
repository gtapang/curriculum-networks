"""curricnet — curriculum network analysis toolkit.

Models a degree program's curriculum as a course-prerequisite network (CPN)
and student records as an empirical progression network, computes standard
curricular-analytics metrics (Heileman et al., 2018; Stavrinides & Zuev, 2023),
and compares curricula across programs, institutions, and countries.
"""

from curricnet.schema import Curriculum, ValidationReport
from curricnet.format import parse_requirements, read_courses_csv, courses_to_frames
from curricnet.ingest import (
    load_curriculum,
    curriculum_from_frames,
    from_checklist_table,
    structural_graph,
)
from curricnet.metrics import (
    blocking_factor,
    delay_factor,
    cruciality,
    course_metrics,
    curriculum_summary,
)
from curricnet.compare import compare_curricula

__version__ = "0.1.0"

__all__ = [
    "Curriculum",
    "ValidationReport",
    "load_curriculum",
    "curriculum_from_frames",
    "from_checklist_table",
    "structural_graph",
    "parse_requirements",
    "read_courses_csv",
    "courses_to_frames",
    "blocking_factor",
    "delay_factor",
    "cruciality",
    "course_metrics",
    "curriculum_summary",
    "compare_curricula",
]
