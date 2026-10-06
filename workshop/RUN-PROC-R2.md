# RUN-PROC-R2 · Direito Processual Civil I · 2026-10-06

## Chairman questions
- Aula 10-estabilização's blueprint received a second `REVISE`: Q2 must test S0's construction outcome, and §05/Q5 must stay within C9's narrower doctrinal claims. Please decide whether to require another revision or accept this blueprint.
- Aula 11-merit's blueprint received a second `REVISE`: the whole-request contrast in A4/§02 remains ambiguous, and T1 repeats across the Hero, §01, and §04. The panel protocol escalates after a second `REVISE`; please decide whether to require another revision or accept the current blueprint.
- Aula 15's blueprint received a second `REVISE`: its integrated exercise still needs a documentary means and a reasoned admissibility assessment. The panel protocol escalates after a second `REVISE`; please decide whether to require another revision or accept the current exercise.
- Aula 10's blueprint received a second `REVISE`: the closing exercise still gives the learner the evidence-necessity premise instead of asking them to assess it. The panel protocol says a second `REVISE` goes to the chairman; please decide whether to require another revision or accept the current exercise.
- The syllabus lists Novo Curso, Volume I as basic-essential, while the shelf classifies its acquired copy as supplementary (“Theory only”) and S3 found no directly mapped lesson chapter. I mapped its exact source ID for the primary-word policy but left its shelf role unchanged; should this volume be promoted to book_base? Promoting it would require meeting the S2 15,000-word cap on four currently oversized chapters.
- Should the 2025/2 P1 PDF that names Sérgio Mattos be included in Scarparo’s exam bank? It is in the course folder, but the scanned exam identifies a different professor. It remains a candidate until decided.

## S0 · Source discrepancies resolved
- The PDF has a final general bibliography section: Didier volume I and Novo Curso volume I. The 28/09 intake map omitted it; the new map includes it without changing the week order.
- The brief says P2 has no live pages, but aula-10/11 and their subpages already cover weeks 11–12. The rebuild keeps those matching hrefs; the evidence lessons get new numbers.
- Cintra’s reading cell spans weeks 5–6 in the PDF. The 28/09 map attached it only to week 5; the new map records both weeks and keeps the chapter marked missing.

## Run contract
Master brief: `work/briefs/2026-10-06-processo-r2.md`. Umbrella: #83. Staging branch: `codex/processo-r2` (site repo). The CEO reads the staging build before the final swap PR to `main`; all upstream stage changes are integrated by the orchestrator after checks. S0 and S1 run together by explicit order. S5 lesson order starts with P2.

## Stages
| Stage | Issue | Status | Owner | Output / gate |
|---|---:|---|---|---|
| S0 Course map | #84 | checked, ready to integrate | Sol high | `work/pipeline/processo-civil-i/course-map.{json,md}`; `pipeline_check.py s0` |
| S1 Shelf | #85 | checked, ready to integrate | Luna high | `work/pipeline/processo-civil-i/shelf.csv` + reuse notes; hashes, OCR state, dedup |
| S2 Split | #86 | checked, ready to integrate (12 disjoint source batches) | Luna high | Luna high | chapter/page-marked corpus and indexes; `pipeline_check.py s2` |
| S3 Triage | #87 | checked, ready to integrate | Luna xhigh | lesson × chapter triage; `pipeline_check.py s3` |
| S4 Compendia | #88 | corrected gate passed; ready to integrate | Luna high | assembled lesson workbenches + CPC statute slices |
| S4b Exam bank | #89 | checked, ready to integrate | Luna high | `exam-bank.json` + `.md`, verified questions and exclusions |
| S5a Blueprints/panel | #90 | P2: 5 approved, 4 escalated to chairman; P1 first batch of 6 now starting | Luna max author, Sol high panel | blueprint per lesson; panel per lesson |
| S5 Pages | #91 | blocked on prototype gate | Luna xhigh | one lesson PR at a time; P2 first |
| S6 Front/planta | #93 | checked, ready to integrate | Luna high | `work/plantas/processo-civil-i/structure.md` + staging front |
| S7 Revisão/cartões | #95 | blocked on S4b/S5 | Luna high | generated exam-bank workbench and cards |
| Final swap | #83 | blocked on CEO read | Orchestrator | one PR `codex/processo-r2` → `main`; no merge before CEO review |

