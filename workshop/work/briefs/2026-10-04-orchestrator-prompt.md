# RESUME HERE (CEO, 05/10 evening): read this section first, then the plan below

Codex ran out of credits on 05/10. The CEO (Claude) carried the work in the meantime. **Everything below this section is still the plan, but these facts override it where they conflict.**

## Already done: don't redo, don't overwrite
- **Closed out (merged):** site #47 CHG-1, #52/#53/#54 Controle 02/04/05, #58 Processo A01, #59 Controle A08, #67 REG-H1; workshop #36 BRK-1. Issues #11, #16, #18 are closed.
- **LAT-1 data stages S0–S4: done** (workshop #39–#56). The split chapter texts are git-ignored, and the CEO gathered all 950 into the main checkout's `work/pipeline/direito-latino-americano/chapters/`. Rebuild compendia with `python3 work/pipeline/tools/build_compendia.py --site <site checkout> direito-latino-americano`.
- **LAT-1 Aula 05 (Gelman): rebuilt and merged by the CEO** (site #70). It is the **reference page for every other Latam writer**: read it and its ISSUES.md line. No blueprint file was written for it; the scripts are `work/latam-rebuild/a05_*.py`.
- **Latam course front: rebuilt** (site #71, "Quem respondeu a quem"; generator `work/latam-build/front_courts.py`, frame `geo/frame_courts.json`). Don't regenerate it from `index_gen.py`.
- **Latam figure pass (site #72–#74), CEO-built.** All figures in the table below are **canonical**. Writers keep them as they are. A writer may add new figures but may not redraw these without a written reason in the PR.

| Page | Canonical CEO figures |
|---|---|
| A01 | Fig. 2 field (`p-pj*`) |
| A03 | Fig. 1 "conexos" (`p-rd*`) |
| A04 | Fig. 1 marked-up sheets (`p-dc*`) |
| A05 | Figs. 1 (`p-gr*`) and 2 (`p-am*`) |
| A06 | Fig. 1 (`p-us*`) |
| A07 | Fig. 1 lanes (`p-rm*`) |
| A08 | Figs. 1 (`p-ck*`), 2 (`p-tr*`) and the hero |

- **Latam phone pass (site #73).**
  - The inline 19 px figure rule and the `latam-wide` full-bleed hack are gone.
  - Legacy figure labels have a paper halo.
  - Every `table.compare` stacks into cards on upright phones (cells carry `data-label` / `data-tone`).
  - Breakscan, whole course: **1280: 0 findings; 375: 25**. All 25 are haloed map labels over coastlines on four legacy maps; that's accepted.
  - New Latam figures must keep those numbers: 0 new findings at either width.

## Figure conventions for any new Latam figure (learned today, binding)
- Use `work/latam-rebuild/fk.py`: panels are `.figkit.lt`; upright phones set text to 18 px (mono) and 21 px (hand).
  - Design every label to fit at that size: ≤ 28 mono characters per line from x≈40 in a 600-wide box.
  - Line spacing ≥ 28 px for stacked mono lines and ≥ 30 px for hand lines.
  - Titles ≤ 30 characters.
- Maps use the course frame: `Frame('courts')` from `work/latam-build/maps.py`, with defs injected once per page as a hidden SVG (see `a06_fig.py`).
- Run breakscan at **both** widths on every changed page (`node work/checks/breakscan.mjs <root-with-touched-pages> out.csv --width 1280 --width 375 --base-url ...`).
- Look at every panel yourself, but only through a worker that returns crops.

## What's left, in order (wide, not long: same operating rules as below)
1. **LAT-1 · the other nine pages.** Blueprint (Sol) → panel (Sol) → write (Luna xhigh) → checks → merge, for Aulas 03, 04, 06, 07, 08, 09, 02, 01 and the revisão.
   - Build on the live pages, which now include the canonical figures.
   - Model the text on Aula 05: each fact once; cases with court · year · holding · reasoning · dissent · what came next; the closing test ends with an eixo question.
   - The revisão becomes the eixo workbench (§5.6 below).
   - Then cards + front register + RETRO.md (§5.9). The front drawing itself is done.
2. **Site #69 PHN-1: rebase on main first.** It touches every Latam page and `curso.css`, so it conflicts with #71–#74.
   - **On every Latam file, main wins.** Keep the CEO's phone pass as is.
   - Apply PHN-1 only where it adds something main lacks, such as heroes shown on upright phones. If PHN-1 re-adds forced font sizes, a full-bleed figure rule, or phone-variant drawings on Latam, that part is dropped.
   - Merge after breakscan at 375 shows no new findings on Latam.
3. **Site #68 BIO-2, #65 Contratos A01, #51 Delito U01.** Finish each per its latest verdict comment, rebase, check, merge.
4. **Site #55, #60 (Controle A07, A09), workshop #5 PIPE-5 (Aula 30).** Revise per the W2 verdict and the #59 lessons, then merge.
5. **#17 CAST-1, #10 FIG-2, #12 PIPE-C, #13/#15 Controle waves:** proceed on spare slots, lowest priority.
6. **Housekeeping:** create the `RUN-0410.md` ledger (§3.1). It was never written, and a fresh orchestrator needs it to resume.

---

# Master plan, 04/10: close out everything open, rebuild Direito Latino-americano

**For: the orchestrator (Codex app, Luna high, fresh window).** Written by Claude (CEO) on the chairman's direction. Read every word before dispatching anything. You'll be running this for many hours with many workers, and every decision you'll need is either in here or in a file this points to. Where this plan and an older document disagree, **this plan wins for this run** (§9 lists the known conflicts and how they're resolved).

---

## 0. The situation in one minute

- **Who's who.** Benecles is the chairman: he set today's direction. Claude is the CEO: it wrote this plan and the GitHub issues it points to, and it reviews the result *after* you ship. **You** are the orchestrator: you own the HOW. You split work into units, write complete briefs, dispatch workers, check that each unit actually got done, merge, and keep the line full. You don't do unit work yourself.
- **Two streams run at once, from the first minute:**
  - **Stream A, the priority:** rebuild the Direito Latino-americano course (workshop issue **#25, LAT-1**) on the full Source Pipeline, plus the breakscan fix (**#23, BRK-1**) that every figure check depends on.
  - **Stream B:** close out every open thread of prior work (site PRs and workshop issues, §6).
- **Chairman overrides for this run (04/10):**
  1. **No gates.** Never add `needs-gate` and wait. Never STOP for the CEO. Where an issue says "STOP", "write only the prototype", "blocked until #59 passes" or "paused (F-023)", ignore that wait and keep going. Your own checks are the bar (§5.8). When a PR passes them, **you merge it** through the merge queue (§7). The CEO reads the live result afterwards and files fix-up issues.
  2. **Wide, not long.** Use all 16 worker slots, all the time, until the work runs out. Never let a stream crawl along on one or two long-lived workers.
  3. **Pipeline, not waves.** Each unit moves to its next stage the moment its own inputs exist. No stage waits for the whole previous stage (§4).
  4. **Build on what exists.** The Latam rebuild improves the live pages; it never restarts from blank. Keep by default; every cut is named with a reason (§5.7).
- **Why Latam, why now:** the chairman has an in-class group activity on **05/10** covering the 17/08–28/09 classes (site Aulas 02–09). He doesn't want cramming notes. He wants the course genuinely done well: depth, volume, accuracy, state-of-the-art visuals, every house rule applied. Latam is also the house's best course today (its atlas plates are the figure bar), so it becomes **the first course built end to end by the pipeline, and the reference for every other course**.

---

## 1. Definition of done (the whole run)

**Stream A**
- BRK-1 merged in the workshop: breakscan measures after webfonts load, at 1280 and 375, in every panel step, with CLIP and OVERFLOW findings. It provably FAILS on the known-bad cases listed in #23.
- `work/pipeline/direito-latino-americano/` holds S0–S4 artifacts that pass `pipeline_check.py s0…s4 direito-latino-americano`.
- Ten pages rebuilt and **merged to `main`** on the site: `courses/direito-latino-americano/aula-01.html` … `aula-09.html` and `revisao-atividade.html`. Each has a Sol-APPROVED blueprint in `compendium/<lesson>/blueprint.md`.
- `cartoes.html` and the course front's class register regenerated from the rebuilt lessons.
- `work/pipeline/direito-latino-americano/RETRO.md` (≤1 page): what the pipeline had to bend for a case-based course, so Direito Constitucional I (same professor) can reuse it.

**Stream B**
- Every item in §6 either merged, or closed with a one-line reason on its issue.

**Always**
- One `ISSUES.md` line + one patch-note line per merge.
- One status comment on the relevant issue per finished unit.
- A final summary comment on #25 and on a new workshop issue titled `RUN-0410 · run report` (§10).

---

## 2. What you read, and what each worker reads

### 2.1 You, before dispatching anything (in full)
1. `~/Developer/ordenacoes-filipinas-workshop/CEO.md`: the mandate, state and gotchas. The gotchas are paid-for lessons; every one applies.
2. `FLIGHT-LOG.md` (F-001…F-027): every row is a rule. Tags tell you which stage it binds.
3. `BUGS.md`: the bug catalogue, by symptom. Workers search it before debugging.
4. `protocols/CUFRGS Source Pipeline.md`: the stages. This plan adapts it for Latam (§5).
5. `protocols/templates/Lesson Blueprint.md`, the reference blueprint `work/pipeline/controle-de-constitucionalidade/compendium/aula-01/blueprint.md` (read its Method notes), and the live reference page `~/Developer/ordenacoes-filipinas/courses/controle-de-constitucionalidade/aula-01.html` with its `REF ·` comments.
6. Skim for orientation (workers read them in full): `protocols/CUFRGS Writing Standard.md`, `CUFRGS Visual Casting.md`, `CUFRGS Visual Genres.md`, `CUFRGS Figure Library.md`, `CUFRGS Design Direction.md`.
7. `~/.codex/AGENTS.md` (your standing rules), and "Build-process lessons" in `Relay Baton.md`.
8. Every issue in §5–§6, **with all comments**. The newest CEO comment on an issue is its current verdict.

### 2.2 Each worker reads only what its role needs
Put the exact list in each brief. Don't tell workers to "read everything": that's how quota burns and attention blurs.

| Role | Must read in full | Skim |
|---|---|---|
| S0 course map (Sol) | Source Pipeline §S0; the Latam dossier Parts 0–3 (path in §5.1); the Moodle scrape index; deck titles | — |
| S1 shelf / S2 split (Luna high) | Source Pipeline §S1–S2; §5.2–5.3 of this plan; `work/latam-prep/L-status.md` and `sources-public/primary-gap-status.md` + inventories | — |
| S3 triage, per lesson (Luna xhigh) | Source Pipeline §S3; F-001, F-002; `course-map.md`; the chapter indexes | — |
| Blueprint (Sol) | Lesson Blueprint template; reference blueprint + Method notes; reference page + REF comments; Writing Standard; Visual Casting; Visual Genres; FLIGHT-LOG F-019…F-027; LAT-1 (#25) with comments; its own compendium `00-index.md` and files; its live page | Figure Library, Design Direction |
| Panel (Sol) | Source Pipeline §S5a rubric + the Latam test (§5.6); the blueprint; `course-map.md`; the compendium index; the lesson's exam/eixo questions. **Never the full sources.** | — |
| Writer (Luna xhigh) | Its APPROVED blueprint; its compendium (primary files in full); its live page; Writing Standard; Visual Casting; Visual Genres; Figure Library; Design Direction; FLIGHT-LOG (all); BUGS.md (search on demand); PHN-1 (#24) | reference page |
| Stream B worker | Its issue + all comments; the PR + all review comments; the FLIGHT-LOG rows the verdict names; CEO.md gotchas on site edits | — |

---

## 3. Operating model

### 3.1 Your memory is a file, not your context
Your context is the run's most expensive object: every call re-reads it. Keep it small, and make the run restartable.
- Create **`work/pipeline/direito-latino-americano/RUN-0410.md`** (committed and pushed after every dispatch round) with one row per unit:
  `unit id · stream · stage · state (queued / running / done / failed / merged) · worker model · output path · done-check result · notes (≤12 words)`.
- If your context grows large (past ~120k tokens), write the ledger, commit, and tell the chairman in one line: *"Context is large: open a fresh window with the same paste prompt; it will resume from RUN-0410.md."* A fresh orchestrator must be able to read this plan + the ledger and continue with no loss. Design every step for that.
- Also keep your registry file `/Users/benecles/Documents/agents/Luna<N>.md` (per AGENTS.md) up to date at each phase change, pointing to the ledger.

### 3.2 The dispatch loop
1. **Dispatch** every unit whose inputs exist, up to 16 running. Priority when slots are scarce: LAT-1 critical path (S0, then whichever lesson is furthest along) > BRK-1 > the merge queue > Stream B small fixes > Stream B larger work > LAT-1 non-critical units.
2. **Wait once** for the next completion(s). No polling loops of `list_agents` / `wait_agent`; one long wait.
3. On each completion, run the unit's **done-check mechanically** (the file exists, the script passes, the PR exists with the required body sections). Workers sometimes answer "done" without doing the work; the check catches that cheaply. On a pass, mark it done and dispatch whatever it unblocked. On a fail, re-dispatch **once** with the failure quoted. After a second failure, mark it `failed`, note why, and route around it (§3.6).
4. Update the ledger, commit it, repeat.

### 3.3 Worker briefs: complete, so no follow-ups are needed
Every brief contains:
- **Goal**, in one paragraph: what this unit is for in the whole plan (workers do better when they know why).
- **Inputs:** absolute paths. **Outputs:** exact paths, and the branch name if it's a PR.
- **Reading list** (§2.2) and the FLIGHT-LOG rows that bind this stage, quoted.
- **Done-condition:** the exact command(s) that must pass, and what the PR body must contain.
- **Reply format:** at most 5 lines (what was done, paths, check results, one doubt if any). Never paste work product back.
- The **BUILD, DON'T AUDIT** paragraph from AGENTS.md, verbatim, followed by this sentence: *"The Source Pipeline's S5a panel is a pipeline stage, not an audit; it runs."*
- Spawn with **`fork_turns:"none"`** and the **explicit model + effort** from §3.4.

### 3.4 Models
| Unit | Model | Why |
|---|---|---|
| S0 course map | **Sol, high** | upstream of everything; errors compound |
| S1 shelf, S2 split, S4 workbench | Luna, high | mechanical / scripted |
| S3 triage (per lesson) | Luna, xhigh | precision decides quality |
| **S5 blueprint (per page)** | **Sol, high** | No gates: the blueprint is the last real judgment. Long Spanish decisions; only ten of them |
| S5a panel (per page) | Sol, high | small input, sharp judgment |
| S5 writer (per page, text + figures) | Luna, xhigh | volume; follows an approved blueprint |
| BRK-1, PHN-1, REG-H1, BIO-2 | Luna, xhigh | engineering with judgment |
| Stream B fix-ups (#58, #47, #59, #65, #51) | Luna, xhigh | finishing a known verdict |
| Merge queue | Luna, high | procedural |

### 3.5 Parallelism, serial points, diminishing returns
- **Up to 16 workers at all times.** If the runtime refuses that many, use what it allows and note it in the ledger.
- **Disjoint ownership:** two workers never write the same file. Each lesson unit owns its `compendium/<lesson>/` and its page; each Stream B unit owns its branch.
- **The only deliberate serial points:**
  1. **One merge queue** (§7): parallel merges collide in the offline manifest and generated fronts.
  2. **One writer per page:** a page's text and its figures need one mind. Never split a page across writers.
  3. **Cards, front register and course-level regeneration run once,** after the last lesson merges (and again only if a later fix touches cases).
- **Diminishing returns:** don't cut units below ~15 minutes of work; overhead beats the gain. Don't parallelise anything that needs one author's judgment (one blueprint = one author). Don't spawn reviewers of reviewers.
- AGENTS.md says "chunks of ≤ 6 units". That rule exists because big orders failed partway. Under per-unit pipelining every unit is its own chunk with its own check, which satisfies it. Ten lesson units in flight is fine.

### 3.6 When things go wrong
- **A source can't be fetched:** mark it `missing` in the shelf with the URL and the error, and move on. Never substitute an unofficial copy or model memory. The lesson is written from what exists, and the blueprint's A9 names the gap.
- **A panel says REVISE:** that page's blueprint author revises (same Sol model, fresh worker, given the panel's numbered points and the old blueprint). A second REVISE: you read the two panel verdicts and decide the 1–3 decisive changes yourself (architect-level judgment, allowed), then dispatch one final revision. A third panel isn't needed. Note it in the ledger.
- **A check fails on a PR:** re-dispatch the writer once with the failure output. If it fails again, hold that PR out of the queue, mark `failed`, and keep everything else moving. Never weaken a check to make a PR pass.
- **The shared workshop checkout is on a `codex/*` branch** (it happens): run `git status -sb` before every commit, and work in worktrees.

---

## 4. The pipeline graph (what can start when)

```
BRK-1 ───────────────────────────────────────────────► merge (early: every later figure check uses it)

S0 course map (Sol) ─┐
S1 shelf ─► S2 split per source ─┼─► S3 triage per lesson ─► S4 workbench per lesson ─► blueprint (Sol) ─► panel (Sol) ─► writer ─► checks ─► merge queue
                                 │      (needs S0 + the sources that lesson names)                       ▲ REVISE loops back here, this lesson only
                                 └─ late sources append verdicts, never redo triage

after the last lesson merges: cards + front register + RETRO.md
Stream B: every item independent, from minute one
```
- **S1 and S2 don't wait for S0.** Sources are the same whatever the map says.
- **S3 for a lesson** starts once S0 is done *and* the sources named in that lesson's syllabus line are split. Other sources join later as appended verdicts.
- **S4 is a script:** seconds per lesson. Run it the moment a lesson's triage is in.
- **Each lesson then runs its own chain to merge.** Aula 05 can be merging while Aula 09 is still in triage.
- **Order of preference** where it matters: **Aula 05 (Gelman) first** at every stage. It's the richest case and the most central to the activity, and its merged page becomes an extra example for later writers (point later writer briefs at it once it's live). Then 03, 04, 06, 07, 08, 09, 02, 01, revisão. The revisão writer starts last, because it draws on all the others' blueprints.

---

## 5. Stream A: LAT-1 in detail (workshop #25; read it and its comments in full)

### 5.1 Sources and places
- **Course material (the chairman's; read, never reorganise):** `~/Documents/UFRGS 2026-2/Direito Latino Americano/`: decisions (PDF/RTF), statutes, articles, the professor's slide decks, `Moodle/` scrapes, and the **dossier** `Direito Latino-americano - Dossie atividade 05-10 para IA.pdf`. Part 0 maps every case. Part 1 is the full programa, with each class's *eixo de discussão*. Part 3 is the 10/08 class transcript. The dossier's case map is a lead, not a source: writers verify against the decision text.
- **September prep (reuse first):** `~/Developer/ordenacoes-filipinas-workshop/work/latam-prep/`: `digests/` (12 decisions; provisional leads, not citable sources); `text/ocr/adpf153-run-20250925/` (ADPF 153 OCR of selected ranges: don't rerun); `sources-public/` (official copies of Gomes Lund (EN), the 2013 Gelman supervision resolution, T-025/04, Autos 176/05 and 008/09, the Tema 1234 recheck, and `inventory*.csv` with official URLs); `L-status.md` (the September review's corrections, which must not regress); `drafts/` (earlier drafts of 08, 09 and the revisão).
- **Old generators (reference only):** `work/latam-build/a01.py … a09.py`, `maps.py`, `geo/`. Their output path is dead, and the live pages were hand-fixed after generation (FIG-1, label crossings). **The live HTML on site `main` is canonical. Never regenerate a page from these scripts.** Mine them, and their `*.pre-*` versions, for content the live pages lost. Reuse `maps.py` / `geo/` as the map toolkit (Design Direction §5).
- **Pipeline home:** `work/pipeline/direito-latino-americano/` (create it), mirroring the Controle layout. Book and decision text stays git-ignored (`text/`, `chapters/`, `compendium/**/*.txt`); maps, indexes, blueprints, panels, logs and the ledger are committed.

### 5.2 S0, course map (1 unit, Sol high)
- Output: `course-map.json` + `course-map.md`. Done-check: `pipeline_check.py s0 direito-latino-americano`.
- Lesson ids are the live hrefs: `aula-01.html` … `aula-09.html`, `revisao-atividade.html`. Map each to its class date(s) and syllabus line. The 31/08 class feeds both 05 (Gelman / Uruguay) and 06 (Bolivia / OC-28); the 24/08 class feeds both 03 (Brazil) and 04 (Colombia). Aula 01 draws on the 10/08 presentation and the "história constitucional na AL" deck.
- **Each lesson's eixo de discussão goes in verbatim.** It is the lesson's function: the reader must leave able to answer it with cases.
- The 26/10+ topics go in as `scheduled` rows with no page (they haven't been taught; no pages are built for them).
- Prerequisites: e.g. 05 depends on 03 (amnesty, conventionality); 08 depends on 07 (ECI); 09 depends on 08 (structural remedies, dialogue).
- Bibliography: as the programa lists it (Engelmann & Bandeira; the cases per class).

### 5.3 S1 shelf + S2 split (1 + ~6–8 units, Luna high)
- **S1 (1 unit):** `shelf.csv`, one row per source (decision, statute, article, deck, transcript, Moodle item), with role, path, sha256, format and text status. Reuse every `latam-prep` copy and record that it was reused. **One honest retry from official sources only** for the known gaps: STA 175 inteiro teor, RE 566.471 acórdão (Tema 6, merits 20/09/2024), the ADPF 347 2015 cautelar, and a check that the local OC-28/21 is complete. Anything still unavailable is `missing`, with the URL and the error. No third-party rehosts. Scans get local OCR only (Tesseract); never cloud vision.
- **S2 (split sources across ~6–8 workers, ~4 sources each, starting as soon as each is on the shelf):** Latam has no textbooks, so the unit is **the decision's own structure**: antecedentes/hechos · problema jurídico · consideraciones (by the decision's numbered ¶, keeping the ¶ numbers) · resuelve/dispositivo · each voto/salvamento/aclaración separately. Statutes split by article. Articles (Engelmann & Bandeira, Gargarella, Kosicki & Van der Broocke, Ariza & Iturralde) split by their own sections. Decks: one file each, with slide markers. Every file carries `===== p. N (PDF M) =====` page markers, plus ¶ markers where the source numbers its paragraphs. Write `chapters/<source-id>/index.json`.
- Done-check: `pipeline_check.py s1` / `s2 direito-latino-americano`. If the checker assumes book chapters and rejects decision sections, **extend the checker** (keep the continuity and no-overlap logic) rather than bending the data, and show it failing on a planted gap first.

### 5.4 S3 triage (one unit per lesson, Luna xhigh)
- Each lesson's worker reads the S0 line + eixo and the chapter indexes, and writes `triage/<lesson>.csv` (`source_id, chapter_id, lesson_id, role, why`) with precise ¶ ranges. **Precision is the point:** Gelman §§ around 238–239 and the operative points go to 05; the 2013 supervision considerandos go to 05; ADPF 347 sections go to 07 and others to 08. A triage that hands a lesson a whole decision "because it's relevant" has failed (F-001, F-002: statutes by article only; supporting material ≤ 10k words per item).
- **Background closure:** a lesson also receives its prerequisites' `primary` chapters as `background`.
- A tiny final step (script) merges the per-lesson files into `triage.csv` and adds `unused` (with a reason) for every chapter no lesson claimed. Done-check: `pipeline_check.py s3`.

### 5.5 S4 workbench (script, per lesson)
- `build_compendia.py` (in `work/pipeline/tools/`) assembles `compendium/<lesson>/` (`10-slides`, `20-primary-*`, `30-supporting-*`, `40-background-*`, `50-exercises-and-exams`, `00-index.md` provenance). Add a **`05-eixo.md`**: the eixo verbatim, plus the dossier's instruction on how answers are judged (court, year, holding, why, dissent, how it answers the eixo). Add a **`60-live-page.txt`**: the current live page's visible text, so the blueprint and writer see exactly what exists. Done-check: `pipeline_check.py s4`. Later material: `pull_source.py`, logged in `requests.md`.

### 5.6 S5 blueprint → panel (per page; Sol / Sol)
- **Blueprint (Sol high):** fill every field of the Lesson Blueprint template, modelled on the reference blueprint's Method notes. Latam specifics:
  - **A0:** the live page counts as an input. Inventory what it has that's worth keeping.
  - **A1:** the reader brief's "can do after reading" includes answering this lesson's eixo with cases.
  - **A2 traps:** Latam's signature trap is **confusing a Corte IDH holding with a national court's**, or an advisory opinion with a judgment. Place it once, test it once (F-021).
  - **A4 claim inventory:** every case appears with **court · year · what was decided · why · who dissented and how** · what happened next. Every claim has a locator (¶ or page) in the compendium.
  - **A5 thread:** a real one (F-022). In Latam the thread is usually the lesson's central case, followed through time.
  - **A7 figures, cast from Latam's world:** real geography and real chronology: the atlas plate, borders by date, regimes on a timeline, courts as tallies, vote records, dockets, calendars, the ruling's own text. Never boxes and arrows (F-026: text in ruled cells is a table). The issue gives per-lesson casting hints; the blueprint chooses, and records ≥3 candidates and its rejections.
  - **A8 cut list, per §5.7.**
  - **Closing exercises:** at least one is the eixo (or an eixo-shaped question) that the reader answers with the lesson's cases.
- **Revisão blueprint:** an **eixo workbench**. For each class: its eixo, the cases that answer it, and an answer frame (tese → casos → divergência → posição). Plus at least one cross-cutting question that forces two lessons together (e.g. Gelman's majority × ADPF 153's amnesty × C-579's selection). It's a working page, not a summary of summaries.
- **Panel (Sol high):** the Source Pipeline's seven-point rubric, **plus the Latam test:** *does every case appear with court, year, holding, reasoning and dissent; does the closing exercise ask an eixo question the reader answers with cases; is every Corte IDH / national / advisory distinction right?* Output: `compendium/<lesson>/panel.md`, either **APPROVED** or **REVISE** with ≤ 5 numbered points. REVISE handling is in §3.6.

### 5.7 S5 writer (per page, Luna xhigh: text and figures together, one agent)
- **Branch** `codex/latam-<lesson>` from fresh site `main`; one PR per page: `LAT-1 · Aula NN: <title>` with "Part of Benecles/ordenacoes-filipinas-workshop#25".
- **Edit the live page; never start blank.** Keep by default. Every case analysis, figure, callout, exercise or well-made explanation stays unless the blueprint's A8 names something better. The atlas plates and figures that already meet the bar stay (recast only when Visual Casting gives a stronger instrument). **Words after ≥ words before**, unless A8 justifies the cut. The PR body lists every cut and its reason.
- Read the primary compendium files in full. Pull missing back-references with `pull_source.py` and log them in `requests.md`.
- **Standards that bite hardest** (all of FLIGHT-LOG applies):
  - **F-019 / F-020:** no backstage on the page. Never "a professora", "os slides", "o dossiê", "o material", "nesta aula veremos"; no visible source parentheticals; the scope fence never appears on the page. Sources live only in hidden `data-src`.
  - **F-021:** each trap is said once, tested once.
  - **F-022:** carriers are real.
  - **F-025 / F-026:** a figure is an instrument and never restates the adjacent paragraph; text in ruled cells is a table, not a figure.
  - **F-027:** PR body crops of every new or changed figure panel (every step), at 1512 and 390.
  - Kit rules F-004…F-017 for every figure: kit-built, viewBox cropped to the drawing, labels ≥ 11 px at 600 px, no negative-space corners.
- **Language:** the page is Portuguese. Quote Spanish decision text only where the exact words are the point (Gelman § 239, a C-579 holding), with a Portuguese rendering beside it.
- **Facts that must not regress** (corrected in September; see `L-status.md`):
  - Art. 5º, XLIII names torture, drug trafficking, terrorism and crimes legally defined as hediondos. Calling homicide and rape hediondos comes from statute; that was Ayres Britto's reading, not the Constitution's classification.
  - C-579/13 allows conditional renunciation of prosecution for non-selected cases while keeping prosecution of the gravest crimes and the most responsible.
  - C-694/15 upheld only what its disposition names.
  - The TCP's SCP 0084/2017 displaced the term limits despite the 2016 referendum. It did not formally annul the referendum.
  - OC-28/21 is a later advisory opinion, not an appeal or reversal.
  - Sentencia 65/2014 (SCJ Uruguay) does not mention Gelman: never present it as part of the Gelman case.
  - STF and Corte IDH holdings applied different legal frameworks; don't make them sound interchangeable.
- **Size:** one sitting, ~2.5–4.5k words. Volume means depth on the cases (the reasoning, the dissent, what happened next), not padding. The hero's "Leitura" matches the front clock (F-013).
- **Phones:** follow PHN-1 (#24): upright = the same drawings in one column; sideways = desktop; no phone-variant drawings. No horizontal overflow at 375 (this also fixes TBL-1's Latam 08/09 overflow).
- **Site-edit procedure** (CEO.md gotchas, in this order): after injecting figures run `tools/offline_build.py`, then `git checkout -- assets/front.css specimen/register.html`, then `tools/polish.py capture` and `rm -rf tools/polish/specimen`, then `git add`, then `tools/check_all.sh`. (check_all compares against the git INDEX: `git add` first.)

### 5.8 Checks a Latam PR must pass before it enters the merge queue
`tools/check_all.sh` PASS · `slop_lint` 0 hard hits (run from the workshop) · `anatomy_check` PASS · **breakscan (BRK-1 version) 0 findings at 1280 and 375** for that page. Until BRK-1 merges, use the old breakscan *and* say in the PR body that BRK-1 hasn't run; re-run it once BRK-1 lands, before merging. Also: word count before/after in the PR body, the cut list, crops of every figure panel, `requests.md` summary, doubts.

### 5.9 Course-level finish (after the last Latam page merges; 1–2 units)
- **`cartoes.html`:** one card per case (court · year · holding · why · dissent · which eixo it answers), generated from one case-data file that the lessons' facts also come from, so cards and lessons can't disagree.
- **Course front:** the class register shows the rebuilt lessons with their real reading times. The 26/10+ topics appear as scheduled rows without links. Keep the atlas identity of the front.
- **`RETRO.md`.** Then the final comment on #25.

---

## 6. Stream B: close out prior work (each item its own unit, from minute one)

Each item: read the issue/PR **and all comments**; the newest CEO comment is the verdict. Rebase on current `main` (merge `origin/main` in; for an offline-manifest conflict, take main's side and rerun `offline_build.py`). Apply exactly the verdict. Run the §5.8 checks. Enter the merge queue.

| # | Item | What closes it |
|---|---|---|
| B1 | **BRK-1, workshop #23** (Stream A priority, listed here for completeness) | As the issue says. Must FAIL on #65 as it stands, Latam 08/09 at 375, and #58's two edge labels, then PASS on live Controle Aula 01. Merge in the workshop. |
| B2 | **Site #59, Controle Aula 08** | Apply the cut list in the 03/10 CEO comment: the F-021 repetition (the "modulation ≠ anulabilidade" trap, said ~8 times, goes down to once + once tested), cut the 3 off-lesson paragraphs, add why 11 vereadores was unconstitutional *if the sources say* (otherwise leave it out). Rebase (it conflicts). Merge. |
| B3 | **Site #52, #53, #54, #55, #60** (Controle W2/W3: Aulas 02, 04, 05, 07, 09) + **workshop #5 PIPE-5** (Aula 30 ADC, blueprint approved) | No longer wait on #59. Apply the 01/10 REVISE comment (F-019…F-022) and the #59 cut list's lessons (F-021). Rebase. Merge each. For PIPE-5: write Aula 30 from its approved blueprint. One worker per page. |
| B4 | **Site #58, Processo A01 figure** | Fix the two labels clipping at the viewBox edge; rebase. Merge. |
| B5 | **Site #47, CHG-1 bento** (closes workshop #11) | Fill the holes at the end of the grid; drop the "0 rótulos cortados" QA tile; scale the "Um contrato de verdade" miniature. Merge; close #11. |
| B6 | **Site #65, Contratos A01 figures** | The 03/10 REVISE: fix the 6 broken panels; recast p-est (F-026); merge p-sub + p-esp into one "roupagem" drawing; keep p-lad, p-nor, p-dest, p-teo, p-cas once fixed. Must pass BRK-1. Merge. |
| B7 | **Site #51, Delito U01** | Restore the one-fact-two-norms fork with the art. 13 § 2º duty contrast (F-025). Rebase. Merge. |
| B8 | **PHN-1, workshop #24** | As the issue says. Merge. |
| B9 | **REG-H1, workshop #18** (register hover) and **BIO-2, workshop #22** (professor card; also normalises the BIO-1 bios into one voice) | As each issue says. One worker each. Merge. |
| B10 | **CAST-1 #17, FIG-2 #10** | Continue recasting/rebuilding per the verdicts on those issues (the 395-row DOM count is authoritative). Cut into per-lesson units; ≤ 3 workers on this at a time so it doesn't starve Latam. |
| B11 | **PIPE-C #12, PIPE-W2 #13, PIPE-W3 #15** (Contratos and Controle pipelines) | No gates now: proceed to the next stage each issue describes (Contratos S5 blueprints → panel → writing; Controle A10–A13 writing from the merged blueprints). **Lowest priority:** only on slots Latam and B1–B9 aren't using. |
| B12 | Housekeeping | Close **#16 BIO-1** (data merged in site #66; superseded by #22). Close **#14 TBL-1**: five courses checked clean; Latam 08/09 overflow is fixed inside LAT-1 and caught by BRK-1. |

---

## 7. The merge queue (one worker at a time, Luna high)

For each PR that passed its checks, in arrival order (Latam pages and BRK-1 jump the queue):
1. Fresh worktree on the PR branch; `git merge origin/main`. On a conflict in the offline manifest or generated fronts, take main's side and rebuild (`tools/offline_build.py`, then the §5.7 procedure). On a conflict in `specimen/figuras.html`, `tools/figkit/inject.py` or `tools/figkit/specimen.py`, keep **both** entries; never drop another PR's work.
2. Add one line to `ISSUES.md` (site repo) and one patch-note line.
3. Run `tools/check_all.sh` (after `git add`). Run breakscan for the touched pages.
4. Push to the PR branch, `gh pr merge --merge`. Comment one line on the issue.
5. **Word-count guard:** if a lesson's visible words drop on merge versus the PR's own count, stop that merge and investigate. It means content got lost (AGENTS.md lesson).
Never force-push `main`. Never merge with a failing check.

---

## 8. Never

- Never wait on the CEO; never add `needs-gate` and stop (this run).
- Never write from model memory or unofficial copies of decisions; never cloud-vision a scan.
- Never regenerate Latam pages from `work/latam-build/`; never let any regeneration revert live edits (the polish layer exists for this).
- Never put backstage text on a reader page (F-019/F-020).
- Never build phone-variant drawings (F-009, PHN-1).
- Never take full-page screenshots: selector crops only, under `/private/tmp`. Never use computer use for bulk checks; checks are scripts.
- Never fork your history into a worker; never do unit work in your own context; never paste worker output back into your context.
- Never install daemons, LaunchAgents, cron jobs or watcher loops.
- Never `pkill -f` (it kills its own shell); kill by pid.
- Never put anything on the Desktop (it holds only the chairman's Felipe and Mark folders).
- zsh: brace variables before a colon (`"${n}:courses/..."`, not `"$n:courses"`); `:c` is a modifier and silently breaks pushes.

---

## 9. Conflicts with older documents, resolved for this run

| Older text | This run |
|---|---|
| AGENTS.md / Source Pipeline: "add `needs-gate`, STOP; never merge" | No gates; you merge through the queue after checks (§0, §7). |
| AGENTS.md: "build, don't audit: no reviewers" | Still true. The S5a panel is a pipeline stage, not an audit, so it runs. Nothing else reviews. |
| AGENTS.md: "spawn the whole batch, then one long wait" | Still true per dispatch round. Pipelining means you dispatch again after each wake-up, not after a whole stage. |
| AGENTS.md: "chunks of ≤ 6 units" | Satisfied by per-unit pipelining (§3.5). |
| Source Pipeline: Luna max for blueprints | Sol high for Latam blueprints (§3.4). |
| F-023: "S5 writing paused until Aula 08 passes" | Lifted by the chairman for this run. Aula 05 goes first so its result informs later writers, but nothing waits. |
| Design Direction §2/§5: "a wide figure needs a vertical phone version"; `phone_svg` | Superseded by F-009 and PHN-1: one drawing for every screen; upright phones re-lay out. |
| Issues saying "blocked until #59" | Unblocked (§6, B3). |

---

## 10. Reporting

- **Per unit:** one line on its issue when done (what, link, checks).
- **Per dispatch round:** update `RUN-0410.md` (commit + push), including how many workers are running.
- **Every ~2 hours, or at a big milestone** (BRK-1 merged; Latam S0–S4 done; first Latam page merged; all Latam merged): a 3–5 line comment on #25 the chairman can read on his phone, with the full live URL of each newly merged page (`https://benecles.github.io/ordenacoes-filipinas/courses/direito-latino-americano/aula-05.html`, etc.).
- **End of run:** a new workshop issue `RUN-0410 · run report`: what merged (links), what failed and why, what's left, the gaps marked `missing`, and anything you'd change in this plan. Delete your registry file.

---

## 11. Your first hour, concretely

1. `git -C ~/Developer/ordenacoes-filipinas-workshop pull` and `git -C ~/Developer/ordenacoes-filipinas pull`. Read §2.1. Create the registry file and `RUN-0410.md` with every unit from §5–§6 as `queued`.
2. **Dispatch at once** (≈ 14–16 workers):
   - S0 (Sol)
   - S1 shelf
   - BRK-1
   - B2 #59
   - B4 #58
   - B5 #47
   - B6 #65
   - B7 #51
   - B8 PHN-1
   - B9 REG-H1
   - B9 BIO-2
   - B3: three of the six Controle pages
   - B12 housekeeping: do it yourself; it's two `gh issue close` commands.
3. As S1 lands, fan S2 out across ~6–8 workers, taking slots from the B3/B10/B11 pool if needed. Latam outranks B3–B11.
4. As S0 + S2 land, start S3 per lesson, Aula 05 first. From there each lesson flows through S4 → blueprint → panel → writer → checks → queue on its own.
5. Keep all 16 slots full until §1 is true.
