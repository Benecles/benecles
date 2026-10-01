# CUFRGS Source Pipeline (v1, 2026-09-30)

Owner: Claude (CEO). Direction: Benecles, 30/09. Codex runs it; Claude gates each stage.

**Why this exists.** The site's weak lessons weren't written badly so much as fed badly. Writers got slides plus whatever extracts happened to be lying around, so they described instead of explaining. From now on, nothing gets written until its material has been prepared: mapped, split, triaged, stitched and documented. The prep is mundane, and it is the job.

**Coordination (since 01/10): GitHub Issues in `Benecles/ordenacoes-filipinas-workshop`.** One issue per stage per course (label `codex` + `pipeline` + `course:<x>`; `blocked` until its predecessor has `gate:approved`). When a stage is done: comment the check result and doubts on its issue, add `needs-gate`, STOP. The CEO answers on the issue and adds `gate:approved` (or asks for a fix). Lesson PRs go to the site repo with "Closes Benecles/ordenacoes-filipinas-workshop#n".

**Order: understand → prepare the workbench → write (or edit).** No stage starts before the previous one passes its check.

Everything lives under `work/pipeline/<course>/`. Book text stays out of git (`work/pipeline/**/text/`, `**/chapters/`, `**/compendium/**/*.txt` are git-ignored). Maps, indexes, blueprints and logs are committed.

---

## S0 · Course map: what this course is

Read the plano de ensino, the Moodle snapshot and the slide decks' titles. Write `course-map.json` (+ a readable `course-map.md`):
- each lesson, in the syllabus's own order: id (the live page's href), syllabus line, what the lesson must let the reader do (one line), exam;
- **prerequisites:** for each lesson, the earlier lessons whose understanding it *depends on*, each with one line saying why. This is what lets a late lesson carry forward early material (S3);
- the bibliography, split into base and supplementary, as the plano lists it.

Model: **Sol, high.** It's one short run per course, and every later stage inherits its mistakes.
Gate: Claude reads the map. Check: `pipeline_check.py s0 <course>` (every live lesson page is in the map; every prerequisite points backwards).

## S1 · Shelf: what we have

`shelf.csv`: one row per source: slides, Moodle material, base and supplementary books, statutes, past exams. Columns: role, path, sha256, format, text status (text layer / OCR done / needs OCR / missing).
- **Reuse before re-extracting:** `work/book-extracts/`, `work/controle-depth/extracts/`, `work/source-intake-2026-09-28/`, and every `*-prep/` folder. List what you reused.
- Missing = a row marked `missing`. Never fill a gap from peer summaries or model memory.
- Scans: local OCR only (Tesseract), never cloud vision.

Model: Luna, high.

## S2 · Split: books into chapters

