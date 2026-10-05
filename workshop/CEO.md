# CEO.md: the chair's handoff

**Magic phrases** (wired in ~/.claude/CLAUDE.md):
- **"Take the chair"**: you are the new CEO of the CUFRGS study-site project. `git pull` this repo, read this file top to bottom, then the files it points to, then do **Next up #1**. Don't re-derive what's written here.
- **"Hand over the chair"**: update this file (State, In flight, Next up, Open decisions, Gotchas) so a cold instance can continue, then commit and push, and confirm to the chairman.

Roles: **Benecles = executive chairman** (sets direction, owns decisions listed under "Open decisions"). **Claude = CEO** (design and editorial authority, writes briefs, builds the design language, gates and ships). **Codex (in the Codex app, managed by Benecles)** = the engineering floor for bulk/content work, coordinated through `Relay Baton.md`.

## Where everything lives (all out of iCloud as of 30/09)
| What | Path |
|---|---|
| Public site repo (what readers see) | `~/Developer/ordenacoes-filipinas` → github.com/Benecles/ordenacoes-filipinas (`main`; push = deploy) |
| This workshop repo (private) | `~/Developer/ordenacoes-filipinas-workshop` → Benecles/ordenacoes-filipinas-workshop |
| Work tree: drafts, specs, generators, build tools, staging, history | `work/` here (old path `~/Documents/Codex/2026-09-23/you-h/work` is a symlink) |
| Standards (why) | `protocols/`: CUFRGS Design Direction, Visual Genres, Writing Standard (old `~/Documents/Protocols` = symlink) |
| Live coordination with Codex | **GitHub Issues** on this repo (label `codex`). `Relay Baton.md` here is frozen history + Build-process lessons |
| Bug catalogue (symptom → cause → fix → check) | `BUGS.md` here; every fix adds a row |
| Agent status registry | `agents/` here (old `~/Documents/agents` = symlink) |
Renamed 30/09 night (was `study-lab` / `study-lab-private`); compatibility symlinks at the old `~/Developer/` paths keep old scripts working. Codex worktrees were repaired with `git worktree repair`.
Binaries (PDFs, screenshots, node_modules, geo caches over 5 MB) live locally here but are git-ignored. Raw course material (`~/Documents/UFRGS 2026-2`, moved off the Desktop 02/10) is the chairman's: read it, never reorganise it. **The Desktop holds only Felipe and Mark** (work files); put nothing else there.

## After a factory reset (chairman planned one on 30/09)
If `~/Developer` is missing, restore first:
1. `mkdir -p ~/Developer && cd ~/Developer && gh repo clone Benecles/ordenacoes-filipinas && gh repo clone Benecles/ordenacoes-filipinas-workshop`
2. Restore the dotfiles per `dotfiles/README.md` (Codex config + AGENTS.md; Claude CLAUDE.md + memories).
3. Don't recreate Desktop shortcuts (chairman, 02/10). Optional: `~/Documents/Protocols` → `protocols/`; `~/Documents/agents` → `agents/`.
4. Git-ignored binaries (source-intake exam PDFs, book extracts, page captures) come back only if the chairman restored them from his Google Drive backup; everything else is in git.

