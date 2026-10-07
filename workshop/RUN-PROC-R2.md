# RUN-PROC-R2 · Direito Processual Civil I · 2026-10-06

## Open decision for CEO
Aula 09 received a second `REVISE` after its targeted author pass. The panel confirms the CPC art. 279 sequence and the 2025/2 Q3 mapping, but says closing exercises 2–4 still depend on choices or case facts missing from their reader-facing prompts. Should Aula 09 get another targeted author→panel cycle, or should its current blueprint proceed to page writing with that note recorded? Work on other lessons continues.

## Resolved 07/10
- Require one exact targeted author pass for each of the six second-`REVISE` blueprints; the orchestrator verifies every stated point, and there is no third panel. Aula 08-revelia: test classification of the defendant's own demand, make Figure 1's status consistent, and place the reconvenção distinction in the correct section. Aula 03: reconcile Didier print/PDF locators, explicitly test same-proceeding plurality and pole configuration in the closing tasks, and remove duplicated exam practice. Aula 10-estabilização: make Q2 test S0's construction outcome and keep §05/Q5 within C9. Aula 11-merit: clarify the whole-request contrast in A4/§02 and remove T1 repetition across Hero, §01, and §04. Aula 15: add a documentary means and reasoned admissibility assessment to the integrated exercise. Aula 10: make the learner assess evidence necessity rather than supplying that premise.
- Finish A06, A07, A09, and A13 under the normal author→panel rule.
- Replace F-023 with the F-023b prototype-and-waves rule: prototype A14, then proceed in waves of at most six, P2 first; no mid-run CEO gate.
- Novo Curso, Volume I remains supplementary (“Theory only”); do not promote it to `book_base`.
- Include the 2025/2 P1 with the Sérgio Mattos label in both the exam bank and the relevant lesson pages.
- Before writing A12/A16, retrieve the specified missing CPC/Marinoni sources.
- Resolve conflicting 2018/2 variant answers against the CPC; if unresolved, show both answers and label the divergence.
- Keep canonical issues #84–91, #93, and #95; close duplicate stage issues.

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
| S5a Blueprints/panel | #90 | targeted second-REVISE set complete and verified; A06/A07/A13 approved; A09 awaits CEO ruling recorded above | Luna max author, Sol high panel | blueprint per lesson; panel per lesson |
| S5 Pages | #91 | Aula 14 merged; P2 wave 1 authors (A10-estabilização/A10/A11/A11-merit/A15/A16) in progress | Luna xhigh | one lesson PR at a time; P2 first |
| S6 Front/planta | #93 | checked, ready to integrate | Luna high | `work/plantas/processo-civil-i/structure.md` + staging front |
| S7 Revisão/cartões | #95 | ready after S5 lesson waves | Luna high | generated exam-bank workbench and cards |
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

S5a P1 first batch progress: Aula 01 is `APPROVED`. Aula 05 received first `REVISE` on aligning A1's promised skills with closing exercises and retaining Q2's necessary authenticated context; the author made the targeted revision, and the second panel is `APPROVED`. Aula 02 received first `REVISE` on missing timing/route tasks and repeated trap explanation; its targeted revision passed the second panel, with the 2015 competence question explicitly excluded as outside S0 scope. Aula 03 received first `REVISE` on thread coverage, exam placement, inconsistent locators, and committing all promised closing tests. After the targeted round, the second panel still found inconsistent Didier locators, incomplete assessment of same-proceeding plurality/pole configuration, and duplicate practice placements; this is now escalated to the chairman on #90. Both 2018/2 Q7 answer conflict remains unresolved from memory. Aula 04 received first `REVISE` on explaining the art. 124 assistant/necessary-litisconsorte distinction and making the assistance exercise meet the example-production demand and Caderno restriction; its targeted revision was `APPROVED`. Aula 12 received first `REVISE` for a missing chamamento test, omitted excluded 2015/1 Prova 1 Q5 entry, and conflicting locators; its targeted revision was `APPROVED`. Its Q9 source dependency on missing CPC art. 385 remains flagged. Aula 06-citacao received first `REVISE` on a ruled-list figure, repeated teaching, untested failed mandado, and page-facing scope language; after its targeted revision the second panel is `APPROVED`. Aula 07 received first `REVISE` because its DJE thread did not show a supported completed calculation, source cautions repeated, publication trap repeated, and closing tests did not meet promised preclusion/official-deadline skills. Its targeted author revision was interrupted by the service usage limit. Aula 08 received first `REVISE` to expand the closing set into a sourced contestation-organization task; its targeted revision was `APPROVED`. Aula 08-revelia received second `REVISE` after its author round; unresolved own-demand classification, stale Figure 1 instructions after the figure was cut, and A5 thread-role mismatch are escalated to the chairman on #90. Aula 06 is submitted for panel; its panel turn failed at the service usage limit. Aula 09’s author turn also failed at the service usage limit; a saved draft exists, but no final author check was reported. Second P1 author chunk is incomplete. The service reports retries unavailable until 23:48 local time. Runtime refused additional workers at the 16-thread cap during the batch; source-reader packets were split to disjoint groups as slots freed.

