# Known bugs: symptom → cause → fix → what catches it now

Search this file by what you SEE before you debug anything. Every agent (Claude, Codex orchestrators, Luna workers) adds a row the moment they fix a bug that isn't here. One row per bug. Write the symptom the way the next agent will notice it, not the way you diagnosed it. Rules that came out of a bug also go in `FLIGHT-LOG.md`; this file keeps the diagnosis and the fix.

"Catches it" names the check that now fails on the bug. A bug with no check says **none**: be extra careful there, and add a check when you can make one fail on the bad state first.

## Layout and CSS

| Symptom | Cause | Fix | Catches it | Seen |
|---|---|---|---|---|
| Prose hugs the left edge of a wide screen (x = 0) while headings sit centred | `<div class="prosa">` placed directly in `<body>`; house prose lives inside `.wide` | Wrap in `<div class="wide">`; prose then aligns with the chapter heading | `anatomy_check` LOOSE-PROSA (in `check_all`) | Controle 01, 01/10 |
| Table row labels stack one letter per line on phones ("QU / EM / CO…") | `overflow-wrap:anywhere` on `.compare th` lets an auto-width column shrink to one character | `.compare tbody th,.compare thead th:first-child{overflow-wrap:normal;hyphens:manual}` (done in `controle.css`) | none (look at 375 px); other six courses → workshop #14 | Controle 01/03, 01/10 |
| CSS edit has no effect in the preview | Stylesheet is pinned by `?v=<hash>`; browser serves the cached file | Run `assetver` (or `offline_build.py`), reload with a new `?r=N` | n/a | often |
| Every figure label forced to 14 px, exact layouts broken | Blanket `svg.fig text{font-size:14px!important}` from 30/09 | Kit SVGs carry `.figkit`; rule is `svg.fig:not(.figkit) text` | review: never add blanket label CSS | FIG-1, 01/10 |
| `offline_build.py` changes `assets/front.css` and `specimen/register.html` | Known debt: it appends the landscape rule / offline script to files it shouldn't | `git checkout -- assets/front.css specimen/register.html` after every run | none | since 30/09 |

## Figures

| Symptom | Cause | Fix | Catches it | Seen |
|---|---|---|---|---|
| Figure frame much bigger than the drawing; half the box is blank; labels tiny | Kit panel left on the default `0 0 600 600` viewBox, drawing in the top half; stage forced a square | Crop viewBox to the drawing + ~16 units; one-panel scrolly takes the drawing's proportions (`controle.css`) | `anatomy_check` SQUARE-KIT | Controle 01, 01/10 |
| A figure fades in a second late, or stays invisible | Its panel lacks class `on`; it waits for the scroll observer | Give the only panel of a one-step scrolly `class="… on"` | `anatomy_check` LATE-PANEL | Controle 01 Figs. 2–3, 01/10 |
| Corners of a figure empty even after cropping (T or L shape) | Composition, not framing: the bounding box is tight but the arms are empty | Put legend / verdict / second object in the empty arms, or recompose | none yet (4×4 grid rule, Figure Library test 4) | chairman, 01/10 |
| Labels collide after shrinking a drawing to make type bigger | Ruler narrowed 520 → 420 units: stops 84 units apart, "autorização" × "proibição" | Keep widths the kit gate passed; get size from cropping or simplifying, then re-probe | breakscan CLASH / CROSS | Controle 01, 01/10 |
| Breakscan says clean while a figure is visibly broken | It measured fallback fonts and local SVG boxes, missing transformed text overlap, viewBox clipping, hidden panel steps, and phone overflow | Wait for `document.fonts.ready`; compare rendered screen boxes at both widths in every `data-panel` step; report CLASH, CLIP, and OVERFLOW | breakscan fails on #65, #58, and Latam 08/09; live Controle 01 is the positive case | BRK-1, 04/10 |
| Two-line labels overlap; a limit line cuts a title band | Leading under 14 px (mono) / 18 px (serif); line drawn through text band | Kit leading minimums; lines skip text bands | breakscan / specimen probe 0 CROSS 0 CLASH | FIG-1, 01/10 |
| SVG files grew +83 KB with no visible change | SVGs re-serialized through the DOM (`<path/>` → `<path></path>`) | Patch attributes in place; text outside SVGs byte-identical | `work/checks/gate_prs.sh` (svgcheck) | LBL-1, 01/10 |
| A stroke animation stops short of the end | Path longer than its `stroke-dasharray` | Set dasharray ≥ path length | breakscan SHORT | 30/09 |
| A chart's numbers don't add up | Source data failed its own arithmetic (7,714 ≠ 7,632 + 83) | Check sums before drawing; never chart failing data | none | Controle 27, 01/10 |