## Milestones
- 2026-10-06: both repos pulled (already up to date); umbrella #83 labelled; S0 and S1 issues created and dispatched in parallel.

## S0 · Worker result
Created `work/pipeline/processo-civil-i/course-map.json` and `course-map.md`: 22 lessons, 16 weeks, 5 detached Moodle exports classified in place, 7 planned URLs, and every old aula path retained or explicitly redirected. JSON parsed.
Initial check exposed the S0 schema gap (planned pages and redirects); checker extended. Corrected check: `python3 work/pipeline/tools/pipeline_check.py s0 processo-civil-i` → `S0 PASS: 22 mapped / 17 live lessons`. The fix is recorded in `BUGS.md`. No chairman question.

## S1 · Worker result
Created `work/pipeline/processo-civil-i/shelf.csv` and `shelf-notes.md`: 42 rows (40 physical files, two missing). `python3 work/pipeline/tools/pipeline_check.py s1 processo-civil-i` passes. The scanned 2025/2 P1 names Sérgio Mattos; held as a candidate pending the chairman decision above. CPC refresh is flagged for S2.

## S2 · Work assignment
Six book sources each have a source-specific Luna worker. The 34 remaining physical sources are assigned in six non-overlapping chunks (six or fewer IDs each). Runtime refused further child threads at the configured 16-thread ceiling; chunk owners are finishing remaining IDs directly. No source directories overlap. The stage-wide checker runs only after all indexes/text land. S6 started in parallel because it depends only on S0.


## S6 · Front/planta result
The staging front and `work/plantas/processo-civil-i/structure.md` cover 16 syllabus weeks, 22 mapped lesson links, and source-listed readings. Evaluation dates are omitted. Final corrected-state check: `python3 tools/fronts/check_register_data.py processo-civil-i` → `processo-civil-i: 22 lessons checked` (exit 0).


## S2 · First course-wide gate
`python3 work/pipeline/tools/pipeline_check.py s2 processo-civil-i` found 9 errors across 1,267 indexed chapters. Five duplicate Part II IDs on Part III chapters in Novo Curso v1 and four document-shaped indexes lacking `chapters` entries are assigned back to their source owners. No source text changed; one corrected-state course gate remains.

S2 corrected-state gate: `python3 work/pipeline/tools/pipeline_check.py s2 processo-civil-i` → `S2 PASS: 1276 indexed chapters` (exit 0).

S3 protocol correction: the global S2 catalog is 40 indexes / 1,276 chapter entries; the shared brief now uses that passed-gate inventory. A checker mismatch that rejected any non-basic-essential primary (including assigned reading or mapped slides) was corrected: such rows may be primary when their title/rationale matches the mapped syllabus, while only basic-essential primary words count toward the 5,000-word threshold. Known-bad policy fixture reproduced the rejection pre-fix and returned no errors post-fix; diagnosis recorded in `BUGS.md`.

S3 execution note: 20 of 22 lesson matrices are assigned; 10 have returned completed, checked outputs. The first lesson files all contain 1,276 unique chapter keys. Remaining lessons are queued until a slot opens. Nested workers use disjoint scratch-only chapter batches; lesson owners merge their own batches and check only their lesson matrix.

S3 progress: all 22 lesson units are assigned. Fourteen checked matrices are complete; eight remain active. The 16-thread ceiling is documented in the worker handoffs; remaining parents finish any unspawned chapter ranges directly and preserve disjoint ownership.

S3 merge started after all 22 lesson files reported complete and checked. The final output is `triage.csv`; a dedicated Luna xhigh worker will add the prerequisite-primary background closure and run the one course-wide S3 gate. Aula 18 carries the map's concrete `thin_primary_reason` because it has no assigned reading and no directly matched basic-essential source reaching 5,000 words.

