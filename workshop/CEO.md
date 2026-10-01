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
| Agent status registry | `agents/` here (old `~/Documents/agents` = symlink) |
Renamed 30/09 night (was `study-lab` / `study-lab-private`); compatibility symlinks at the old `~/Developer/` paths keep old scripts working. Codex worktrees were repaired with `git worktree repair`.
Binaries (PDFs, screenshots, node_modules, geo caches over 5 MB) live locally here but are git-ignored. Raw course material (`~/Desktop/UFRGS 2026-2`) is the chairman's and stays put.

## After a factory reset (chairman planned one on 30/09)
If `~/Developer` is missing, restore first:
1. `mkdir -p ~/Developer && cd ~/Developer && gh repo clone Benecles/ordenacoes-filipinas && gh repo clone Benecles/ordenacoes-filipinas-workshop`
2. Restore the dotfiles per `dotfiles/README.md` (Codex config + AGENTS.md; Claude CLAUDE.md + memories).
3. Recreate the convenience symlinks only if the old paths are wanted: `~/Desktop/Relay Baton.md` → this repo's baton; `~/Documents/Protocols` → `protocols/`; `~/Documents/agents` → `agents/`.
4. Git-ignored binaries (source-intake exam PDFs, book extracts, page captures) come back only if the chairman restored them from his Google Drive backup; everything else is in git.

## The mandate (chairman's direction, 30/09; read this twice)
1. **The design system is the product.** Exams don't gate development; this site is one study resource among many. Ship every day.
2. **Show, don't tell. Function, not description. Signs over text.** Never caption what's already visible (the "O semestre, desenhado." masthead was removed for this reason). When words are needed, say what a thing DOES, not what it IS. Guiding question for all design work: *what does this do?* A drawn sign (an orange airplane in an orange ring) beats a sentence. Course decks answer "what does this course let you do?".
3. **Pixar, not a senate.** A shared hand with many voices: each course front's feature drawing (the planta: a map, a sluice, routes to the STF) is free and curated to that course. The **class register** below it is one shared instrument: identical anatomy, type, signs and spacing on every course. A standard is ONE implementation plus a **specimen page** showing every state with the reason for it. Examples over rules; no benchmark-maxxing.
4. **A lesson is one sitting**: one syllabus topic, readable in about 15–25 min (roughly 2.5–4.5k words). Split a topic past one sitting into parts; deepen one thinner than one sitting. The data flags outliers (>2× or <½ the site median) for a human look. It's never a pass/fail target.
5. **Atomic cycles, like clockwork**: find an issue → diagnose → iterate → document → ship. One issue = one branch = one PR = one merge (the app shows the merge card). Every merge adds a line to `ISSUES.md` (site repo) and a patch-note line. Engineers, not execs: no top-down audits, no auditing audits, no inference-heavy reviews. Cheap scripts are fine.
6. **Bulk/content work goes to Codex in the app** via the baton, one issue per brief, staged on a branch; the CEO gates and merges. The CEO builds design-language components personally.

