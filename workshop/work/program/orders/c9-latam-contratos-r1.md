# ORDER c9-latam-contratos-r1

Redo generation 1 for `c9-latam-contratos` after its approved ship request hit a publish-baseline conflict.
Token budget: 900000.

## Exact failure and correction

`program/ships/conflicts/c9-latam-contratos.md` says the published Latam lesson pages `aula-01.html` through `aula-09.html` and Contratos `aula-01.html` differ from the old immutable baseline. The approved C9 changes are still in the archived request and `program/ships/staged/c9-latam-contratos/`. Re-stage those exact changes on the current live baseline after `fr-r1-r1` and `plates-2-r1` ship. The final permitted Latam curation generation (`curation-build-direito-latino-americano-r2` plus `r2b`) failed its queue check in chunk 1 and is blocked; neither chunk has a passing GATE or pending ship request. Preserve the partial staging under `program-old` without overwriting existing copies, but do not merge its unapproved figure edits into this C9 restage. Refresh all ten C9 targets from current live and reapply only the approved C9 edits, preserving intervening live changes.

## Inputs and scope

- Conflict: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/conflicts/c9-latam-contratos.md`
- Original approved order: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/orders/c9-latam-contratos.md`
- Approved change reference: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/c9-latam-contratos-GATE.md`
- Frozen accepted copy: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/staged/c9-latam-contratos/`
- Live publish checkout is read-only to this order: `/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish`
- Staging: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site`
- Fresh GATE: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/c9-latam-contratos-r1-GATE.md`

Retain the nine already approved Latam bet rewrites and the two `00 · O curso` introductions (Latam and Contratos). Do not add new content or alter the approved wording. Preserve all existing `program-old/c9-latam-contratos/` copies and old baselines; create new r1 pre-edit copies and immutable baselines from the current live files under `program-old/c9-latam-contratos-r1/` and `program/ships/baselines/c9-latam-contratos-r1/`. Refresh each target from current live only after confirming no other unshipped request owns it.

Run `slop_lint.py` for each of the ten changed pages, capture the changed pages in desktop/phone and light/dark, inspect the capture results, and run the relevant geometry and jank gates. The old GATE reports 17px phone overflow on four Latam pages with no visible clipping; preserve this as a stated doubt unless the exact C9 text reapplication itself changes it. Write a fresh ≤50-line GATE with exact paths, URLs, judgments, `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP` paths, and exact-file `SHIPCOPY` maps rooted in the new live baselines. Request fresh approval through the normal ship pipeline; do not write to or ship from the publish checkout.

Done-condition: the ten approved C9 page changes are re-staged on the current live baseline with unrelated live changes preserved; all ten pages pass slop lint; the geometry/jank checks pass or retain the documented unchanged overflow doubt; and the new GATE carries a complete exact ship map.

Mechanical queue check:

```sh
python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/checks/check_c9-latam-contratos-r1.py && /Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course direito-latino-americano --course teoria-geral-dos-contratos --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/c9-latam-contratos-r1-jank.csv && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/c9-latam-contratos-r1-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/c9-latam-contratos-r1-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/c9-latam-contratos-r1-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/c9-latam-contratos-r1-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/c9-latam-contratos-r1-GATE.md
```
