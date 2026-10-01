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
| Live coordination with Codex | `Relay Baton.md` here (Desktop copy = symlink) |
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

## State (30/09 ~17:00)
- **Out of iCloud (done):** the site is at `~/Developer/ordenacoes-filipinas` (standalone clone on main); the workshop (work/, protocols/, agents/, Relay Baton.md, CEO.md) is here. Old paths are symlinks; all verified. Codex trusts both folders.
- **Chairman is switching off iCloud Desktop & Documents** (Keep Downloaded → toggle off → move files home). Afterwards, re-verify the symlinks (`~/Desktop/Relay Baton.md`, `~/Documents/Protocols`, `~/Documents/agents`, the old `work/` and `study-lab-publish` paths) and run a site build.
- **Shipped today via PR** (the app shows merge cards): study-lab#13, the hero/figure line animations finish drawing (dasharray 1200 → 3000; the site-wide scan finds 0 remaining); ordenacoes-filipinas-workshop#1, the workshop move + this file. Cycles from here: branch → PR → merge.
- Measured 30/09 (words per lesson): Contratos 1.3k · Controle 1.7k · MJ 2.6k · Latam 3.5k · Const I 5.3k · Processo 5.8k · Delito 7.3k. The class registers differ per course (units 0–11, gists 0–100%, three exam-division styles).
- The headless Codex machine is retired; Codex runs in its app; the chairman tracks usage himself.

## In flight
- **Source Pipeline** (`protocols/CUFRGS Source Pipeline.md`, chairman's design 30/09): understand → prep → write/edit; Controle pilot = baton PIPE-0..5. Gate every stage. Aula 30 (ADC) is the first S5 edit; the CEO rebuilds Controle Aula 01 from the same compendium as the reference page. Visual Genres v2 adds "Instruments, not diagrams".
- Site renamed **Ordenações Filipinas**: repo `Benecles/ordenacoes-filipinas`, https://benecles.github.io/ordenacoes-filipinas/ (local folder still `~/Developer/ordenacoes-filipinas`). Storage keys now `ordenacoes-*`.
- **Codex REG-1..7**: 2/4/5/6/7 MERGED (#16–20, fix-up #22). REG-1, REG-3 re-issued under contract v2 (#21) (baton): register data (`reg` key: exams, units for Const I/Latam, a `does` line per lesson). Check: `tools/fronts/check_register_data.py` (study-lab#15). Gate each PR: read the `does` lines (function, not description; generic = reject), then merge.
- **Label/line crossings: 47 pages** (heroes + numbered figures, all panels; mostly Controle, Contratos, Latam). Scanner: `work/checks/breakscan.mjs <site dir> <out.csv>` (serve the site on :8790 first; it reports SHORT/CROSS/CLASH; ignore SHORT hits with a dash ≤ 8, those are deliberately dashed lines). → Write this as ONE atomic Codex issue in the baton, with the scanner as the check (CROSS + CLASH = 0 on the pages it fixes; text outside SVGs unchanged).
- ~~Tools port~~ DONE 30/09 evening: study-lab#14 merged. `tools/fronts/data` reconciled from live (drawings verbatim via `drawing.inner_html`; railway gone); `tools/check_all.sh` = regenerate fronts + assetver + FAIL on any diff + check_front. `ISSUES.md` started at #0. The relay-design d1 copy is now retired: use `tools/fronts/` only.
- Pre-mandate figure queue: the baton entry "BACK TO THE APP + BATON". Re-express as atomic issues.

## Next up (in order)
0a. **The PIPE-3 gate is the swap point (chairman, 01/10).** When the chairman brings "PIPE-2 done": (1) the CEO reviews PIPE-1/PIPE-2 and the PIPE-0 prerequisite fix; (2) does the GitHub migration below; (3) hands over the chair (this file). The **new CEO** then writes a fresh orchestrator prompt for the GitHub-based flow (Luna high; PIPE-3 onward; issues instead of the baton; stop at each gate), and the chairman closes the old Codex orchestrator and pastes that prompt into a new instance. Swap both together, CEO first. The old orchestrator's knowledge is all in files (course map, shelf, chapter indexes, baton log), so nothing is lost.
0. **At the first pause where both Codex workstreams sit at a gate: move coordination to GitHub** (chairman, 30/09). The baton becomes Issues in the workshop repo (one per atomic task; labels `codex`/`gate`/`pipeline:sN`/`blocked`; PRs `Closes #n`; gates = comment + `gate:approved` label), plus a Project board; `agents/*.md` replaced by assignee + labels; `ISSUES.md` generated from closed issues. Files stay files: CEO.md, protocols/. **Everything goes to git except** third-party personal data (WhatsApp exports, classmates' notes, MP case files), secrets/machine state, and original book/scan binaries (cold storage in Drive, kept only for re-extraction). Extracted chapter text, compendia, **slide decks (small; their visuals matter for figures)** and page images of key book tables/figures DO go into the private workshop repo (un-ignore `work/pipeline/**`). End state: GitHub is the working environment; the Mac is just one place work runs. Freeze `Relay Baton.md` to its history + build lessons; point AGENTS.md and the Source Pipeline protocol at `gh issue`.
- ~~Cycle 0 class register~~ SHIPPED 30/09 (#27): `_register()` in front.py + `.reg*` in assets/front.css; specimen `specimen/register.html` via `tools/fronts/specimen.py`. Reading time = words/180 wpm, so any lesson-page edit changes its front: regenerate fronts (front.py + assetver) in the same PR or `check_all` fails.
1. **Controle Aula 01 reference rebuild** (after PIPE-4 lands its compendium): text + instrument figures, by hand.
2. ~~Cycle 0~~ (done). **Next design piece:** the lesson-page anatomy + subpage standard.
   (old) **Cycle 0: the class register + specimen page**, under the mandate (signs over text: a drawn clock sign + minutes computed from word count, part ticks, the exam fold, one row per lesson, units always, a missing gist as a quiet gap). Build it once in `tools/fronts/front.py`; ship to all 7 fronts as a PR; ISSUES.md #1. Run `tools/check_all.sh` before every front PR.
2. Gate REG PRs as they land; then Codex LBL-1 (crossed labels, already in the baton).
3. Course decks as function (Codex, after the register ships).
4. The lesson-page anatomy + subpage standard; then size outliers; then the pre-mandate figure work as atomic issues.

## Open decisions for the chairman
- (none pending as of this handoff)

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
- Long sessions balloon: hand over the chair once context is large.