## State (01/10 ~02:00, handed over by Claude Opus 5.5)
- **Site:** Ordenações Filipinas, https://benecles.github.io/ordenacoes-filipinas/ (repo `Benecles/ordenacoes-filipinas`, folder `~/Developer/ordenacoes-filipinas`). Workshop: `Benecles/ordenacoes-filipinas-workshop` / `~/Developer/ordenacoes-filipinas-workshop` (old `study-lab*` paths are compat symlinks).
- **Shipped 30/09–01/10 (site PRs #14–#27):** tools port (`tools/fronts/`, `tools/check_all.sh`); register data contract v2 + data for all 7 courses (REG-1..7); rename; **class register** on all 7 fronts (#27; specimen `specimen/register.html`). `ISSUES.md` logs each.
- **Coordination is GitHub Issues now** (workshop repo; labels `codex`, `pipeline`, `needs-gate`, `gate:approved`, `blocked`, `course:*`, `figures`). `Relay Baton.md` is FROZEN (history + Build-process lessons). `~/.codex/AGENTS.md` points Codex at `gh issue`. No Project board yet (token lacks `project` scope: chairman would run `gh auth refresh -s project`).
- **Source Pipeline** (`protocols/CUFRGS Source Pipeline.md`): Controle pilot passed S0–S2 (course map with real prerequisites, shelf of 100 sources, 187 chapters in 8 books, slides, Moodle; Gilmar scan OCR'd). Extracted text is committed under `work/pipeline/`.
- **Delito P1 dossier** (chairman, 01/10; P1 was 01/10): `~/Desktop/Teoria do Delito - Dossie P1 para IA.pdf` (358 pp; P1 POSTPONED, new date unknown, so the dossier carries no exam date), built by `work/dossie-delito-p1/build.py` (Latam-dossier format: AI instructions, plano, slides, past P1s, CP arts. 1–31, site guide, doctrine packets). Reuse it for the P2 (10/12) by changing scope/pages.

## In flight
- **Workshop issue #2 PIPE-2b** (`codex`, not blocked): section-split the core controle chapters (Mendes ch. 160k words etc.), Lenza by §, fetch Leis 9.868/9.882/11.417, fix the S2 check. Then #3 PIPE-3 triage, #4 PIPE-4 compendia, #5 PIPE-5 Aula 30 ADC (blueprint → Sol panel → CEO reads → write). #6 LBL-1 crossed labels (not Controle/Contratos).
- **The Codex orchestrator must be swapped (step 0 below).** The old one ran on the baton.

## Next up (in order)
0. **Write the new Codex orchestrator prompt and give it to the chairman** (he closes the old instance and pastes it into a fresh one, Luna high). Draft to check and send:
   > You are the Codex orchestrator for the Ordenações Filipinas study site. Read `~/.codex/AGENTS.md`, then `~/Developer/ordenacoes-filipinas-workshop/protocols/CUFRGS Source Pipeline.md` in full, then the "Build-process lessons" section of `~/Developer/ordenacoes-filipinas-workshop/Relay Baton.md` (the rest is frozen history). Your work queue is GitHub Issues: `gh issue list -R Benecles/ordenacoes-filipinas-workshop -l codex`. Work only issues without `blocked` or `needs-gate`; read each issue fully before starting. Delegate each stage to a worker with `fork_turns:"none"` at the model the protocol assigns (Sol high for S0 and the S5a panel; Luna xhigh for triage and writing; Luna max for blueprints; Luna high for mechanical stages). You coordinate, run checks, comment results on the issue (`gh issue comment`), add `needs-gate`, and STOP that issue until the CEO adds `gate:approved`; when a gate is approved, remove `blocked` from the next issue and continue. Never merge. Start with #2 (PIPE-2b) and, in parallel, #6 (LBL-1).
1. **Gate PIPE-2b (#2)** when it shows `needs-gate`: check section files ≤ ~15k words for the core chapters, Lenza § split, statutes present, S2 check fails on a missing index. Then `gate:approved` + unblock #3.
2. **Gate PIPE-3 triage (#3) closely**: each lesson gets specific sections, not whole chapters; básica essencial (Lenza, Mendes) first; background = prerequisites' primaries.
3. **Controle Aula 01 reference rebuild by the CEO** (after #4 compendia exist): text + instrument figures, by hand; it's the bar for S5.
4. Gate PIPE-5 (#5): read the blueprint + panel verdict; spot-check the panel's first ~10 verdicts.
5. Next design piece: the lesson-page anatomy + subpage standard. Then course decks as function; then Contratos through the pipeline (books now on disk).

## Quality findings and sources (30/09–01/10; why the pipeline exists)
- **Text:** Controle is genuinely weak: median lesson 1.25k words (other courses 2.7–3.8k); Aula 01 circles abstractions, promises an example it never gives, repeats its own summary, and ends with a "Fontes e limites" disclaimer (breaks the no-citations rule). Aula 24 is decent (concrete, statute-anchored). Contratos is equally thin (1.06k median). Cause: writers got slides plus scattered ad-hoc extracts, never per-lesson prepared sources.
- **Figures:** chairman: every Controle figure is at the level of the Aula 01 triangle, "completely unacceptable"; the Latam atlas plates are the bar. Fix = Visual Genres v2 "Instruments, not diagrams" + the same agent writes text and figures. **If Codex can't reach the bar in the ADC pilot, the chairman wants to evaluate plugins** (something launched at a dev day on 29/09; ask him for the link; don't guess).
- **Sources on disk:** Controle 7/8 base books + Lenza (AZW3) + new Gilmar Mendes *Aspectos* (a 146-pp SCAN: needs Tesseract) + ADC deck (`01 Slides/30 - ADC.pdf`) + Moodle ADI/ADC exercise list (`03 Moodle/2026-09-30 scrape/`). Contratos now has Venosa (17ª ed., 2016) and Caio Mário III (2014): both pre-Lei 13.874/2019 (arts. 421/421-A), so route post-2019 material from Gerson Branco's articles. Delito: Ilha da Silva skipped (not needed); Faccini's *Teoria Geral do Crime* not findable, so use his *Lições Introdutórias* (he's the professor). Still missing, low priority: Duque (Controle professor's book), Dirley da Cunha, Savigny, Couto e Silva, Martins-Costa (*Método da Concreção*). Const I has no plano on disk.
- **Existing extracts to reuse:** `work/book-extracts/` (+ `book-extract-map.md`), `work/controle-depth/extracts/`, `work/source-intake-2026-09-28/` (Metodologia, Processo, Const I intake on the same philosophy).

## Open decisions for the chairman
- Optional: grant the `project` scope (`gh auth refresh -s project`) if he wants a Project board on top of the issues.
- If the ADC pilot (#5) misses the figure bar: evaluate the dev-day plugins (ask him for the link).

## Gotchas (hard-won; the full list is in `Relay Baton.md` → "Build-process lessons" and ~/.codex/AGENTS.md)
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
