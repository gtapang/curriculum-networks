# Curriculum encoding format (standard)

This is the standard for encoding a degree program's curriculum in this
project. **Use it for every new curriculum.** It is designed so a person can
transcribe an official curriculum checklist plus a course catalog into one
spreadsheet, and the pipeline turns that into a course-prerequisite network
with no further hand-editing.

## Files: one directory per curriculum

```
curricula/<slug>/
    curriculum.yaml     metadata (see below)
    courses.csv         one row per course — the single source of truth
```

`<slug>` is a short, stable, lowercase id, e.g. `updiliman-bstourism-2018`
(`<institution>-<program>-<catalogyear>`). The loader (`curricnet.load_curriculum`)
reads `courses.csv`. A legacy `nodes.csv` + `edges.csv` pair is still read when
no `courses.csv` is present (used only by provenance-preserving imports such as
`updiliman-bshrim-2021`); do **not** author new curricula that way.

## `courses.csv` columns

Headers are case-insensitive and common aliases are accepted (`code`→id,
`name`/`title`→title, `sem`/`term`→semester, `prereqs`→prerequisites, …).

| column | required | meaning |
| --- | --- | --- |
| `id` | ✅ | unique short course code — becomes the network node id (e.g. `MATH21`, `HRIM 131`). Keep it identical everywhere it is referenced. |
| `title` | ✅ | human-readable course name. |
| `units` | ✅ | credit units. **Negative = non-credit** (PE, NSTP, non-credit bridge courses) — the convention lets these appear in the network without inflating the credit total. |
| `category` | recommended | `GE`, `Core`, `Elective`, `PE`, `NSTP`, `Non-Credit`, `Foreign Language`, … |
| `year` | optional | year level (`1`..`N`). |
| `sem` | optional | `1`, `2`, or `M` (midyear). |
| `prerequisites` | optional | requirement expression — see grammar below. |
| `corequisites` | optional | `;`-separated ids taken concurrently. |
| `standing` | optional | class-standing / milestone gate (e.g. `Junior`, `Senior`, `Passed all 5th-sem courses`). Recorded on the node; **not** a course edge. |
| `notes` | optional | free text (source page, caveats). |

### Repeated slots

When a program has repeated slots (PE 1–4, two NSTP terms, elective
placeholders), give each a **unique** id: `PE1`,`PE2`,`PE3`,`PE4`,
`Elective 1`,`Elective 2`, … Duplicate ids are a validation error.

## Prerequisite grammar

The `prerequisites` cell is a boolean expression in conjunctive form:

| syntax | meaning |
| --- | --- |
| `;` | **AND** — separate required clauses: `MATH21; STAT101` needs both |
| `\|` | **OR** — alternatives within a clause: `BA101 \| IE31` needs either |
| `or` (word) | synonym for `\|` |
| `( … )` | optional grouping for readability: `MATH21; (BA101 \| IE31)` |

Rules:

- Every id referenced must be a row in the same file (validation enforces it).
- Class-standing requirements (`Junior Standing`, `Senior Standing`) go in the
  `standing` column, never in `prerequisites` — they are not edges.
- Leave the cell blank for courses with no prerequisite.

Each AND-clause of a single course becomes one directed prerequisite edge
(`Requirement=AND`). An OR-clause becomes one edge per alternative sharing a
`Group` id (`Requirement=OR`); the default network build treats OR edges like
ordinary prerequisites (a conservative over-count for blocking/delay metrics) —
note this when an OR prerequisite is load-bearing for a result.

Corequisites become undirected edges (`Corequisite`) and are excluded from the
prerequisite DAG used for the Curricular-Analytics metrics, but included in the
Gephi/GEXF export.

## `curriculum.yaml`

```yaml
slug: updiliman-bstourism-2018        # matches the directory name
program: BS Tourism                    # full program name
program_short: BST
institution: University of the Philippines Diliman (Asian Institute of Tourism)
country: Philippines
catalog_year: 2018
total_units: 145                       # validated against the courses.csv credit total
source: >                              # citation / URL / document the data came from
  Official OUR curriculum checklist (checklists/Tourism.pdf), 148th UPD UC.
tags: [tourism]
quantitative_courses: [Math 2]         # ids of the math/stat gate courses (optional)
prereqs_encoded: false                 # true once prerequisite edges are filled in
notes: |                               # encoding decisions, mappings, caveats
  ...
qa: |                                  # ~10% edge spot-checks with source page refs
  ...
```

`program`, `institution`, `country`, `catalog_year` are required (validation
warns if missing). `total_units` is checked against the sum of positive units.

## Validation (run before committing)

`load_curriculum(dir)` runs `curriculum.validate()`, which **errors** on:
duplicate ids, prerequisite/corequisite references to unknown ids, unknown edge
types, and prerequisite cycles; and **warns** on missing metadata or a
units-total mismatch. `tests/test_encoded_curricula.py` validates every
directory under `curricula/` automatically, so a new curriculum is covered the
moment it is added.

## Two-stage encoding (checklists vs. catalogs)

UP Registrar (OUR) checklists give course placement and units but **not**
prerequisites. Encode in two passes:

1. **Placement pass** — transcribe id/title/units/year/sem from the checklist;
   leave `prerequisites` blank; set `prereqs_encoded: false`.
2. **Prerequisite pass** — fill `prerequisites`/`corequisites` from the college
   catalogue, the UP CRS course catalog, or course-description PDFs; flip
   `prereqs_encoded: true` and add a `qa:` spot-check block.

A placement-only curriculum loads and reports correct units, but its
structural-network metrics are meaningful only after the prerequisite pass.

## Templates

- `templates/curriculum.yaml`, `templates/courses.csv` — blank starting point.
- `templates/example/` — a small, self-contained curriculum exercising every
  feature (AND, OR, corequisite, standing, midyear, non-credit); loaded by
  `tests/test_format.py` so it stays valid.
