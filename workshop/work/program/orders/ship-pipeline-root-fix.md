# ORDER ship-pipeline-root-fix

Token budget: 220000.

Claude added this explicit machine-maintenance request to `program/claude-requests.md` after the `c9-latam-contratos` and `jank-ci-mj` ship conflicts:

- Every new order must re-stage its target pages from the current publish checkout and take fresh immutable baselines, unless those paths belong to an unshipped staged order.
- The shipper must never copy non-site files into the publish checkout. Curation plans were copied under `curation/` and left it dirty.
- iCloud `Resource deadlock avoided` reads should retry after `brctl download <file>` instead of failing the ship.

## Work

1. Update `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/preamble.md` with a concrete pre-edit procedure for every future page order: identify exact existing publishable targets from the order and approved plan; check pending ship requests/GATE `SHIPCOPY` maps for an unshipped owner of each path; preserve and wait for overlapping staged changes instead of overwriting them; otherwise copy the current published file into staging and take an immutable order-specific baseline from that same current file. Never overwrite an existing baseline. If work must overlap, explicitly merge only the ordered change with the unshipped change and preserve unrelated live edits.
2. Update `program/ships/shipper.py` so its `SHIPCOPY` validation accepts only actual site content and refuses non-site roots/files such as `curation/`. Keep the existing rule that only `ships/approved/` requests can ship. Curation plans remain staged artifacts, never publish-checkout content.
3. Make ship attempts resilient to iCloud `OSError` errno 11: identify the exact file, run `brctl download <file>`, then retry a bounded number of times. Make a ship attempt transactional: if validation/build/polish fails after any copy, restore only files touched by that request to their pre-attempt bytes and leave every unrelated publish edit intact. Never use a whole-checkout reset. Do not clear baseline conflicts; the c9 and jank restages have their own queued orders.
4. Recover only pipeline state this failure created. Preserve `ships/done/curation-plan-2.not-a-ship`: the curation plan is staging-only, not a publish request. Remove accidental `curation/` files from the publish checkout only when the archived request copyset and repository history prove that the failed ship attempt introduced those exact uncommitted files; preserve all other changes. For transient `Resource deadlock avoided` errors on still-approved site requests, let the repaired watcher retry only after the publish checkout is clean and all baseline checks pass. Keep `ships/INDEX.md` at one line per request and refresh the inbox with the gate paths for anything still awaiting Claude.
5. Add `program/checks/check_ship_pipeline.py`. It must exercise, without writing to the real publish checkout, rejection of a non-site curation copyset, acceptance of a site copyset, the bounded `brctl download` retry path using a stub, and rollback of only request-owned files after a simulated ship failure.

Do not publish, commit, or push anything in this order. The watcher remains the only shipper.

Done-condition: the common preamble requires a current-live refresh and protected baseline for future page orders; the shipper rejects non-site files, retries errno 11 through `brctl download`, and rolls back only its own partial copies; the curation-plan request remains staging-only; the new checker passes; and the request index has one line per request.

Mechanical queue check:

```sh
bash -n /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/runner.sh && python3 -m py_compile /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/shipper.py && python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/checks/check_ship_pipeline.py
```