S6 integration: checked front/planta changes committed on staging branch `codex/processo-r2` as `2dfd6c5` (`Add Direito Processual Civil I course front`); branch is now also published as `origin/codex/processo-r2`. No push to `main`.

S4b assignment: seven independent exam-source fragments assigned to Luna high workers at `exam-fragments/<source-id>.json`; all seven are now present and the Luna high merge/dedup is underway. 2025/2 P1 remains excluded as a candidate pending the chairman's answer.

S4b result: merger created `exam-bank.json` and `exam-bank.md`; structural/artifact checks pass with 56 consolidated questions and 9 exclusions. Questions retain per-appearance text, answers, citations, topics, lesson IDs, and kinds. The scanned 2025/2 P1 naming Sérgio Mattos is listed as an excluded candidate pending the chairman's answer.

## Resume · 2026-10-07 S3/S4b corrections
S3 Art. 267 correction: split the missing CPC atom in S2 and added one verdict per lesson (Aula 06 supporting; the other 21 unused). Updated the cap checker so past exams/exercises, including `exam_candidate` sources, remain role-validated but do not count as doctrinal supporting words; recorded the cause and fix in `BUGS.md`. Final `python3 work/pipeline/tools/pipeline_check.py s3 processo-civil-i` → `S3 PASS: 28263 triage rows / 1277 chapters`; unmapped slide decks remain warnings.

S4b chairman ruling: incorporated 2025/2 P1 with the Sérgio Mattos label into the exam bank and mapped all five questions to lessons; the bank now has 61 consolidated questions and eight pre-existing exclusions. The 2025 exam packet is also mapped into Aulas 03, 07, 09, 11, and 12 for generated lesson workbenches. S4 compendia rebuild/check remains pending.

## Resume · 2026-10-06 evening
All three repositories were refreshed with `git pull --ff-only`; each was already current. No new chairman reply appears on #90. Current S5a P1 queue: retry Sol high panel for Aula 06; finish Luna max author round for Aula 07 then panel; finish Luna max authored check for Aula 09 then panel; author and panel Aula 13. Existing second-REVISE cases remain escalated. F-023 still pauses page writing. The Codex usage tool reports zero credits and prior worker errors specify retry after 23:48 São Paulo time, so no worker was restarted before that reset. Duplicate S7 issue #99 was closed; canonical tracking remains #95.

## Resume · 2026-10-07 targeted revisions and source refresh
The six blueprints with a second `REVISE` each received one targeted author pass. The orchestrator verified the listed point against each blueprint: A03 reconciles print/PDF locators, tests same-proceeding plurality and pole configuration, and removes duplicate practice; A08-revelia classifies the defendant's own demand, aligns Figure 1 status/instructions, and places reconvenção in the correct section; A10 asks the learner to assess whether more proof is needed; A10-estabilização makes Q2 test S0's construction outcome and keeps §05/Q5 within C9; A11-merit distinguishes art. 355 from art. 356, including a whole request, and removes the repeated T1; A15's integrated task assesses documentary means and reasoned admissibility without assuming an event occurred. No third panels were commissioned.

A06 received its targeted revision and second panel approval. A07 now includes a single-use, labelled `2025/2 P1 — Sérgio Mattos` Q1 with the supported 06/10/2025 deadline calculation under CPC arts. 219, 224, 1.003 §5, and 1.026 caput; its second panel had requested this exact coverage, and the author completeness/source-locator check passed. A13's second panel approved the targeted date qualification and CPC arts. 352/357 §1 check. A09's second panel still returned `REVISE`; its missing exercise prompts/case facts are recorded as the open CEO question at the top. The duplicate issues are closed; canonical issues remain open. The stale `blocked` label was removed from S5 issue #91 under F-023b.

The 2025/2 P1 exam is in the bank (61 questions, eight exclusions) with all five questions mapped to lessons. The A12/A16 CPC source requests are fulfilled. Marinoni `14.04` now ends at PDF p.322 and `14.04b` begins at PDF p.323. S2 passes with 1,278 atoms; S3 passes with 28,285 triage rows / 1,278 chapters. Compendia rebuilt as 22 lessons / 681 files / 1080 provenance rows. Corrected-state S4 passes with 22/22 manifests / 1080 provenance rows; unmapped slide decks remain warnings.

## Resume · 2026-10-07 S5 prototype
Aula 14 was drafted alone on `codex/proc-r2-aula-14`, with one figure panel. The final canonical reader count is 3,603, within the approved 3,600–3,700-word range. Its Conform slop gate passed (76 advisory findings), `marks_lint` passed with 0 findings, and whole-site `check_all` passed. The served 1280 px breakscan comparison found 48 findings on both live main and staging, 0 new, and 0 on Aula 14. The author inspected the 1512 px selector crop; it is embedded in [PR #108](https://github.com/Benecles/ordenacoes-filipinas/pull/108). The PR branch contains `a457801` and follow-up generated-output fixes `2e031b0` and `f836245`; GitHub's `check_all` passes at `f836245`. Prototype faults are recorded in `FLIGHT-LOG.md` F-028–F-030 and `BUGS.md`.

P2 wave 1 started from `b3499eb` with six disjoint author checkouts. Authors are building the blueprint-scoped pages and their lesson-specific figures; integration will regenerate the shared Processo front and offline outputs one lesson PR at a time.
