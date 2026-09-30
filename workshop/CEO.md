# CEO.md: the chair's handoff

**Magic phrases** (wired in ~/.claude/CLAUDE.md):
- **"Take the chair"**: you are the new CEO of the CUFRGS study-site project. `git pull` this repo, read this file top to bottom, then the files it points to, then do **Next up #1**. Don't re-derive what's written here.
- **"Hand over the chair"**: update this file (State, In flight, Next up, Open decisions, Gotchas) so a cold instance can continue, then commit and push, and confirm to the chairman.

Roles: **Benecles = executive chairman** (sets direction, owns decisions listed under "Open decisions"). **Claude = CEO** (design and editorial authority, writes briefs, builds the design language, gates and ships). **Codex (in the Codex app, managed by Benecles)** = the engineering floor for bulk/content work, coordinated through `Relay Baton.md`.

## Where everything lives (all out of iCloud as of 30/09)
| What | Path |
|---|---|
| Public site repo (what readers see) | `~/Developer/study-lab` → github.com/Benecles/study-lab (`main`; push = deploy) |
| This workshop repo (private) | `~/Developer/study-lab-private` → Benecles/study-lab-private |
| Work tree: drafts, specs, generators, build tools, staging, history | `work/` here (old path `~/Documents/Codex/2026-09-23/you-h/work` is a symlink) |
| Standards (why) | `protocols/`: CUFRGS Design Direction, Visual Genres, Writing Standard (old `~/Documents/Protocols` = symlink) |
| Live coordination with Codex | `Relay Baton.md` here (Desktop copy = symlink) |
| Agent status registry | `agents/` here (old `~/Documents/agents` = symlink) |
Binaries (PDFs, screenshots, node_modules, geo caches over 5 MB) live locally here but are git-ignored. Raw course material (`~/Desktop/UFRGS 2026-2`) is the chairman's and stays put.

## The mandate (chairman's direction, 30/09; read this twice)
1. **The design system is the product.** Exams don't gate development; this site is one study resource among many. Ship every day.
2. **Show, don't tell. Function, not description. Signs over text.** Never caption what's already visible (the "O semestre, desenhado." masthead was removed for this reason). When words are needed, say what a thing DOES, not what it IS. Guiding question for all design work: *what does this do?* A drawn sign (an orange airplane in an orange ring) beats a sentence. Course decks answer "what does this course let you do?".
3. **Pixar, not a senate.** A shared hand with many voices: each course front's feature drawing (the planta: a map, a sluice, routes to the STF) is free and curated to that course. The **class register** below it is one shared instrument: identical anatomy, type, signs and spacing on every course. A standard is ONE implementation plus a **specimen page** showing every state with the reason for it. Examples over rules; no benchmark-maxxing.
4. **A lesson is one sitting**: one syllabus topic, readable in about 15–25 min (roughly 2.5–4.5k words). Split a topic past one sitting into parts; deepen one thinner than one sitting. The data flags outliers (>2× or <½ the site median) for a human look. It's never a pass/fail target.
5. **Atomic cycles, like clockwork**: find an issue → diagnose → iterate → document → ship. One issue = one branch = one PR = one merge (the app shows the merge card). Every merge adds a line to `ISSUES.md` (site repo) and a patch-note line. Engineers, not execs: no top-down audits, no auditing audits, no inference-heavy reviews. Cheap scripts are fine.
6. **Bulk/content work goes to Codex in the app** via the baton, one issue per brief, staged on a branch; the CEO gates and merges. The CEO builds design-language components personally.

## State (30/09 ~17:00)
- **Out of iCloud (done):** the site is at `~/Developer/study-lab` (standalone clone on main); the workshop (work/, protocols/, agents/, Relay Baton.md, CEO.md) is here. Old paths are symlinks; all verified. Codex trusts both folders.
- **Chairman is switching off iCloud Desktop & Documents** (Keep Downloaded → toggle off → move files home). Afterwards, re-verify the symlinks (`~/Desktop/Relay Baton.md`, `~/Documents/Protocols`, `~/Documents/agents`, the old `work/` and `study-lab-publish` paths) and run a site build.
- **Shipped today via PR** (the app shows merge cards): study-lab#13, the hero/figure line animations finish drawing (dasharray 1200 → 3000; the site-wide scan finds 0 remaining); study-lab-private#1, the workshop move + this file. Cycles from here: branch → PR → merge.
- Measured 30/09 (words per lesson): Contratos 1.3k · Controle 1.7k · MJ 2.6k · Latam 3.5k · Const I 5.3k · Processo 5.8k · Delito 7.3k. The class registers differ per course (units 0–11, gists 0–100%, three exam-division styles).
- The headless Codex machine is retired; Codex runs in its app; the chairman tracks usage himself.

## In flight
- **Label/line crossings: 47 pages** (heroes + numbered figures, all panels; mostly Controle, Contratos, Latam). Scanner: `work/checks/breakscan.mjs <site dir> <out.csv>` (serve the site on :8790 first; it reports SHORT/CROSS/CLASH; ignore SHORT hits with a dash ≤ 8, those are deliberately dashed lines). → Write this as ONE atomic Codex issue in the baton, with the scanner as the check (CROSS + CLASH = 0 on the pages it fixes; text outside SVGs unchanged).
- **Tools port** (study-lab branch `tools-home`, pushed? NO, local only; a WIP commit): front.py + data + shells and gates moved into `tools/`. BLOCKER: the staging `d1/data` picked up the INTERRUPTED, unapproved front-drawings-r3 output (e.g. a Processo "railway" drawing), so regenerating from it changes live fronts. Fix: reconcile `tools/fronts/data/*.json` so that regenerating reproduces live `courses/*/index.html` byte-for-byte (except asset ?v= stamps) BEFORE merging; then delete the relay-design d1 copy from use.
- Pre-mandate figure queue: the baton entry "BACK TO THE APP + BATON". Re-express as atomic issues.

## Next up (in order)
1. Finish the tools port (reconcile the data, see In flight) → PR → merge. Then `tools/check_all`.
2. **Cycle 0: the class register + specimen page**, under the mandate (signs over text: a drawn clock sign + minutes computed from word count, part ticks, the exam fold, one row per lesson, units always, a missing gist as a quiet gap). Build it once in `tools/fronts/front.py`; ship to all 7 fronts as a PR; ISSUES.md #1.
3. Write the crossed-labels Codex issue into the baton.
4. Content cycles for Codex: gists as "what this lesson lets you do" (Controle 0/36, Delito 0/20) → units for Const I/Latam → course decks as function.
5. The lesson-page anatomy + subpage standard; then size outliers; then the pre-mandate figure work as atomic issues.

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
- Long sessions balloon: hand over the chair once context is large.
