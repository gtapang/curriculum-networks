# Data source inventory & acquisition tracker

Status: `have` / `identified` / `requested` / `encoded` (encoded = in `curricula/`).

## Tier A — UP Diliman implemented curricula

| Program | Source | Status |
| --- | --- | --- |
| BS HRIM (2021) | APacCHRIE 2026 anonymized tables | **encoded** (`curricula/updiliman-bshrim-2021/`) |
| BS Physics | NIP curriculum checklist (co-author's institute) | identified |
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
| BS Hospitality Management | CMO 62 s.2017 (BSHM PSG) | identified |
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
