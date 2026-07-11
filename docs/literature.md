# Annotated bibliography — curriculum network analysis

Papers retrieved via academic search (scite), 2026-07-11. Grouped by the
two-paper split. Add annotations as papers are read in full.

## Foundations / metric frameworks (both papers)

- **Aldrich, P. R. (2015).** The curriculum prerequisite network: Modeling the
  curriculum as a complex system. *Biochemistry and Molecular Biology
  Education*, 43(3), 168–180.
  First CPN formulation; single institution (Benedictine); community
  clusters, bridges, hub courses. Already cited in the APacCHRIE paper.
- **Heileman, G. L., Abdallah, C. T., Slim, A., & Hickman, M. (2018).**
  Curricular analytics: A framework for quantifying the impact of curricular
  reforms and pedagogical innovations. arXiv:1811.09676.
  https://doi.org/10.48550/arxiv.1811.09676
  THE metric framework: blocking factor, delay factor, cruciality,
  structural complexity. Open tooling: CurricularAnalytics.jl and
  curricularanalytics.org. `curricnet.metrics` implements these definitions;
  cross-validate against the Julia package (planned, see plan Phase 2).
- **Dawson, S., & Hubball, H. (2014).** Curriculum analytics: Application of
  social network analysis for improving strategic curriculum decision-making
  in a research-intensive university. *Teaching & Learning Inquiry*, 2(2).
  https://doi.org/10.20343/teachlearninqu.2.2.59
  Earlier SNA-for-curriculum-decisions framing; useful for the policy angle.

## Paper 1 — structural / comparative CPN studies

- **Stavrinides, P., & Zuev, K. M. (2023).** Course-prerequisite networks for
  analyzing and understanding academic curricula. *Applied Network Science*.
  https://doi.org/10.1007/s41109-023-00543-w
  Whole-institution CPN (Caltech); node/edge-level metrics for curriculum
  redesign. Benchmark for institution-level analyses.
- **Yang, B., et al. (2024).** Comparative analysis of course prerequisite
  networks for five Midwestern public institutions. *Applied Network Science*,
  9(1), 25. https://doi.org/10.1007/s41109-024-00637-z
  The direct model for Paper 1's comparative design. Already cited in the
  APacCHRIE paper. Action: request/download their network data.
- **(2025).** Breadth, depth, and flux of course-prerequisite networks.
  *Network Science*. https://doi.org/10.1017/nws.2025.10013
  Follow-up metrics (breadth/depth/flux) — `curricnet.metrics.curriculum_summary`
  exposes depth/width; add flux when the paper's definition is extracted.
- **Extending curricular analytics to analyze undergraduate physics programs
  (2024).** *Physical Review Physics Education Research*, 20, 020143.
  https://doi.org/10.1103/physrevphyseducres.20.020143
  Discipline-specific application (physics) — template for the UP Diliman
  physics encoding.
- **Applying centrality measures to the course prerequisite network analysis
  of the undergraduate civil engineering curriculum (2025).**
  https://doi.org/10.18173/2354-1075.2025-0137
  Vietnam — closest Southeast Asian comparator found; useful for the ASEAN angle.
- **Does curricular complexity imply program quality? (ASEE 2019).**
  https://doi.org/10.18260/1-2--32677 — and **Curricular complexity versus
  quality of computer science programs.** arXiv:2006.06761.
  Negative/nuanced results linking complexity to quality — important to cite
  to avoid overclaiming that lower complexity is always better.

## Paper 2 — cohort / progression studies

- **A new public dataset for exploring engineering longitudinal development by
  leveraging curricular analytics (ASEE 2023).** https://doi.org/10.18260/1-2--42606
  Public longitudinal dataset — candidate external validation cohort. Action:
  download and convert to `curricnet.cohort` record format.
- **Curricular complexity as a metric to forecast issues with transferring
  into a redesigned engineering curriculum (ASEE 2020).**
  https://doi.org/10.18260/1-2--34363 — transfer-student angle.
- **Examining the impacts of the Wright State model for engineering
  mathematics education through curricular analytics (ASEE 2023).**
  https://doi.org/10.18260/1-2--43521
  Directly relevant: an intervention on the *math gate* (the CALC analogue),
  evaluated with curricular analytics. Key citation for recommendations.

## Philippine context

- No Philippine curriculum-network study found in the indexed literature
  (searches: "Philippines curriculum network/prerequisite/analytics",
  2026-07-11) — the gap both papers fill.
- Policy corpus: CHED CMOs / Policies, Standards and Guidelines (PSGs) define
  the national minimum curricula (see docs/data-sources.md).
- ASEAN standards: ACCSTP / CATC (already discussed in the APacCHRIE paper)
  for the regional hospitality benchmark.

## Search log

| Date | Tool | Query | Notes |
| --- | --- | --- | --- |
| 2026-07-11 | scite | "curricular analytics" AND ("structural complexity" OR "curricular complexity") AND graduation | framework + ASEE cluster |
| 2026-07-11 | scite | "course prerequisite network" OR ("curriculum network" AND "student progression") | CPN cluster (Caltech, 5-institution, breadth/depth/flux) |
| 2026-07-11 | scite | Philippines AND curriculum AND ("higher education" OR CHED) AND (network OR prerequisite OR analytics) | no PH CPN work → gap |
| 2026-07-11 | web | CHED CMO "policies standards and guidelines" curriculum prerequisites | PSG PDFs on ched.gov.ph / cms-cdn.e.gov.ph |
