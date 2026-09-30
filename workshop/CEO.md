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

## State (30/09 ~15:40)
Shipped in the last 24 h: see `git log` in study-lab. Headlines: the D1 front template for all 7 courses (+ lesson descriptions, bibliographies), D4 modo avião phrases, D5 bookmarks + Meu caderno, home masthead removal, the figure-legibility repair (labels ≥11 px) across 6 courses, 35 Controle box figures redrawn, curation builds for Processo + MJ, D2 ius commune plates on 5 MJ lessons, C9 Latam bets and course intros.
Measured 30/09 (words per lesson): Contratos 1.3k · Controle 1.7k · MJ 2.6k · Latam 3.5k · Const I 5.3k · Processo 5.8k · Delito 7.3k. Class registers differ per course: units 0–11, gists 0–100%, reading time on some, three different exam-division styles.
The headless Codex machine (runner/watcher/LaunchAgent) is RETIRED. Codex runs in its app; the chairman tracks usage himself.

## In flight
- Codex app: nothing launched yet under the new mandate. The remaining pre-mandate queue is in the baton entry "BACK TO THE APP + BATON" (Controle/Contratos curation builds, front drawings r3, Const I/Latam curation, plates-2, box detector, Delito wave 2). **Re-express each as atomic issues under the new mandate** rather than running them as mega-orders.

## Next up (in order)
1. **Finish Phase 0 foundations**: (a) move the site-building tools that still live in `work/relay-design-2026-09-29/` (`d1/front.py` + `d1/data/`, `gates/jank.mjs`, `gates/gate.mjs`, `fr/check_text.py`, `d1/check_front.py`, `d2/*` plate tools) into the site repo's `tools/` with paths fixed, plus `tools/check_all`; (b) a one-time cheap diff per course (regenerate to a temp dir vs live): archive any generator that doesn't reproduce live (Delito's is known stale) and treat that course's live HTML as canonical; write the result as one line per course in `tools/SOURCES.md`; (c) give each doc a single job: protocols = why, specimen = look and signs, ISSUES.md = history, baton = live coordination only (archive old baton log entries to `Relay Baton — archive.md`).
2. **Cycle 0: the class register + specimen page.** Anatomy (to refine under "signs over text"): unit header (mono label, sans title, one serif line of what the unit lets you do) → lesson rows (number · title · serif gist ≤2 lines · a drawn clock sign + minutes computed from word count · part ticks for multi-page lessons · "complementar" state) → exam FOLD between rows (a ruled line with a mono label; --conc only for the upcoming exam), no colored row bars → a missing gist shows as a quiet gap, never a different layout. Build once in `front.py`; ship to all 7 fronts as PR #1; ISSUES.md #1.
3. **Content cycles for Codex** (one issue per brief): gists written as "what this lesson lets you do" for Controle (0/36) and Delito (0/20) → units for Const I and Latam → course decks rewritten as function.
4. **Lesson-page anatomy + subpage standard** (the same shared-hand treatment for lesson pages: hero, chapter heads, bets, figures, quiz, endnav, the "Nesta unidade · I · II" strip).
5. **Size outliers as cycles**: Delito S19 8.7k, Const I aula-03-república 7.2k, Contratos' thin lessons (deepen from sources).
6. The pre-mandate figure work (Controle/Contratos curation, front drawings, plates, box detector), re-expressed as atomic issues.

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
