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

## State (03/10, handed over by Claude Opus 5.5)
- **Read mandate #8 first: the CEO is the master prompter (WHAT, not HOW).** Turn the chairman's ideas into detailed master briefs via GitHub issues; build only trivial fixes; keep final say at the gate.
- **Site shipped this chair:** TXT-1/1b (#46, #49: Aula 01 rebuilt, figures fit, anatomy_check), HERO-0 (#50 specimen), DESK-1 (#61 paths), CHG-2 (#62 changelog open/close all), LAY-1 (#63 prose-only stretches centred, 720 px), REF-1 (#64 Aula 01 annotated with 22 `REF ·` agent notes; REF-LEAK guard).
- **Reference set:** live Controle Aula 01 + its REF comments; reference blueprint `work/pipeline/controle-de-constitucionalidade/compendium/aula-01/blueprint.md` (Method notes); template `protocols/templates/Lesson Blueprint.md`.
- **Figures:** `protocols/CUFRGS Visual Casting.md` governs (house vs role, course worlds, casting steps, ledger, six example casts). Figure Library = craft and tests.
- **Memory of mistakes:** `BUGS.md` (Codex adds rows), `FLIGHT-LOG.md` F-001…F-024. Enforced by `anatomy_check` (in check_all), `slop_lint` (backstage ban; ignores HTML comments), breakscan.
- **Desktop holds only Felipe + Mark.** Course material: `~/Documents/UFRGS 2026-2`.

## In flight (Codex; gate each at `needs-gate`)
- **S5 writing PAUSED (F-023)** until the prototype passes: **Controle Aula 08** revision (site #59). Gate it hard: slop_lint 0 hard, then READ against Aula 01; then its verdict goes to every other lesson PR (#52 A02, #53 A04, #54 A05, #55 A07, #60 A09, plus A03, A06, A30).
- **#17 CAST-1:** casting ledger + cast every in-flight figure redo before drawing.
- **#10 FIG-2:** kit PR #48 (clean) → #51 Delito U01 (clean) → #56/#57/#58 (conflicts; rebase). Contratos A01: approved the deliberate hero removal despite svgcheck. Gate by looking, against Visual Casting.
- **#11 CHG-1 (#47):** rebase; must keep the CHG-2 toggle.
- **#16 BIO-1:** professor bios data (Codex researches; CEO then briefs the pop-up).
- **#14 TBL-1**, **#12 PIPE-C** (S3 batches), **#15** blueprints A10–A13 to redo with the template.

## Next up (in order)
1. Gate whatever is `needs-gate`, Aula 08 first.
2. **Write master briefs (not code)** for: the class-register hover (whole-row affordance; inspiration rareui.com), the professor pop-up (after BIO-1 data), the hero rollout (once the chairman picks on `specimen/hero.html`; CEO recommends "Desenho à frente"), and the phone hero decision.
3. Write the remaining course-world pages for Visual Casting (drafts exist inside the doc) as the course redos come up.

## Quality findings and sources (30/09–01/10; why the pipeline exists)
- **Text:** Controle is genuinely weak: median lesson 1.25k words (other courses 2.7–3.8k); Aula 01 circles abstractions, promises an example it never gives, repeats its own summary, and ends with a "Fontes e limites" disclaimer (breaks the no-citations rule). Aula 24 is decent (concrete, statute-anchored). Contratos is equally thin (1.06k median). Cause: writers got slides plus scattered ad-hoc extracts, never per-lesson prepared sources.
- **Figures:** chairman: every Controle figure is at the level of the Aula 01 triangle, "completely unacceptable"; the Latam atlas plates are the bar. Fix = Visual Genres v2 "Instruments, not diagrams" + the same agent writes text and figures. **If Codex can't reach the bar in the ADC pilot, the chairman wants to evaluate plugins** (something launched at a dev day on 29/09; ask him for the link; don't guess).
- **Sources on disk:** Controle 7/8 base books + Lenza (AZW3) + new Gilmar Mendes *Aspectos* (a 146-pp SCAN: needs Tesseract) + ADC deck (`01 Slides/30 - ADC.pdf`) + Moodle ADI/ADC exercise list (`03 Moodle/2026-09-30 scrape/`). Contratos now has Venosa (17ª ed., 2016) and Caio Mário III (2014): both pre-Lei 13.874/2019 (arts. 421/421-A), so route post-2019 material from Gerson Branco's articles. Delito: Ilha da Silva skipped (not needed); Faccini's *Teoria Geral do Crime* not findable, so use his *Lições Introdutórias* (he's the professor). Still missing, low priority: Duque (Controle professor's book), Dirley da Cunha, Savigny, Couto e Silva, Martins-Costa (*Método da Concreção*). Const I has no plano on disk.
- **Existing extracts to reuse:** `work/book-extracts/` (+ `book-extract-map.md`), `work/controle-depth/extracts/`, `work/source-intake-2026-09-28/` (Metodologia, Processo, Const I intake on the same philosophy).

## Open decisions for the chairman
- Hero composition (`specimen/hero.html`) and whether the hero drawing shows on phones.

## Gotchas (hard-won; the full list is in `Relay Baton.md` → "Build-process lessons" and ~/.codex/AGENTS.md)
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
