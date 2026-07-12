# Agent handoff brief

**You are a fresh agent (Hermes, or another Claude instance) picking up this
project.** Read this file top to bottom, then read
[`docs/PROJECT_PLAN.md`](PROJECT_PLAN.md) for strategy. This brief is the
operational manual: environment, guardrails, exact command recipes, the data
pipeline, known pitfalls, and the immediate next actions. Everything you need
to continue is in the repo — no outside context is required.

---

## 0. Mission in one paragraph

Model degree-program curricula as course-prerequisite networks and student
records as empirical progression networks; compute Curricular-Analytics metrics
(Heileman et al. 2018); compare structures across programs, institutions, and
countries. Two papers: **Paper 1 = structural** (public catalog data, scales
now) and **Paper 2 = cohort/empirical** (student records, access-gated). The
BSHRIM (UP Diliman) case study is the worked reference; the job is to
generalize it and build the comparative corpus. Full context: `PROJECT_PLAN.md`.

## 1. Environment (read before running anything)

- **Remote, ephemeral container.** The repo was cloned fresh; the container is
  reclaimed after inactivity. **Anything not committed and pushed is lost.**
  Commit and push at every stable point.
- **Working directory:** `/home/user/curriculum-networks`.
- **Git:** develop on the branch your task assigns (this work used
  `claude/curriculum-network-read-4yjcoy`, already merged to `main`). Push with
  `git push -u origin <branch>`. Do not open a PR unless explicitly asked.
  Match the commit-message style in `git log`; use your own attribution, not a
  prior session's trailer.
- **Python deps are NOT preinstalled.** Run once per container:
  ```bash
  pip install networkx pandas pyyaml pytest        # plotly is optional (viz)
  ```
- **Run the tests** (should be green before and after your change):
  ```bash
  cd /home/user/curriculum-networks && python3 -m pytest tests/ -q
  ```
- **Network policy blocks most external hosts.** In particular all UP and CHED
  sites 403: `*.upd.edu.ph`, `ched.gov.ph`, `chedro1.com` (curl, WebFetch, and
  the proxy all refuse). Only package registries are allowlisted. Check state
  with `curl -sS "$HTTPS_PROXY/__agentproxy/status"`. **Do not fight this** —
  get blocked documents via Google Drive (below) or ask the user to upload.
- **Scratchpad for temp files:** use the session scratchpad dir, not `/tmp`.

## 2. Guardrails (do not violate)

1. **Never fabricate curriculum data.** Prerequisites, units, and course lists
   go into research artifacts. Encode only from an authoritative source you
   have actually read (checklist, catalogue, UC-approved revision doc, CRS).
   If a source is unreachable, stop and ask the user to upload it — do **not**
   guess prerequisites from course numbering or memory. This rule has shaped
   every decision in this repo; keep it.
2. **Document every judgment call.** Id mappings, assumptions, and anything a
   human should confirm go in the curriculum's `curriculum.yaml` `notes:`/`qa:`
   blocks and are flagged `CONFIRM`.
3. **Data governance.** Commit only anonymized/aggregate/published data. Raw
   student-level records must never be committed.
4. **Keep tests green** and regenerate `notebooks/comparison-table.csv` after
   any encode.

## 3. Repo map (where things are)

```
curricnet/         package: schema, format (courses.csv + grammar), ingest,
                   metrics, cohort, viz, compare
curricula/<slug>/  one encoded curriculum: curriculum.yaml + courses.csv
                   (bshrim-2021 is legacy nodes.csv+edges.csv — do not copy that form)
checklists/        UP Diliman OUR checklist corpus (58 valid PDFs + JSON index)
templates/         blank format template + worked example/ (loaded by tests)
data/              BSHRIM reference networks (GEXF), anon tables, summary CSVs
papers/            APacCHRIE manuscript versions
docs/              PROJECT_PLAN, CURRICULUM_FORMAT, data-sources, literature, this file
tests/             58 tests
```