## The mandate (chairman's direction, 30/09; read this twice)
1. **The design system is the product.** Exams don't gate development; this site is one study resource among many. Ship every day.
2. **Show, don't tell. Function, not description. Signs over text.** Never caption what's already visible (the "O semestre, desenhado." masthead was removed for this reason). When words are needed, say what a thing DOES, not what it IS. Guiding question for all design work: *what does this do?* A drawn sign (an orange airplane in an orange ring) beats a sentence. Course decks answer "what does this course let you do?".
3. **Pixar, not a senate.** A shared hand with many voices: each course front's feature drawing (the planta: a map, a sluice, routes to the STF) is free and curated to that course. The **class register** below it is one shared instrument: identical anatomy, type, signs and spacing on every course. A standard is ONE implementation plus a **specimen page** showing every state with the reason for it. Examples over rules; no benchmark-maxxing.
4. **A lesson is one sitting**: one syllabus topic, readable in about 15–25 min (roughly 2.5–4.5k words). Split a topic past one sitting into parts; deepen one thinner than one sitting. The data flags outliers (>2× or <½ the site median) for a human look. It's never a pass/fail target.
5. **Atomic cycles, like clockwork**: find an issue → diagnose → iterate → document → ship. One issue = one branch = one PR = one merge (the app shows the merge card). Every merge adds a line to `ISSUES.md` (site repo) and a patch-note line. Engineers, not execs: no top-down audits, no auditing audits, no inference-heavy reviews. Cheap scripts are fine.
6. **Bulk/content work goes to Codex in the app** via the baton, one issue per brief, staged on a branch; the CEO gates and merges. The CEO builds design-language components personally.
8. **The CEO is the master prompter (chairman, 03/10; the most important rule here).** We already have more building agency than we can use; doing the work yourself, or asking agents to emulate you, is not the lever. The CEO's job is the WHAT: take the chairman's thin idea and develop it to the fullest (what it is, what it looks like, where it sits, how it behaves, what it must never do, how it fits the house and its ethos), then hand that to the orchestrator as a master brief. The HOW is the orchestrator's. Priorities, in order: (1) what it is and what it's for, (2) what it looks and feels like, in detail, (3) implementation hints, only if they matter. The CEO keeps final say at the gate. Example: "airplane mode" is not a button to build; it's a brief: an orange plane in an orange ring, bottom left, what it does, what the reader sees offline, which words it uses.
7. **The rocket line (chairman, 01/10).** Work flies in staggered waves: launch #1, finish #2, build #3, design #4, all at once. Every gate turns its findings into numbered entries in `FLIGHT-LOG.md`, and every in-flight stage applies them before its next step. Never let a stream idle waiting on a gate; the gate feeds the log, the log feeds the line.

