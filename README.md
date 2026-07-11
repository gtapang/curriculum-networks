# curriculum-networks

Curriculum Networks analysis: a toolkit (`curricnet`) and datasets for
modeling degree programs as course-prerequisite networks, computing
curricular-analytics metrics, and studying student progression — across
programs, institutions, and countries.

## Quick start

```bash
pip install -e .[dev]
pytest tests/            # regression suite reproduces the published BSHRIM results
```

```python
from curricnet import load_curriculum, course_metrics, curriculum_summary
from curricnet.compare import compare_directory

bshrim = load_curriculum("curricula/updiliman-bshrim-2021")
course_metrics(bshrim)          # blocking/delay factor, cruciality per course
curriculum_summary(bshrim)      # one master-table row
compare_directory("curricula")  # cross-curriculum comparison table
```

- `curricnet/` — package: `schema` (validation), `ingest` (CSV/checklist/GEXF),
  `metrics` (Heileman blocking/delay/cruciality/structural complexity + CPN
  descriptors), `cohort` (empirical progression networks from student records),
  `viz` (GEXF/Sankey/tables), `compare` (master table).
- `curricula/` — one directory per encoded curriculum
  (`curriculum.yaml` + `nodes.csv` + `edges.csv`).
- `docs/literature.md` — annotated bibliography; `docs/data-sources.md` —
  acquisition tracker (UP Diliman, CHED PSGs, international).
- `tests/` — regression tests pinned to the published APacCHRIE 2026 numbers.

## Reference case study (APacCHRIE 2026)

Working data and documents for **"Curriculum Network Analysis of Quantitative
Bottlenecks in Hospitality Management Education"** (Maranan-Montano & Tapang,
APacCHRIE 2026) — a dual-network study of the BS HRIM (2021) curriculum at UP
Diliman: a structural course-prerequisite network vs. an empirical progression
network built from 269 anonymized student curriculum checklists.

## Repository contents

Files imported from the project's Google Drive folder (2026-07-11):

### `data/`
| File | Description |
| --- | --- |
| `nodes_table_anon.csv` | Anonymized course nodes (Id, Label, Category, Units) |
| `edges_table_anon.csv` | Anonymized prerequisite/corequisite edges (Source, Target, Type, Label, Weight) |
| `course_network.gexf` | Structural BS HRIM course network (normalized course names, weighted transitions) |
| `student_sequences.gexf` | Empirical student progression network (course-taking sequences incl. retakes) |
| `lar-00.gexf` | Edited course network export (Gephi) |
| `lar-course-network-edited.gephi` | Gephi project file for the edited course network |
| `summary_tables.csv` | Cohort distribution, WAG, completion-rate, and risk-indicator summary tables |

### `figures/`
| File | Description |
| --- | --- |
| `figure1_structural.png` | Figure 1 — structural curriculum network |
| `figure2_empirical.png` | Figure 2 — empirical progression network |
| `student_flow_sankey.png` | Sankey diagram of student flow/current standing |

### `docs/`
| File | Description |
| --- | --- |
| `v10-manuscript-curriculum-network-analysis.md` | Markdown export of the v10 manuscript (Google Doc) |
| `REVISED FINAL VERSION TEMPLATE (APacCHRIE 2026 Main Conference) MONTANO & TAPANG.docx` | Latest submitted full-paper version |
| `presentation-montano-tapang-2026-curriculum-network-analysis.txt` | Text export (slides + speaker notes) of the conference presentation |