Format spec you must follow when encoding: `docs/CURRICULUM_FORMAT.md`.

## 4. Getting data in (the pipeline that actually works here)

External fetch is blocked, so data arrives two ways:

### A. Google Drive (MCP tools — the user's files live here)
Tools are deferred; load their schemas first:
```
ToolSearch  "select:mcp__Google_Drive__search_files,mcp__Google_Drive__download_file_content,mcp__Google_Drive__read_file_content"
```
- `search_files` — structured query, e.g. `title contains 'Tourism'` or
  `fullText contains 'prerequisite'`. Use `excludeContentSnippets: true` to
  keep results small.
- `read_file_content(fileId)` — natural-language text of a PDF/Doc/Sheet. Best
  for reading a document's content (handles PDFs, docx, Google Docs).
- `download_file_content(fileId[, exportMimeType])` — base64 of the raw bytes.
- **Large-result quirk:** when a result exceeds the token cap it is written to
  a file and the path is returned. Decode from that file:
  ```bash
  jq -r '.content'     TOOL_RESULT_FILE | base64 -d > out.bin   # download_file_content
  jq -r '.fileContent' TOOL_RESULT_FILE            > out.txt    # read_file_content
  ```
  GEXF/manuscripts are multi-MB — expect the file path, not inline content.
- **PDFs already on disk** (e.g. in `checklists/`) can be read directly with the
  **Read tool** (it renders PDF pages) — this is how the Tourism/BPA checklists
  were transcribed.

### B. User uploads
When a source is network-blocked, ask the user to push it to the repo (they
added the whole `checklists/` corpus this way) or drop it in Drive. Give exact
filenames/URLs. Then read and encode.

## 5. Core workflows (copy-paste recipes)

### 5a. Encode a new curriculum — placement pass
1. Read the Registrar checklist PDF (Read tool if in `checklists/`).
2. Create `curricula/<institution-program-year>/`:
   - `curriculum.yaml` — copy `templates/curriculum.yaml`, fill metadata, set
     `prereqs_encoded: false`, `total_units:` = sum of positive units.
   - `courses.csv` — copy `templates/courses.csv`; one row per course with
     `id,title,units,category,year,sem` (leave `prerequisites` blank).
     Conventions: negative units = non-credit (PE/NSTP); `sem` ∈ {1,2,M}.
3. Verify:
   ```python
   from curricnet import load_curriculum
   load_curriculum("curricula/<slug>").validate().raise_if_errors()
   ```

### 5b. Prerequisite pass (turn placement-only into a real network)
1. Read the catalogue / CRS / course-description source.
2. Fill the `prerequisites` (and `corequisites`) column in the existing
   `courses.csv`. Grammar: `;` = AND, `|` or `or` = OR, `()` grouping.
   Class-standing goes in the `standing` column, **not** prerequisites.
3. In `curriculum.yaml` set `prereqs_encoded: true` and add a `qa:` block
   listing ~10% of edges with source page references.
4. Every prereq id must be a row in the same file (validation enforces it).

### 5c. Tests + comparison table
```bash
python3 -m pytest tests/ -q
python3 -c "from curricnet.compare import compare_directory; \
  compare_directory('curricula').to_csv('notebooks/comparison-table.csv', index=False)"
```
`tests/test_encoded_curricula.py` auto-validates every dir under `curricula/`.
Pin notable counts for a new curriculum there if it has real prerequisites.

### 5d. Commit + push
```bash
git add -A && git commit -m "..."      # match git-log style, your own attribution
git push -u origin <branch>
```

## 6. Current state (snapshot — see PROJECT_PLAN §7–8 for the living detail)

- 4 curricula encoded: BSHRIM 2021 (156u, prereqs ✅, legacy form), BSHRIM 2018
  (138u, ✅), BS Tourism 2018 (145u, placement-only), BPA 2018 (144u,
  placement-only). 58 tests passing.
