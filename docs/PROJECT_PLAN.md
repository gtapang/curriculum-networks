# Curriculum Networks — Project Plan

A comprehensive, comparative study of curriculum structures and student
progression using network science, with a reusable toolkit (`curricnet`) and a
standard data format. This document is the single source of truth for scope,
status, methodology, data, and roadmap.

- **Repository:** `gtapang/curriculum-networks`
- **Working branch:** `claude/curriculum-network-read-4yjcoy` (merged to `main`)
- **Status date:** 2026-07-12
- **Test suite:** 58 passing (`pytest tests/`)
- **Curricula encoded:** 4 (BSHRIM 2018, BSHRIM 2021, BS Tourism 2018, BPA 2018)
- **Picking this up as an agent?** Start with
  [`docs/AGENT_HANDOFF.md`](AGENT_HANDOFF.md) — the self-contained operational
  manual (environment, guardrails, command recipes, next actions).

---

## 1. Context and motivation

The project began with one completed case study: the BS HRIM (UP Diliman)
curriculum network analysis for **APacCHRIE 2026** (Maranan-Montano & Tapang) —
a dual-network study pairing a *structural* course-prerequisite network with an
*empirical* progression network built from 269 anonymized student checklists.
It found that quantitative gate courses (Calculus, Statistics) act as
compounding bottlenecks: e.g. Math 21 with a 37.3% failure rate and a
retake self-loop of weight 71, driving a ~24% on-time graduation rate.

The goal now is to **generalize that case study into a repeatable method and
toolkit** that works for any program at any institution, assemble curriculum
data from the Philippines and abroad, and run a comprehensive comparative
study — deliberately split into two papers so the fast, public-data work is not
gated by the slow, access-restricted work.

## 2. Research questions and the two-paper split

### Paper 1 — Structural (comparative curriculum structure)
Public catalog/checklist data only; scales fast.
- **RQ1.** How do curriculum *structures* differ across programs, institutions,
  and countries when modeled as course-prerequisite networks (CPNs)?
- **RQ2.** How much structure do institutions add on top of the CHED national
  minimum (PSG), and where does the added structure concentrate?
- **RQ3.** Where do quantitative gate courses sit structurally, and does their
  structural position predict empirical bottlenecks? (Bridge to Paper 2.)

### Paper 2 — Cohort / empirical (student progression)
Needs anonymized student records; gated by registrar access + ethics.
- **RQ4.** How does actual student progression deviate from the intended
  curriculum (the design–reality gap)?
- **RQ5.** Which courses are empirical bottlenecks (failure, retake loops,
  incomplete/dropped), and what is their impact on time-to-degree?
- **RQ6.** Can a replicable protocol quantify this for any program given
  checklists + anonymized records?

**Why the split:** Paper 1 runs entirely on public data and can proceed to a
large corpus immediately. Paper 2 depends on data-sharing and ethics approval,
so it must not block Paper 1. The BSHRIM case already demonstrates Paper 2's
method end-to-end.

## 3. Literature positioning

Full annotated bibliography: [`docs/literature.md`](literature.md). Anchors:
- **Aldrich (2015)** — CPN concept (single institution).
- **Heileman et al. (2018)** — Curricular Analytics framework: blocking factor,
  delay factor, cruciality, structural complexity. Reference tooling
  `CurricularAnalytics.jl`.
- **Stavrinides & Zuev (2023)** — whole-institution CPN (Caltech).
- **Yang et al. (2024, 2025)** — comparative CPNs across five US institutions;
  breadth/depth/flux metrics. Direct model for Paper 1.
- **Dawson & Hubball (2014)** — SNA for curriculum decision-making.
- **Gap confirmed:** no Philippine curriculum-network study in the indexed
  literature; nothing compares curricula to a *national regulatory baseline*
  (CHED PSGs) — the main novelty.

## 4. Repository architecture

```
curricnet/                 Python package (networkx + pandas)
  schema.py                Curriculum dataclass + validation
  format.py                STANDARD courses.csv reader + prerequisite grammar
  ingest.py                load_curriculum (courses.csv or legacy nodes/edges), GEXF
  metrics.py               Heileman CPN metrics + graph descriptors
  cohort.py                empirical progression network from student records
  viz.py                   GEXF export, Sankey flow tables, bottleneck tables
  compare.py               cross-curriculum master table
curricula/<slug>/          one encoded curriculum each (curriculum.yaml + courses.csv)
checklists/                UP Diliman OUR checklist corpus (58 valid PDFs + JSON index)
templates/                 blank format template + worked example/
data/                      BSHRIM reference networks (GEXF), anon tables, summary CSVs
figures/                   published BSHRIM figures
papers/                    APacCHRIE manuscript versions (docx + md)
notebooks/                 comparison-table.csv and analysis outputs
docs/                      CURRICULUM_FORMAT.md, literature.md, data-sources.md, this plan
tests/                     58 tests (regression + format + encoded-curricula)
```

