# ORDER boxy-detector

Token budget: 450000 tokens.

## Objective

Add the requested `boxy` detector to `R/gates/jank.mjs`, scan the seven live course trees, and queue one figure-only redraw order for every flagged figure that is not already owned by a pending staged change. This order is scanner and queue work only: do not edit lesson pages, and do not publish or push.

## Detector rule

Per panel, count labels whose centers fall inside rectangles, reusing the scanner's existing rectangle-host geometry. Flag `boxy` when at least three such labelled rectangles are connected by lines or paths and do not form an aligned grid. Treat a true grid as shared column x-edges and row y-edges, as in a decision table, form, or ledger. Add this as a failing finding in the normal `jank.mjs` behavior without suppressing existing findings.

Add focused synthetic fixtures to exercise: fewer than three labelled rectangles; three or more disconnected labelled rectangles; three or more connected rectangles forming a true grid; and three or more connected rectangles that do not form a grid. The last case must report `boxy`; the other cases must not.

## Scan and downstream orders

Scan the current published site read-only at `/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish` for all seven courses: `controle-de-constitucionalidade`, `teoria-geral-dos-contratos`, `direito-latino-americano`, `processo-civil-i`, `direito-constitucional-i`, `metodologia-juridica`, and `teoria-do-delito`. Write `R/program/boxy-scan.csv`, with one row per figure/panel and fields that identify the course, lesson page, figure selector or index, labelled-rectangle count, grid result, connector result, and `boxy` result. Record existing non-box jank separately; expected boxy findings may make normal course scans exit nonzero at this stage.

Before creating redraw orders, inspect current queue rows, active orders, ship approvals, and staged GATE `SHIPCOPY` maps. Do not create overlapping work for a figure already owned by an active, pending, approved, or staged order. Record every such exact overlap in `program/boxy-redraw-map.tsv`; every other `boxy=true` row must map to exactly one new redraw order. Group by course into chunks of at most six distinct lesson pages, with disjoint lesson ownership. Create self-contained `program/orders/boxy-redraw-<course>-<chunk>.md` briefs and append corresponding queue rows after `boxy-detector`; serialize chunks within each course and use a per-course lock. Each redraw brief must:

- redraw only its assigned flagged figures, following the applicable approved plan when one exists;
- enforce the NO BOXES rule: no text in rectangles joined by arrows or lines; only a true aligned grid may contain text in cells;
- preserve bytes outside figure blocks from an immutable current-live baseline;
- name its done-condition, token budget, and exact mechanical queue check;
- capture selector crops for the figures actually changed, identified by figure index or data attribute, never merely the first `<figure>` on a page;
- write its GATE note with exact changed paths, review crops, and ship map.

Implement `program/checks/check_boxy_scan.py` as the mechanical checker. It must verify the detector fixtures pass, the seven course names are represented in the CSV, every `boxy=true` row is either mapped once to a new queued redraw order or explicitly covered by an exact pending/staged owner, every generated chunk has no more than six lessons, and every generated queue row points to an existing self-contained order with a check command and token budget. Run it once after building the artifacts. The per-order queue check command is:

`python3 program/checks/check_boxy_scan.py`

## Done-condition

The normal jank scanner fails on the specified connected non-grid box pattern; all four fixtures distinguish the target pattern from the three non-target patterns; the read-only scan covers all seven current live courses and writes `R/program/boxy-scan.csv`; and every detected figure is covered by exactly one new queued redraw order or an exact active/staged owner, as verified by `program/checks/check_boxy_scan.py` exiting 0. No lesson page or publish checkout is edited by this scanner order.

## Gate handoff

Write `R/program/boxy-detector-GATE.md` (at most 50 lines) with the detection rule, synthetic-fixture result, seven-course scan summary, flagged-count summary, redraw coverage-map path, and exact output paths. State clearly that no lesson page changed. The checker must verify this GATE exists and reports the successful mechanical check.

## Mechanical queue check

`python3 program/checks/check_boxy_scan.py`

## Ship handling

This order changes program tooling and scan metadata only; leave site publish files untouched and do not create a site ship request. The downstream redraw orders use the ordinary gate and approved-ship pipeline.
