# ORDER jank-ci-mj-r1

Redo generation 1 for `jank-ci-mj` after its approved ship request hit a publish-baseline conflict.
Token budget: 1200000.

## Exact failure and correction

`program/ships/conflicts/jank-ci-mj.md` reports live-baseline differences in Direito Constitucional I `assets/curso.css`, `aula-02.html`, `aula-13.html`, `aula-15-casos.html`, and `aula-20.html`, and in Metodologia Jurídica `assets/curso.css` and `aula-01.html`. The original order's scans passed, but the shipper correctly refused the stale baseline. Re-stage the same approved jank repairs on the current live baseline after the queued Metodologia curation build, `plates-2-r1`, and `d2-reframe-r2` have shipped. The Direito Constitucional I curation build `r2` failed at the final redo cap and is blocked; do not wait on an unpreparable ship request or merge its unapproved staged changes. Preserve its failed staged state as reference only. Preserve the frozen accepted copy at `program/ships/staged/jank-ci-mj/` as the source of the approved change; never replace current pages wholesale with it.

## Inputs and scope

- Conflict: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/conflicts/jank-ci-mj.md`
- Original order: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/orders/jank-ci-mj.md`
- Approved GATE: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/jank-ci-mj-GATE.md`
- Frozen approved copy: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/staged/jank-ci-mj/`
- Staging site: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site`
- Publish checkout is read-only: `/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish`
- Fresh GATE: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/jank-ci-mj-r1-GATE.md`

Refresh target pages from current live and snapshot fresh baselines under `program/ships/baselines/jank-ci-mj-r1/`; preserve old baselines and `program-old/jank-ci-mj/`. Preserve every current unshipped curation/plate change. Reapply only the original approved course-wide typography and page-specific label repairs; keep the five D2 plate SVG artworks untouched, retain meaning/wording, and preserve unrelated live edits. Compare non-figure bytes against the new live baselines, allowing only the exact changes made by the original approved order. Capture representative changed pages at desktop and phone, light and dark, and inspect the results.

Write a fresh ≤50-line GATE with exact changed paths, decisions, doubts, `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP` paths, and exact-file `SHIPCOPY` maps from the new baselines. Run both course-wide jank scans and the baseline-aware text checker. Request fresh approval through the normal ship pipeline; never write to or ship from the publish checkout.

Done-condition: the original approved jank repairs are re-staged on the current live baseline with no unrelated changes lost; both course-wide scans exit 0; the baseline-aware text check passes; and the fresh GATE has a complete exact ship map.

Mechanical queue check:

```sh
python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/checks/check_jank_ci_mj_r1.py && /Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course direito-constitucional-i --course metodologia-juridica --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/jank-ci-mj-r1.csv && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/jank-ci-mj-r1-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/jank-ci-mj-r1-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/jank-ci-mj-r1-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/jank-ci-mj-r1-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/jank-ci-mj-r1-GATE.md
```