## 5. Standard data format

Full spec: [`docs/CURRICULUM_FORMAT.md`](CURRICULUM_FORMAT.md). In brief — one
`courses.csv` per curriculum (single source of truth) plus `curriculum.yaml`:

- Columns: `id, title, units, category, year, sem, prerequisites,
  corequisites, standing, notes`.
- Conventions: **negative units = non-credit** (PE/NSTP/bridge);
  **`sem` ∈ {1, 2, M}** (M = midyear).
- **Prerequisite grammar:** `;` = AND, `|`/`or` = OR, `()` for grouping;
  `standing` column holds class-standing gates (not edges).
- Validation errors on duplicate ids, unknown prereq references, and cycles.

**Two-stage encoding** (the key operational workflow):
1. *Placement pass* — id/title/units/year/sem from the Registrar checklist;
   `prereqs_encoded: false`.
2. *Prerequisite pass* — fill `prerequisites`/`corequisites` from the
   catalogue / CRS / course-description PDFs; set `prereqs_encoded: true` and
   add a `qa:` spot-check block.

## 6. Metrics implemented (`curricnet.metrics`)

- **Per course:** in/out degree, betweenness, **blocking factor** (descendants),
  **delay factor** (longest path through node), **cruciality** = blocking + delay.
- **Per curriculum:** courses, prerequisite/corequisite edges, credit units,
  density, **depth** (longest chain), width, **structural complexity**
  (Σ cruciality), max blocking/delay, top blocking course, Louvain modularity,
  communities, **quantitative-chain length** (longest chain through math/stat
  gate courses).
- **Planned:** flux (Yang 2025); cross-validation of integer metrics against
  `CurricularAnalytics.jl` on 2–3 curricula.

## 7. Data acquisition status

Tracker: [`docs/data-sources.md`](data-sources.md). Summary:

### Encoded (in `curricula/`)
| Program | Units | Prereqs | Notes |
| --- | --- | --- | --- |
| BSHRIM 2021 (UP) | 156 | ✅ | reference; verified vs Appendix H; legacy nodes/edges form |
| BSHRIM 2018 fast-track (UP) | 138 | ✅ | pre-reform; from Appendix H |
| BS Tourism 2018 (UP AIT) | 145 | ⬜ placement-only | prereqs pending (AIT catalogue) |
| BPA 2018 (UP NCPAG) | 144 | ⬜ placement-only | prereqs pending (NCPAG course descriptions) |

### In hand, not yet encoded
- **UP Diliman OUR checklist corpus** — 58 valid checklists + a 78-program JSON
  index (`checklists/`). Placement encodable now; **prerequisites are NOT in
  the checklists** (Registrar convention) and must come from catalogues/CRS.
- 20 checklist downloads failed (32,414-byte HTML error pages), including
  **Physics** — listed in `docs/data-sources.md`; need re-download.

### Blocked by this environment's network policy (403 on `*.upd.edu.ph`, `ched.gov.ph`, `chedro1.com`)
- **Prerequisite sources** for Tourism (AIT catalogue / CRS Tour catalog) and
  BPA (NCPAG course descriptions).
- **BS Physics** checklist (NIP) and **CHED CMO 62 s.2017** BSHM PSG.
- Resolution: upload the PDFs (as done with `checklists/`) **or** allow those
  hosts in the environment network settings.

### International (Tier C, later)
- Yang et al. (2024/2025) five-institution CPN data; ASEE public curricular-
  analytics dataset; curricularanalytics.org curricula (write a converter);
  selected ASEAN + US/Japan hospitality catalogs.

## 8. Results so far

Master table (`notebooks/comparison-table.csv`):

| slug | courses | prereq edges | units | depth | struct. complexity | quant. chain |
| --- | --- | --- | --- | --- | --- | --- |
| bpa-2018 | 53 | 0* | 144 | 1* | 53* | 1* |
| bshrim-2018 | 50 | 21 | 138 | 3 | 112 | 2 |
| bstourism-2018 | 51 | 0* | 145 | 1* | 51* | 1* |
| bshrim-2021 | 55 | 51 | 156 | 7 | 403 | 7 |
`*` placement-only (prerequisites not yet encoded) — metrics are floors.

**Key findings:**
1. **Structure ≠ empirical bottleneck.** In BSHRIM, CALC ranks only ~8th by
   structural cruciality (the MACRO/MICRO intro hubs dominate), yet it is the #1
   empirical bottleneck — motivating the dual-network approach and Paper 2.
2. **The 2018→2021 reform deepened the curriculum dramatically:** structural
   complexity 112→403, depth 3→7, max blocking factor 6→25, quantitative chain
   2→7. The reform that added 18 units also built the long chains that turn one
   Math 21 failure into cascading delays.
