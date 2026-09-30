# ORDER fr-r1-r1

TOKEN BUDGET: 1000000 tokens.

## Why this redo exists

Claude's shipper rejected the baseline for the approved `fr-r1` request: eight live lesson pages differ from the old baselines, so nothing was copied to the publish checkout. Read `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/conflicts/fr-r1.md`, the still-pending request `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/pending/fr-r1.md`, and the original gate `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/fr-r1-GATE.md`.

This order is the authorized restage of that same work. The pending `fr-r1` request is the conflicted prior generation and cannot ship; do not wait for it to resolve. Use it and its gate as the exact change specification, rebase the intended figure-label geometry repairs onto current live pages, and let the runner prepare this generation (`fr-r1-r1`) as a fresh request after its check passes.

## Scope and current-live files

The conflict lists these eight pages:

- `courses/controle-de-constitucionalidade/aula-05.html`
- `courses/controle-de-constitucionalidade/aula-20.html`
- `courses/controle-de-constitucionalidade/aula-21.html`
- `courses/teoria-geral-dos-contratos/aula-06.html`
- `courses/teoria-geral-dos-contratos/aula-09.html`
- `courses/teoria-geral-dos-contratos/aula-11.html`
- `courses/teoria-geral-dos-contratos/aula-14.html`
- `courses/teoria-geral-dos-contratos/aula-16.html`

Preserve only the original approved FR figure-geometry changes on those pages. Keep wording, captions, lesson prose, questions, figure counts, panel counts, and unrelated current-live edits unchanged. Do not change the four course stylesheets or any other page. Never write to the publish checkout.

Follow `program/preamble.md`: inspect other pending ship maps for overlapping ownership; preserve an unshipped staged owner's work if one owns a target; otherwise refresh the target from the current published file and snapshot that live file as an immutable baseline before applying the FR change. The old pending `fr-r1` copyset is this order's own previous output, not an independent staged owner. Preserve it for diffing, then create new snapshots under `relay-design-2026-09-29/program-old/fr-r1-r1/` and current-live baselines under `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/fr-r1-r1-current-live/`; never overwrite prior baselines.

The original check also compares staged text against validation snapshots in `fr/old/`. Preserve its prior snapshots under the new order's `program-old/fr-r1-r1/text-baseline/`, refresh the comparison inputs from the order-start staged state without changing unowned staged pages, then rerun the same all-course text check.

## Done-condition

All four course scans report zero janky rows; `fr/check_text.py` reports zero problems; only the eight approved target pages carry the re-staged geometry repair; and `relay-design-2026-09-29/program/fr-r1-r1-GATE.md` (50 lines maximum) records exact changed paths, staging URLs, remaining doubts, `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP` paths, and exact-file `SHIPCOPY` entries using the immutable current-live baselines. The runner can then prepare this fresh request; do not approve, commit, push, or ship it yourself.

## Mechanical queue check command

```sh
/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course controle-de-constitucionalidade --course teoria-geral-dos-contratos --course direito-latino-americano --course processo-civil-i --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/fr-r1-r1-jank.csv && python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/fr/check_text.py controle-de-constitucionalidade teoria-geral-dos-contratos direito-latino-americano processo-civil-i && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/fr-r1-r1-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/fr-r1-r1-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/fr-r1-r1-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/fr-r1-r1-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/fr-r1-r1-GATE.md
```
