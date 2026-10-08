# ORDER ship-output-artifacts

TOKEN BUDGET: 60000 tokens.

## Agreed request

`program/claude-requests.md` reports that `program/ships/shipper.py` leaves generated publish-checkout output dirty after CSS-related ships: `assetver` query restamps across pages in the affected course, `offline-manifest.json`, and `tools/polish/*.json`. This was seen during c9 and jank-ci-mj shipping. Include generated output in the same ship commit and verify the publish checkout is clean before archiving.

## Scope

Tooling only. Read `program/ships/shipper.py`, `program/checks/check_ship_pipeline.py`, and the relevant ship logs. Adjust shipper staging/commit behavior so every generated output caused by the current ship is committed with that ship, including all affected `assetver` restamps, `offline-manifest.json`, and generated `tools/polish/*.json`. Determine the exact generated paths from the isolated build result; do not stage unrelated pre-existing user changes.

After the commit, inspect `git status --porcelain` and archive the request only when the publish checkout is clean. If unrelated changes remain, fail safely with a useful error and leave the request unarchived. Preserve the root-fix rule that `SHIPCOPY` maps contain site files only; this order concerns build outputs generated inside the publish checkout and does not authorize copying non-site source files such as curation plans.

Extend `program/checks/check_ship_pipeline.py` with isolated temporary-checkout coverage that simulates a CSS ship and asserts that the generated files above are part of the same ship commit, unrelated dirty files are not committed, and the checkout is clean before archiving. Tests must not commit or push to the real publish checkout. Keep the change staging-only; do not write to site pages or create a ship approval request.

## Done-condition

The shipper includes all ship-generated output in the ship commit, refuses to archive when unrelated dirty files remain, and the isolated pipeline checker passes those cases without touching the real publish checkout.

## Mechanical queue check

```sh
python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/checks/check_ship_pipeline.py
```
