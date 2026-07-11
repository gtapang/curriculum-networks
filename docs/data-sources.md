# Data source inventory & acquisition tracker

Status: `have` / `identified` / `requested` / `encoded` (encoded = in `curricula/`).

## Tier A — UP Diliman implemented curricula

| Program | Source | Status |
| --- | --- | --- |
| BS HRIM (2021) | APacCHRIE 2026 anonymized tables; prereqs cross-verified vs Appendix H (UC-approved revision doc) | **encoded** (`curricula/updiliman-bshrim-2021/`) |
| BS HRIM (2018 fast-track, pre-reform) | Appendix H "Existing" program of study + prerequisite statements | **encoded** (`curricula/updiliman-bshrim-2018/`) — enables the 2018→2021 reform comparison |
| BS Physics | NIP curriculum checklist: https://nip.upd.edu.ph/app/uploads/2020/06/BSPhysics_curriculum_post.pdf (+ CRS catalog for prereqs) | identified — **fetch blocked** by this session's network policy (403 on nip.upd.edu.ph); download locally or widen the environment's network access |
| BS Tourism (AIT) | Program page: https://ait.upd.edu.ph/bachelor-of-science-in-tourism/ ; official OUR checklist PDF: https://our.upd.edu.ph/files/Checklist/UG/AIT/AIT_Bachelor%20of%20Science%20in%20Tourism.pdf ; OUR catalogue: https://our.upd.edu.ph/files/catalogue/AIT.pdf | identified — **fetch blocked** by session network policy (403 on ait/our.upd.edu.ph). Known from public summaries: 150 units, 47 courses, ~45 GE units, 19 required tourism subjects, 5 tourism electives (6 u may be one foreign language), 360-hour internship. Upload the checklist PDF to Drive/repo, or allow \*.upd.edu.ph in the environment network policy, to encode. |
| Bachelor of Public Administration (NCPAG) | Program page: https://ncpag.upd.edu.ph/what-we-offer/undergraduate-program/ ; official OUR checklist PDF (2018 curriculum): https://our.upd.edu.ph/files/Checklist/UG/NCPAG/NCPAG_Bachelor%20of%20Public%20Administration.pdf ; course descriptions with prerequisites: https://ncpag.upd.edu.ph/wp-content/uploads/2015/06/BPA-Undergraduate-Course-Description.pdf ; OUR catalogue: https://our.upd.edu.ph/files/catalogue/NCPAG.pdf | identified — **fetch blocked** by session network policy (403 on ncpag/our.upd.edu.ph). Upload the checklist + course-description PDFs to Drive/repo, or allow \*.upd.edu.ph in the environment network policy, to encode. |
| BS Computer Science | DCS curriculum page | identified |
| 2–3 Engineering programs (CE/ME/EEE) | COE curriculum checklists | identified |
| BS Business Administration | VSB/CBA prospectus | identified |
| BA program (e.g., BA Sociology) | CSSP prospectus | identified |

Encoding method: transcribe the official curriculum checklist into the flat
encoder table (Id, Label, Category, Units, Prerequisites, Corequisites,
Semester, Year), then `curricnet.ingest.from_checklist_table`. QA: second
person re-checks 10% of edges against the source (plan, Verification).

## Tier B — CHED PSG minimum curricula (national baseline)

PSG = Policies, Standards and Guidelines CMOs; PDFs on ched.gov.ph and
cms-cdn.e.gov.ph. Each contains the minimum curriculum with prerequisites —
the *regulatory floor* every PH HEI must meet. Target ~8–12 programs:

| Program | CMO | Status |
| --- | --- | --- |
| BS Hospitality Management | CMO 62 s.2017 (BSHM PSG): https://chedro1.com/wp-content/uploads/2019/07/CMO-62-s.-2017-BS-Hospitality-Tourism-Management.pdf (mirror: cmu.edu.ph) | identified — **fetch blocked** by this session's network policy (403); download locally and drop the PDF into the repo or Drive |
| BS Tourism Management | CMO 62 s.2017 companion | identified |
| GE core | CMO 20 s.2013 | identified |
| BS Computer Science | CMO 25 s.2015 | identified |
| Engineering programs (CE, ME, EE...) | CMO 92–101 s.2017 series | identified |
| BS Physics | CMO 51 s.2017 | identified |
| BSBA | CMO 17 s.2017 | identified |
| BS Nursing | CMO 15 s.2017 | identified |

Comparison of interest: institution curriculum vs. its PSG floor — where do
institutions add structure (units, prerequisite chains), and does added
structure concentrate on quantitative gates?

## Tier C — International

| Source | What | Status |
| --- | --- | --- |
| Yang et al. (2024/2025) | 5 Midwestern US institution CPNs | identified — request data from authors (doi:10.1007/s41109-024-00637-z) |
| ASEE public dataset (doi:10.18260/1-2--42606) | longitudinal curricular-analytics dataset | identified — download |
| curricularanalytics.org | US curricula in CurricularAnalytics format | identified — write converter (`ingest`) |
| ASEAN hospitality catalogs (1–2, e.g. Thailand/Malaysia) | hand-encode for the ACCSTP/CATC angle | identified |
| 1–2 US/Japan hospitality programs | hand-encode (APacCHRIE audience relevance) | identified |

## Cohort data (Paper 2)

| Dataset | Status | Notes |
| --- | --- | --- |
| BSHRIM 269 anonymized checklists | **have** (aggregates in repo; raw records off-repo) | published networks in `data/`; raw student-level records must NOT be committed |
| Additional UP Diliman programs | prospective | needs registrar request + ethics clearance; use the anonymization SOP |
| Partner PH HEIs | prospective | data-sharing + ethics template to be drafted |
| ASEE public dataset | identified | external validation cohort |

### Data governance rules

- Only anonymized, aggregate, or published network files are committed.
- Raw student records stay outside the repo; `cohorts/` holds only derived,
  anonymized network files and aggregate tables, each with a provenance note.
- The BSHRIM anonymization protocol (student IDs → BSHRIM-###, course-level
  aggregation) is the SOP template for new cohorts.