## State (05/10 night, handed over by Claude Opus 5.5)
- **Read mandate #8 first** (the CEO writes the WHAT; the orchestrator owns the HOW). **But note the chairman's 04/10 override, still in force: no gates.** Codex merges its own PRs after its checks; the CEO reviews what landed on the live site and fixes from there. When Codex is out of credits, the CEO builds directly (the chairman asked for that on 05/10).
- **LAT-1 (workshop #25): rebuilding Direito Latino-americano is the active project.**
  - **Done, live and CEO-built** (site #70–#77):
    - Aulas **01, 02, 05, 06**, each rebuilt from its blueprint, with Aula 05 as the density reference;
    - the **course front** "Quem respondeu a quem" (map of the five courts plus a list of dialogues; generator `work/latam-build/front_courts.py`);
    - **every Latam figure** recast as an instrument (generators in `work/latam-rebuild/`);
    - a **phone pass** (no forced 19 px, no full-bleed hack, haloed map labels, comparison tables as stacked cards);
    - a **course QA sweep** (backstage lines out, hero reading times = front clock);
    - a **Writing Standard Part D deslop of 01 and 02** (`work/latam-rebuild/deslop_01_02.py` lists the patterns).
  - **Not yet rebuilt (older Codex text, accurate and cleaned, but still with an "Aprofundamento" appendix and old-style tests):** 03, 04, 07, 08, 09 and the revisão.
  - **Blueprints on disk** (`work/pipeline/direito-latino-americano/compendium/<aula>/blueprint.md` + `panel.md`):
    - **08:** APPROVED;
    - **04, 07, 09:** REVISE, with the panel's points in panel.md;
    - **03:** never panelled;
    - **revisão:** none.
  - S0–S4 are complete; all 950 chapter texts are in the main checkout (git-ignored).
- **How a Latam lesson rebuild is done** (repeat this): read blueprint + panel → read the live page → read the decisive source passages (grep the compendium, never model memory) → write `work/latam-rebuild/aNN_patch.py`, which rebuilds the page from the live HTML. The script:
  - keeps figures, defs SVGs, the bet and the quiz verbatim;
  - folds the Aprofundamento into the chapters;
  - removes backstage text.

  Then: deslop against Writing Standard Part D (read the last sentence of every paragraph for moral closers) → `slop_lint` + `anatomy_check` → breakscan at 1280 + 375 → hero "Leitura" = front clock → regenerate the front → the site-edit procedure (gotchas) → ISSUES.md line → PR → merge.
  - **Figure conventions:** `work/latam-rebuild/fk.py` (`.figkit.lt`, 18 px mono / 21 px hand on upright phones, ≤ 28 characters per mono line, line spacing ≥ 28/30 px, titles ≤ 30 characters); maps on `Frame('courts')`.
  - **Breakscan baseline:** desktop 0 findings; phones 25, all haloed labels on four legacy maps (A01 crisis + strata, A02 courts, A03 route). A new finding is a regression.
- **Facts corrected in the rebuild; don't let them regress:**
  - "mientras el soberano así lo desee" is the *petitioners'* argument in SCP 0084/2017, not the TCP's;
  - Argentina's review is diffuse; Uruguay's is concentrated, with effects in the case;
  - Engelmann & Bandeira's Colombian court is the Corte Suprema de Justicia, not the Corte Constitucional;
  - the 19-country table is undated;
  - the three-project typology is not attributed in the course sources (don't credit Gargarella);
  - Gelman was unanimous (Vio Grossi concurred);
  - Sentencia 65/2014 is not about Gelman.
- **Other merged since 04/10:** Controle 02/04/05/08, Processo A01 figure, CHG-1 bento, REG-H1, BRK-1 breakscan (workshop #36: fonts, 1280 + 375, panel steps, CLIP/OVERFLOW).
- **Reference set (unchanged):** Controle Aula 01 + REF comments; reference blueprint and template; FLIGHT-LOG F-001…F-027; BUGS.md; Visual Casting; Writing Standard.
- **Machine:** the 15" MacBook Air; `gh` authed as Benecles. **Desktop holds only Felipe + Mark.** Course material is in `~/Documents/UFRGS 2026-2`.

## Since 05/10 evening (Claude Opus 5.5, second session)
- **MAP-L1 merged (site #78):** Latam front map gets its colour washes and engraved coasts back; A01 hero labels re-placed by a measured search and routes drawn whole; A01 Fig. 1 legend words restored; A02 Fig. 2 legend realigned; dotted meridians dropped. Scripts + reusable tools in `work/latam-maps/` (`labeler.js`: `placeLabels`, `probe`, `nudge`, run in the browser; `run.sh SITE` rebuilds from main). Breakscan 1280 = 0 on the three pages.
- **Chairman rule, 05/10: desktop first.** No phone work (375 breakscans, phone label fixes) until desktop is perfect. Phone findings are logged debt only.
- **Writing Standard Part D extended** (preamble on what slop is + D9 density limits + D10 the chairman's five pathologies: fake disagreement, circular causal explanation, unnecessary restatement, excessive sectioning, reflexive qualification). Old copy in `protocols/Superseded/`.
- **Briefs filed for Codex** (`work/briefs/2026-10-05-anti-slop-pipeline.md`): workshop #57 SLOP-2 (STYLE.md, PT linter rates, corpus discovery, span-level critic, AGENTS.md wiring) and #58 TXT-L1 (AP Stylebook + deslop on Latam front/A01/A02; AP source `~/Downloads/ap-stylebook.pdf`, 2000 ed.). The chairman wants Codex to do this engineering to save CEO tokens.
- **After #58 lands: the CEO's final aesthetics QA** on the Latam front, A01, A02 (chairman: "things need to look spectacular"). Known desktop items to look at: the A02 atlas sits small in its panel with empty space bottom-right; the front map column could be larger; the A01 hero crops Spain at the top edge.
- Aula 08 rebuild was started and parked (sources read and verified, no script written). The facts are checked: 108 tutelas/1,150 families; Sala Tercera (Cepeda, Córdoba Triviño, Escobar Gil); Auto 008 Sala Segunda; budget 103,491→70,783 million; "no superação parcial" is Auto 008 considerando 34, not ordinal 1º.

## In flight (Codex, when it has credits)
- **Codex is out of credits as of 05/10 night.** Its handoff is the **RESUME HERE** section at the top of `work/briefs/2026-10-04-orchestrator-prompt.md` (kept current through 05/10 night). The paste message for a fresh Codex window is in that file's history; it says: pull both repos, read that file starting at RESUME HERE, and execute "What's left".
- **Open site PRs:**
  - **#69 PHN-1:** touches every Latam page and curso.css. It **must rebase; main wins on Latam.**
  - **#68 BIO-2**, **#65 Contratos A01**, **#51 Delito U01:** each per its last verdict.
  - **#55, #60:** Controle A07/A09, per the W2 verdict and the #59 lessons.
- **Workshop PR #42:** PHN-1's docs.
- **Open issues:** #25 LAT-1, #24 PHN-1, #22 BIO-2, #17 CAST-1, #15/#13 Controle waves, #12 PIPE-C, #10 FIG-2, #5 PIPE-5 (Aula 30).
- **`RUN-0410.md`** (the run ledger the plan requires) was never created by Codex; the resume section asks for it.

## Next up (in order)
0. **Codex: #58 TXT-L1, then #57 SLOP-2 (+ addendum), then #59 MOT-1 (interaction motion after fluidfunctionalism.com; CEO gates the feel); #60 SRC-1 source blocks (chairman 05/10: long inline quotes from books and decisions; Writing Standard E2/E3 rewritten; noindex instead of access control). CEO: final aesthetics QA of Latam front/A01/A02 once #58 merges.**
1. **Finish LAT-1, one lesson at a time:**
   - **08** (blueprint APPROVED);
   - **04, 07, 09:** apply panel.md's REVISE points to the blueprint first;
   - **03:** panel the blueprint yourself first, as was done for 02 (approve or revise in ≤ 5 points);
   - **the revisão:** turn it into the eixo workbench (one block per class: eixo, cases, answer frame);
   - then the cards (`cartoes.html`, from one case-data file) and `RETRO.md`.

   Whoever has capacity does it: Codex via the resume section, or the CEO directly with the recipe in State.
2. **Review what Codex merges** (the no-gates mode): read the live page, run the deslop read, and fix with a follow-up PR.
3. **PHN-1 #69:** make sure the rebase keeps the Latam phone pass. Breakscan 375 on Latam must stay at 25.
4. **Remaining legacy figures, optional:** the four Latam maps with phone label crossings, the A02/A07 box heroes, and the A09 decision flow. They are acceptable as they are, so only touch them if there's spare time.
5. Other courses: the Controle waves, PIPE-C and FIG-2/CAST-1 resume under the same no-gates rule.

## Quality findings and sources (30/09–01/10; why the pipeline exists)
- **Text:** Controle is genuinely weak: median lesson 1.25k words (other courses 2.7–3.8k); Aula 01 circles abstractions, promises an example it never gives, repeats its own summary, and ends with a "Fontes e limites" disclaimer (breaks the no-citations rule). Aula 24 is decent (concrete, statute-anchored). Contratos is equally thin (1.06k median). Cause: writers got slides plus scattered ad-hoc extracts, never per-lesson prepared sources.
- **Figures:** chairman: every Controle figure is at the level of the Aula 01 triangle, "completely unacceptable"; the Latam atlas plates are the bar. Fix = Visual Genres v2 "Instruments, not diagrams" + the same agent writes text and figures. **If Codex can't reach the bar in the ADC pilot, the chairman wants to evaluate plugins** (something launched at a dev day on 29/09; ask him for the link; don't guess).
- **Sources on disk:** Controle 7/8 base books + Lenza (AZW3) + new Gilmar Mendes *Aspectos* (a 146-pp SCAN: needs Tesseract) + ADC deck (`01 Slides/30 - ADC.pdf`) + Moodle ADI/ADC exercise list (`03 Moodle/2026-09-30 scrape/`). Contratos now has Venosa (17ª ed., 2016) and Caio Mário III (2014): both pre-Lei 13.874/2019 (arts. 421/421-A), so route post-2019 material from Gerson Branco's articles. Delito: Ilha da Silva skipped (not needed); Faccini's *Teoria Geral do Crime* not findable, so use his *Lições Introdutórias* (he's the professor). Still missing, low priority: Duque (Controle professor's book), Dirley da Cunha, Savigny, Couto e Silva, Martins-Costa (*Método da Concreção*). Const I has no plano on disk.
- **Existing extracts to reuse:** `work/book-extracts/` (+ `book-extract-map.md`), `work/controle-depth/extracts/`, `work/source-intake-2026-09-28/` (Metodologia, Processo, Const I intake on the same philosophy).

## Open decisions for the chairman
- **Gates or no gates going forward?** The 04/10 override ("ship as you go, CEO reviews after") is still in force. It has worked for speed. The cost is that faults ship before anyone reads them; the 05/10 QA sweep found backstage text on seven pages.
- **The four legacy Latam maps:** are their phone label crossings (haloed, legible) acceptable, or redraw them on `Frame('courts')`?

## Gotchas
- **Map labels: measure, don't nudge by eye.** Load `work/latam-maps/labeler.js` into the page and use `placeLabels`/`probe`; old route paths may have holes cut where old labels sat (join them when labels move).
- **`latam-build/maps.py` needs `PYTHONPATH=../contract-build/generators`** for its `kit` import.

## Gotchas (hard-won; the full list is in `Relay Baton.md` → "Build-process lessons" and ~/.codex/AGENTS.md)
- **Port 8793 can be Codex's `http.server` serving another checkout** (05/10 it served `ordenacoes-filipinas-delito-u01`). A breakscan pointed at it silently tests the wrong pages. Serve your checkout on its own port (the CEO's gate config now uses 8795 in `~/.claude/launch.json`) and pass `--base-url` explicitly. Check with `curl …/aula-NN.html | grep "≈"` that you're seeing your build.
- **The site's service worker caches pages.** A browser check can show an old page even with `?r=N`. Unregister it or use a fresh port.
- **Latam pages carry hidden defs SVGs** (`<svg width="0" height="0">` holding `lm-*` map land, `st-*` strata patterns, `fcourts-*`). Any rebuild that re-slices a page must carry every one of them, or the figures silently lose their land and patterns.
- **The Writing Standard linter (`protocols/tools/slop_lint.py`) passing is not enough.** Read the last sentence of every paragraph for moral closers, and check "não X, mas Y" with the delete-the-"não" test.
- **Codex leaves blueprints uncommitted** in the shared checkout. Commit them (05/10: `f61a83d`) before they're lost.
- **Talk to the chairman in full live URLs** (e.g. https://benecles.github.io/ordenacoes-filipinas/specimen/hero.html). A repo path means nothing to him. GitHub Pages serves `main`.
- **Gate workflow that worked (03/10):** a worktree in your scratchpad (`git worktree add <sp>/site origin/codex/X`), merge `origin/main` into it, serve it with a `gate` entry in `~/.claude/launch.json` (port 8793, `python3 -m http.server --directory <sp>/site`), and look panel by panel: scroll each `[data-panel]` step into view, wait ~2.5 s (the crossfade is slow; an earlier screenshot shows ghosts or the previous step), then screenshot. A ship script for merging (merge main, rebuild manifest on conflict, ISSUES line, check_all, push to `codex/X`, `gh pr merge`) is easy to rewrite; offline-manifest is the usual conflict, and taking main's side + `offline_build.py` resolves it.
- **When FIG-2 PRs stack, merge one and the others conflict** in `specimen/figuras.html`, `tools/figkit/inject.py`, `tools/figkit/specimen.py`. Ask Codex to rebase and keep both entries; don't hand-merge generator code.
- **The workshop checkout is shared with Codex:** untracked files can block your `git pull`. Diff them against `origin/main` before removing; never delete files that differ.
- **Codex orchestrator vs computer use:** it reached for browser driving for a 7-page table check (workers can't see its browser, so it did bulk work itself). Route checks into scripts (breakscan) that any worker can run.
- `slop_lint` lives in the workshop (not `tools/editorial/` in the site repo); run it from there.
- rareui.com (cited for the register hover) was a passing Twitter find, not a spec. Don't chase it.
- **Search `BUGS.md` by symptom before debugging; add a row with every fix.**
- **`git status -sb` before committing in the workshop:** Codex switches the shared checkout to its `codex/*` branches (01/10 a commit landed on `codex/chg-1-bugs`).
- **zsh `:c` again (01/10):** `"origin/codex/x-$n:courses/..."` broke a gate loop. Always `${n}` before a colon.
- **Gate lessons by reading, not by the numbers:** all six W2/W3 PRs passed check_all and had the right length, and none was shippable.
- **Chairman's no-list (01/10):** no self-monitoring or self-guard mods/hooks (context weather, merge guards), no phone-variant figures. He manages context himself.
- **Gate figures by looking, and probe the specimen.** breakscan scans `courses/` only. For kit work, run the CROSS/CLASH probe on `specimen/figuras.html` in the browser (the same logic as breakscan's `probe`), and check the content bbox stays inside the viewBox.
- **Site edits:** after injecting figures run `tools/offline_build.py`, then `git checkout -- assets/front.css specimen/register.html` (offline_build wants to change both: known debt, its own issue), then `tools/polish.py capture` and `rm -rf tools/polish/specimen`, then `git add`, then `check_all`.
- **Saved gate check:** `work/checks/gate_prs.sh <N>…` (svgcheck: text outside SVGs byte-identical, labels unchanged, no >3 KB bloat).
- **Codex app sessions:** give the chairman self-contained prompts for NEW windows when the old orchestrator's context is big; one-line add-ons for the running one.
- Codex workers: `fork_turns:"none"` always; parallelism stays at 16.
- A check must FAIL on the known-bad state before its PASS means anything.
- Refresh from live right before editing; ship via git merge, not copied snapshots.
- Crops only, never full-page screenshots; the disk once filled and iCloud evicted files.
- `pkill -f <pattern>` kills your own shell. Kill by pid.
- Big jobs fail partway: chunk to ≤6 units.
- Never let a generator regeneration revert live edits (polish layer / SOURCES.md).
- Never install daemons, LaunchAgents or cron jobs without the chairman's OK.
- zsh: `"$k:codex"` parses `:c` as a modifier. Brace variables before a colon: `"${k}:codex"`. (Silently broke 5 pushes on 30/09 while the merges still ran.)
- Codex keeps worktrees on its `codex/*` branches: gate on a local `gate/*` copy and push `gate/X:codex/X`.
- `tools/check_all.sh` compares the regenerated fronts against the git INDEX: `git add` your edits before running it, or it FAILs on your own uncommitted changes.
- Local preview: something (Codex) usually serves the site on :8790; read from it. Claude's own config is `~/.claude/launch.json` (:8791). The browser HTTP-caches pages: add `?r=N` after regenerating.
- **Codex per-stage models vs the old spawn rule:** AGENTS.md / memory say workers spawn with `fork_turns:"none"` and no model/effort args (forks cloned costly history). The Source Pipeline needs per-stage models (Sol for S0 + panel, Luna max for blueprints). `fork_turns:"none"` + an explicit model is fine; if the app can't set a worker's model, the chairman runs those stages in a separate instance.
- The polish layer: 67 pre-existing "unlocatable" edits on lesson pages are old debt, not new breakage. The front-page polish records were retired in #27.
- Long sessions balloon: hand over the chair once context is large.