- The UP Diliman checklist corpus (58 PDFs) is in `checklists/`, mostly not yet
  encoded. 20 downloads are corrupt HTML (incl. Physics) — listed in
  `docs/data-sources.md`, need re-download.
- Headline finding so far: the BSHRIM 2018→2021 reform raised structural
  complexity 112→403 and the quantitative chain 2→7; and structural cruciality
  does **not** predict the empirical bottleneck (CALC is ~8th structurally but
  #1 empirically) — the core motivation for the dual-network method.

## 7. Immediate next actions

1. **Tourism + BPA prerequisite pass — BLOCKED on source.** Placement is done.
   Need: NCPAG BPA course descriptions
   (`ncpag.upd.edu.ph/wp-content/uploads/2015/06/BPA-Undergraduate-Course-Description.pdf`)
   and the AIT catalogue (`our.upd.edu.ph/files/catalogue/AIT.pdf`) or CRS Tour
   catalog. Both are network-blocked. **Pending user decision:** upload the two
   PDFs, or allow `*.upd.edu.ph` in the environment network settings. Once
   available, follow recipe 5b (edit the two existing `courses.csv`).
2. **Batch placement-encode the 58 checklists** (recipe 5a) — a large,
   repetitive job; a good fit for a multi-agent workflow. Skip the 20 corrupt
   files until re-downloaded.
3. **Prerequisite enrichment at scale** from the UP CRS course catalog (single
   richest prereq source) once reachable.
4. Then Tier B (CHED PSGs) and Tier C (international) per PROJECT_PLAN §9.

## 8. Known pitfalls & quirks (things that already bit us)

- **MCP results over the token cap are written to a file** — always be ready to
  `jq`/`base64 -d` from the returned path (see §4).
- **Registrar (OUR) checklists have NO prerequisites** — placement only. Don't
  expect to find them there; they're in catalogues/CRS.
- **Degree figures in the manuscript exclude self-loop weights** (e.g. CALC
  in-degree 1,252 − 71 = 1,181 as printed). Reconcile with this in mind.
- **Structural modularity Q = 0.674 (paper Fig. 1) is not reproducible** from
  the anonymized structural tables (best ≈ 0.48). The exact structural GEXF is
  not archived — flag, don't "fix" the number.
- **`pypdf` is broken in this container** (missing `_cffi_backend`). Read PDFs
  with the Read tool or Drive `read_file_content`, not pypdf.
- **20 corrupt checklist PDFs** are 32,414-byte HTML error pages, not PDFs
  (`file checklists/*.pdf | grep HTML`).

## 9. Open questions for the authors (carry these forward)

1. **HRIM 155 corequisite** — anon table says CUL (150); Appendix H p.6 says
   Managerial Control (153). Which is approved?
2. **Structural modularity Q = 0.674** — archive the exact structural GEXF
   behind Figure 1 (repo GEXFs are the empirical network).
3. **ETHICS / LAW** anon↔code mapping (HE 100 / HRIM 160) is ambiguous.
4. **Paper 2 scope** — can other UP programs / partner institutions contribute
   anonymized cohort data?

## 10. Glossary

- **BSHRIM / HRIM** — BS Hotel, Restaurant and Institution Management (UP CHE).
- **CPN** — course-prerequisite network (nodes = courses, directed edges =
  prerequisites).
- **Blocking factor** — # courses a course blocks (its descendants).
  **Delay factor** — longest prereq chain through a course.
  **Cruciality** = blocking + delay. **Structural complexity** = Σ cruciality.
- **PSG / CMO** — CHED Policies, Standards and Guidelines / Memorandum Order
  (the national minimum curriculum per program).
- **OUR** — UP Office of the University Registrar (source of checklists).
  **CRS** — UP Computerized Registration System (per-course prereqs).
- **GE / NSTP / PE** — General Education / National Service Training Program /
  Physical Education (NSTP & PE are non-credit → negative units here).
- **Placement-only** — a curriculum encoded with course placement + units but
  no prerequisite edges yet (`prereqs_encoded: false`).