S3 policy mapping: the two bibliography references resolve to `didier-curso-vol1-2017` and `marinoni-novo-curso-vol1-2017`. The course map now names those exact source IDs in `policy.basica_essencial_source_ids`, avoiding fuzzy matches to Vol. II/Mitidiero. Marinoni Vol. I remains `book_supplementary` pending the chairman question above.

S3 second gate after matcher fixes: `pipeline_check.py s3 processo-civil-i` reported six lessons below 5,000 words from the exact basic-essential sources (Aula 01, 04, 06, 14, 15, 17); the other 16 lessons passed policy. The primary matcher now includes lesson title/scope; the essential bibliography IDs are exact. Six lesson owners are checking for direct-fit chapters in those two books and will either update their own matrix or provide a source-grounded thin-primary reason. The global matrix has 28,072 base rows + 162 background rows. Warnings: no slide deck is mapped in the shelf for any lesson.

S3 repair results: Aula 01 and 04 promoted directly relevant Didier Vol. I chapters to primary; Aula 17 promoted a relevant Marinoni Vol. I §4.5 chapter. Aula 06, 14, and 15 have one-sentence thin-primary reasons after checking both basic-essential indexes. Aula 18 has its existing thin-primary reason. The merger is rebuilding base rows/background closure from current part files and will run the final gate once.

S3 final gate: `python3 work/pipeline/tools/pipeline_check.py s3 processo-civil-i` → `S3 PASS: 28241 triage rows / 1276 chapters` (exit 0). Warnings: no slide deck is mapped in the shelf for any lesson.

S4 result: builder created 22 lesson compendia; worker reports 659 generated files and 683 provenance rows. `pipeline_check.py s4 processo-civil-i --site /Users/benecles/Developer/ordenacoes-filipinas-proc-r2` passed with 22/22 manifests; warnings: no slide deck is mapped for each lesson. Mechanical existence check found 22 `00-index.md` files. S4b now starts; 2025/2 P1 candidate naming Sérgio Mattos stays excluded pending the chairman's answer.

S4 correction: S5a author found `compendium/aula-10-estabilizacao/60-statute.txt` absent, confirmed by the orchestrator. The S4 builder now emits the file for all 22 workbenches with per-article provenance from the refreshed 2026-10-06 CPC capture. The assembler/checker defect is recorded in `BUGS.md`. Corrected gate: `pipeline_check.py s4 processo-civil-i --site /Users/benecles/Developer/ordenacoes-filipinas-proc-r2` → PASS, 22/22 manifests, 1,082 provenance rows; unmapped slide decks remain warnings. Mechanical count confirms 22 statute files. S5a verdicts that depended on the prior indexes remain provisional until re-evaluated against the corrected indexes.

S5a first P2 batch final panel status after the corrected S4 index: Aula 11 and Aula 14 are `APPROVED`. Aula 10, Aula 10-estabilização, Aula 11-merit, and Aula 15 remain `REVISE` after the author round, so each is escalated to the chairman under the two-REVISE rule.

S5a next P2 results: Aula 16, Aula 17, and Aula 18 are `APPROVED`. Aula 16's mapped Q9 needs a later S5 source request because its cited CPC arts. 125, 127, 385, 447 §§4–5, 459 and Marinoni §9.12 are absent from its current compendium. No answer rationale is inferred from memory. The first six P1 lesson blueprints are now starting; P2 remains the first page-writing batch once F-023 is lifted.

S6 integration: checked front/planta changes committed on staging branch `codex/processo-r2` as `2dfd6c5` (`Add Direito Processual Civil I course front`). No push to `main`.

S4b assignment: seven independent exam-source fragments assigned to Luna high workers at `exam-fragments/<source-id>.json`; all seven are now present and the Luna high merge/dedup is underway. 2025/2 P1 remains excluded as a candidate pending the chairman's answer.

S4b result: merger created `exam-bank.json` and `exam-bank.md`; structural/artifact checks pass with 56 consolidated questions and 9 exclusions. Questions retain per-appearance text, answers, citations, topics, lesson IDs, and kinds. The scanned 2025/2 P1 naming Sérgio Mattos is listed as an excluded candidate pending the chairman's answer.
