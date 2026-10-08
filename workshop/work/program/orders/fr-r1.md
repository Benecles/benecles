ORDER fr-r1 — finish the agreed four-course figure-jank work
TOKEN BUDGET: 1,000,000 tokens.

Why this order exists
The agreed site-wide FR repair is marked done, but its gate is explicitly not clean: `relay-design-2026-09-29/fr/GATE.md` reports 58 janky panel rows across seven pages after scanning 886 rows. The exact residual scan is `relay-design-2026-09-29/fr/scan-final.csv`. The listed failures are Controle aulas 05, 20, and 21; Contratos aulas 06, 09, 14, and 16. Latam and Processo Civil I passed that scan. `plates-2` is still editing staging, including Latam aula 01, so begin only after the queue says `plates-2` is done and include any new jank it introduces in the final four-course scan.

Scope and constraints
- Repair only measured label geometry: collisions, spills, outside labels, tiny labels, and any newly introduced jank. Preserve figure meaning, labels, wording, captions, lesson prose, questions, and figure counts as they stand when this order begins. Do not add or delete figures or invent content.
- Work from the current staged site; keep earlier changes. Before editing, preserve each target file under `relay-design-2026-09-29/program-old/fr-r1/` without overwriting an existing backup. Do not touch the publish checkout.
- Split implementation across two disjoint course workers: Controle aulas 05/20/21 plus its course CSS; Contratos aulas 06/09/14/16 plus its course CSS. Each worker owns only its course folder and self-checks its work once. Paste the BUILD-DON'T-AUDIT paragraph from `~/.codex/AGENTS.md` verbatim into each worker brief. Handle any newly janky Latam/Processo row in a separate disjoint assignment only if the post-`plates-2` scan identifies one.
- Make only figure-local layout changes needed for the scanner: sizing, placement, wrapping, spacing, or responsive geometry. Preserve the current typography baseline where it already passes. No general review or unrelated polish.

Done-condition
The queue check below exits 0: all four courses have zero janky rows and `fr/check_text.py` reports zero problems. Write `relay-design-2026-09-29/program/fr-r1-GATE.md` (≤50 lines) with changed paths, staging URLs, exact remaining doubts, and `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 `SHIPCROP`, and exact-file `SHIPCOPY` lines. Baseline copies must reflect the pre-edit staged state under `program-old/fr-r1`; include only changed live files in the ship map. Add a dated top entry to the Live work log with `python3 relay-design-2026-09-29/milestone.py <file>`.

Mechanical queue check (run from `/Users/benecles/Documents/Codex/2026-09-23/you-h/work`):
```sh
/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course controle-de-constitucionalidade --course teoria-geral-dos-contratos --course direito-latino-americano --course processo-civil-i --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/fr-r1-jank.csv && python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/fr/check_text.py controle-de-constitucionalidade teoria-geral-dos-contratos direito-latino-americano processo-civil-i
```