For each available book: find its sumário (the book's own table of contents) and cut the text into `chapters/<source-id>/<nn>-<slug>.txt`, one file per chapter, every page marked `===== p. N (PDF M) =====`. Record `chapters/<source-id>/index.json` (title, printed and PDF page span, word count).
- Chapters are the unit: we cut by the book's structure, not by keyword hits.
- A chapter over ~25k words gets flagged in the index. Split it at its own section headings only if S3 needs a part of it; that's the exception.
- Slides: one file per deck, with page markers. Moodle exercise lists and past exams: one file each.

Model: Luna, high (mostly scripting). Check: `pipeline_check.py s2` (page markers continuous, no gaps or overlaps between chapters, word counts plausible).

## S3 · Triage: which chapter feeds which lesson

**This is one of the two stages that decide quality.** The point is precision: Aula 09 gets chapter 3 of book 2 and chapter 9 of book 3, *not* every book. A writer who reads everything reads nothing carefully. A triage that assigns a whole book to a lesson has failed.

`triage.csv`: for every chapter × lesson it serves: role (`primary` | `supporting`), one line of why. Every chapter gets a verdict, including `unused` with a reason.
**Dependency closure:** a lesson also receives the `primary` chapters of its prerequisite lessons (from S0) as `background`. A chapter that's crucial for Aula 01 rides along into Aula 09 when Aula 09 builds on Aula 01.

Model: **Luna, xhigh.** Check: `pipeline_check.py s3` (every chapter has a verdict; every lesson has its slides plus at least one primary book chapter, or an explicit `no book covers this` note; background equals the prerequisites' primaries).

## S4 · Compendium: one workbench per lesson

`compendium/<lesson>/`: the lesson's material stitched into ordered files: `10-slides.txt`, `20-primary-*.txt`, `30-supporting-*.txt`, `40-background-*.txt`, `50-exercises-and-exams.txt`, plus `00-index.md`, the provenance table (file → source, chapter, pages, role, why it's here, sha256).
A script assembles it from S2 + S3; no model judgment involved. `tools/pull_source.py <lesson> <source-id> <chapter-or-pages> "<why>"` adds material later, appending both the file and its index row.

## S5 · Edit: one agent, one lesson, text and figures together

Each lesson gets **one** agent, in one context, that owns both the text and every figure on the page. It edits the live page (adding, replacing, fixing) rather than writing from scratch. The same architecture produces writers for new lessons.

1. **Blueprint (Luna, max). The other stage that decides quality: plan before you write, and make the plan transparent.** Read the live page, the compendium index, the slides, the S0 line and the exam questions. Write `compendium/<lesson>/blueprint.md`, the lesson's architecture from the top down:
   - **Function:** what the lesson lets the reader do, and how they'll know they can (the closing exercises).
   - **Sequence:** sections in order. For each: the claim it makes, why it comes there (what it needs from before, what it sets up), and the compendium files and pages it draws on. A section with no source pages has to say why.
   - **Coverage:** every point of the syllabus line and every matching exam/exercise question, each mapped to a section; anything deliberately left out, with the reason.
   - **Callouts and devices:** each callout (lex block, case folder, contrast, recall) and why it earns its place.
   - **Figures:** each one gives the claim it carries, its form (Visual Genres → *Instruments, not diagrams*), what the reader does with it, and what they know afterwards.
   - **Live page:** what stays, what gets replaced, what gets added, what gets cut, and why.
   - **Size:** estimated words; one sitting (~2.5–4.5k), or a proposed split.
   Then STOP for the panel (S5a).
**S5a · The panel (Sol, high).** A separate agent judges each blueprint the way a thesis committee judges a proposal: it doesn't know the material as deeply as the author, but it can tell whether the plan is sound. It reads only the blueprint, the S0 map, the compendium index and the exam questions, never the full chapters. Its rubric:
   1. Is the function concrete, and do the closing exercises test it?
   2. Does every section trace to specific compendium pages, and does the order make sense (prerequisites before use)?
   3. Is the syllabus line covered, with every matching exam question placed somewhere?
   4. Does every figure pass the instrument test? Any box-and-arrow plan is rejected outright.
   5. Is it one sitting, and is what gets cut from the live page defensible?
   The verdict, in `panel.md`, is either **APPROVED** or **REVISE** with at most 5 numbered, specific points. The author revises; after a second REVISE, it escalates to Claude. Only APPROVED blueprints proceed to writing. Claude spot-checks panel verdicts, especially the first ten, to calibrate it.

2. **Read.** Read the primary chapters in full. When an author points back or forward ("como visto no capítulo 3…", "ver adiante…") and that material isn't in the compendium, pull it with `pull_source.py` and log the request in `requests.md` (what, why, from where). Those requests are data: they tell us what S3 missed.
3. **Write (Luna, xhigh).** Follow the blueprint. Text and figures in the same pass. Standards: Writing Standard, Visual Genres, Design Direction, the lesson-size mandate (one sitting, ~2.5–4.5k words). Branch `codex/<course>-<lesson>`, one PR per lesson, don't merge.
4. **Report in the PR:** words before and after, figures replaced or added, `requests.md` summary, doubts.

Gate (finished page): Claude reads the page in the browser (light and dark, 390 px), not the diff. The reference to match is the lesson Claude rebuilds by hand (Controle Aula 01).

## Models (as of 30/09; GPT-6 launch numbers)

Sol costs about 20× Luna per token. At max effort Luna comes close to Sol on agentic work (DeepSWE 66.6 vs 68.8; Agents' Last Exam 50.9 vs 56.4) at 1/12–1/20 of the cost per task. Its weak spot is factual error rate: 7.6% at max vs Sol's 4.5% at xhigh. So:
- **Sol only for S0 and the S5a panel** (small inputs, upstream of everything, and errors there compound);
- **Luna for everything else**: high for mechanical stages, xhigh for triage and writing, max for blueprints;
- factual risk is handled by the pipeline, not by the model: writers work from the compendium with page markers, and Claude's gate spot-checks claims against the cited pages.
Revisit if the pilot shows Luna missing things Sol would catch.

## Pilot

Controle de Constitucionalidade: S0–S4 for the whole course, then S5 on Aula 30 (ADC, which now has the professor's deck). Claude rebuilds Aula 01 from the same compendium as the reference. If the pilot beats the live pages, run the remaining Controle lessons in batches of ≤6, then Contratos (after its base books are downloaded), then the rest.