3. **Manuscript verification:** every empirical claim in the REVISED FINAL paper
   reconciles with the network data (degree figures exclude self-loops).
   Two items flagged for the authors — see §11.

## 9. Roadmap

### Completed
- **M1** — `curricnet` package, BSHRIM reference curriculum, regression tests,
  research docs.
- **M2** — BSHRIM 2018 encoded from Appendix H; 2021 edges verified; manuscript
  claims cross-checked.
- **Standard format** — `courses.csv` + grammar + spec + templates; three
  curricula migrated.
- **Corpus intake** — full UP Diliman checklist corpus received; Tourism + BPA
  placement-encoded.

### Next
- **M3 — Prerequisite passes (unblock required).** Complete Tourism and BPA
  prerequisites from catalogue/CRS; then BS Physics and CHED CMO 62.
- **M4 — Placement encode the corpus.** Encode all 58 checklists (placement)
  into the standard format; batch job (candidate for a multi-agent workflow).
- **M5 — Prerequisite enrichment at scale.** Attach prerequisites university-
  wide from the UP CRS course catalog (single richest source).
- **M6 — Tier B (CHED PSGs).** Encode ~8–12 national-minimum curricula; run the
  PSG-vs-implemented comparison (RQ2).
- **M7 — Tier C (international).** Yang et al. data, ASEE dataset,
  curricularanalytics.org converter; PH-vs-world comparison (RQ1/RQ3).
- **M8 — Paper 1 draft.** Master table + analyses + figures + outline.
- **M9 — Paper 2 protocol.** Port empirical-network build into `cohort.py` as a
  reproducible SOP; survivorship handling; time-to-milestone survival curves;
  extend to new cohorts as access is granted.
- **Cross-cutting.** `CurricularAnalytics.jl` metric cross-validation; flux
  metric; recover and archive the exact structural GEXF behind Figure 1.

## 10. Blockers and how to resolve

| Blocker | Impact | Resolution |
| --- | --- | --- |
| Network policy blocks `*.upd.edu.ph`, `ched.gov.ph`, `chedro1.com` | Can't fetch prereqs (Tourism/BPA), BS Physics, CMO 62 | Upload PDFs to repo/Drive **or** allow those hosts in the environment network settings |
| 20 corrupt checklist downloads (incl. Physics) | Those programs can't be placement-encoded | Re-download and push |
| Prereqs absent from Registrar checklists | Placement-only curricula have flat metrics | Prerequisite pass from CRS / catalogues / course-description PDFs |
| Raw student records off-repo (correctly) | Paper 2 limited to BSHRIM for now | Data-sharing + ethics track per partner program |

## 11. Open questions for the authors

1. **HRIM 155 corequisite** — anonymized table says Culinary Management (150);
   Appendix H p.6 says Managerial Control (153). Which is the approved version?
2. **Structural modularity Q = 0.674 (Figure 1)** — not reproducible from the
   anonymized structural tables (best achievable ≈ 0.48). Archive the exact
   structural GEXF used for Figure 1.
3. **Anon↔code mapping** of ETHICS and LAW (HE 100 / HRIM 160) is ambiguous
   from the anonymized tables alone.
4. **Paper 2 data scope** — confirm whether additional UP programs / partner
   institutions can contribute anonymized cohort data.

## 12. Verification & QA protocol

- `pytest tests/` — regression tests pinned to published BSHRIM numbers
  (56 nodes/1633 edges; CALC 295 attempts, 37.3%, self-loop 71; STAT 13.2%,
  21; empirical 501/7866), format/grammar tests, and per-curriculum validation.
- Each new curriculum: `validate()` (no duplicate ids, no unknown prereq
  endpoints, acyclic, unit total matches), plus an independent second-pass
  spot-check of ~10% of edges against the source (recorded in `qa:`).
- Comparison table regenerated after every encode.

## 13. Data governance & ethics

- Only anonymized/aggregate/published network files are committed; raw
  student-level records stay off-repo.
- The BSHRIM anonymization protocol (student IDs → BSHRIM-###, course-level
  aggregation) is the SOP template for new cohorts.
- New cohort datasets require data-sharing agreement + ethics clearance before
  intake.

## 14. Key references

See [`docs/literature.md`](literature.md) for the annotated list. Core:
Aldrich (2015); Heileman et al. (2018, arXiv:1811.09676); Stavrinides & Zuev
(2023, doi:10.1007/s41109-023-00543-w); Yang et al. (2024,
doi:10.1007/s41109-024-00637-z; 2025, doi:10.1017/nws.2025.10013); Dawson &
Hubball (2014). Policy: CHED CMOs / PSGs (ched.gov.ph).