## Content and pages

| Symptom | Cause | Fix | Catches it | Seen |
|---|---|---|---|---|
| Hero says one reading time, the course front's clock another | Hero hand-written; front computes `max(5, round(words/WPM/5)*5)` | After a rewrite, set the hero's "Leitura" to the regenerated front clock | `check_all` front diff (shows the clock change) | Controle 01, 01/10 |
| Live word count drops after a template swap | New template silently dropped content (lesson descriptions) | Compare per-page word counts old vs new before shipping | `work/usage/ledger.py` | D1, 29/09 |
| Regenerating a page reverted hand edits | Generator stale vs live; polish layer not applied | Diff generator output vs live first; record hand edits with `polish.py capture` | `polish.py check` | Delito s17, 29/09 |
| "unlocatable edits" from `polish.py check` on lesson pages | 67 old pre-existing records | Old debt, not new breakage; only new ones matter | `polish.py check` | 30/09 |

## Tooling and shell

| Symptom | Cause | Fix | Catches it | Seen |
|---|---|---|---|---|
| `check_all` FAILs on the front right after your own edit | It compares regenerated fronts against the git INDEX | `git add` your edits, then run it | n/a | 01/10 |
| `check_all` treats `professors.json` as a course front and reports a missing `professors.html` shell | Front enumeration treated every JSON file under `tools/fronts/data/` as a course slug | Select course-front records by their object schema (`course` key), allowing list datasets to coexist | `check_all` course-front enumeration | BIO-1, 03/10 |
| A push in a loop silently went nowhere | zsh parses `"$k:codex"` as `$k` + `:c` modifier | Brace it: `"${k}:codex"` | none | 30/09 (5 pushes) |
| `pkill -f <pattern>` killed your own shell/runner | Pattern matches the calling command line | Kill by pid | none | 30/09 |
| Background reads hang / `Errno 11 Resource deadlock avoided` | iCloud evicted files (disk full) | Free space, `brctl download`; work now lives in `~/Developer` | n/a | 30/09 |
| Your commit landed on a `codex/*` branch (or a pull says "commit or stash") | Codex switched the shared workshop checkout to its own branch | `git status -sb` before every commit; if wrong, cherry-pick onto `main` and `git push --force-with-lease origin <prev>:<codex-branch>` | none | 01/10 (Claude, F-019 commit) |
| `No such file` for a path under `~/Desktop/UFRGS 2026-2` (or Desktop dossiers, Arbitration Material, CUFRGS, Relay Baton, Scans) | Moved 02/10: Desktop holds only Felipe + Mark (chairman). Course material is in `~/Documents/UFRGS 2026-2` | `python3 protocols/tools/rewrite_paths.py work/moves/2026-10-02-desktop.json <your files> --include-git` | none | 02/10 |
| A Luna worker replied "done" but no file exists | Workers can claim done without acting | Every brief has a script-checked done-condition | the brief's check script | 29/09 |
| A check passes on something visibly worse | The check never tested that failure | Run every new check against the known-bad state first | n/a | D2, 30/09 |
| A tool-branch catalogue landed in the site repo | Workshop artifact committed to `ordenacoes-filipinas` | Workshop artifacts go in the workshop repo; site gets reader files + `tools/` | review | VIS-2, 01/10 |

## Source Pipeline

| Symptom | Cause | Fix | Catches it | Seen |
|---|---|---|---|---|
| S0 passes a nine-page Latam map that leaves the live review outside the pipeline | S0 enumerated only `aula-*.html`; `revisao-atividade.html` was treated as auxiliary | Include a live `revisao-atividade.html` in required S0 pages and map its syllabus/class links, function and prerequisites in `lessons` | `pipeline_check.py s0`: nine-page map fails with the missing review; ten-page map passes | Latam S0, 04/10 |
