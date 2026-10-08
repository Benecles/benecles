# PROC-R2 S3 merge and dependency closure

## Inputs
- Read `work/pipeline/processo-civil-i/S3-brief.md`, the S3 section of `protocols/Source Pipeline.md`, current S3 `FLIGHT-LOG.md` rules, and the S3 entries in `BUGS.md`.
- Use the checked per-lesson files in `work/pipeline/processo-civil-i/triage/parts/` (22 files, one per course-map lesson).
- Read `course-map.json`, `shelf.csv`, and every S2 `chapters/*/index.json` for the canonical lesson IDs, prerequisites, and chapter keys.

## Output
Create `work/pipeline/processo-civil-i/triage.csv` with the exact columns `source_id,chapter_id,lesson_id,role,why`, and update only `thin_primary_reason` fields in `course-map.json` where a matching file exists in `triage/thin-primary/`. Preserve all base rows from the 22 checked files. Do not edit any part file or other artifact.

For every one-sentence file in `triage/thin-primary/<slug>.md`, set that lesson record's `thin_primary_reason` to the exact sentence; leave other lesson map fields untouched and preserve existing Aula 18 rationale. Each lesson file must contain exactly one base verdict (`primary`, `supporting`, or `unused`) for every indexed `(source_id, chapter_id)` key in S2, with the exact assigned lesson ID. Use all 1,276 S2 chapter entries. Stop and report if any part is missing, incomplete, has duplicates, or references unknown keys; do not silently repair another lesson's file.

Three source-gap notes are expected for Aula 06, Aula 14, and Aula 15; Aula 18 already has a course-map reason. Aula 01 and Aula 04 changed their checked base matrices to add directly matched basic-essential chapters; Aula 17 changed its matrix similarly. Rebuild `triage.csv` from the updated part files before dependency closure. After all base rows are validated and combined, add dependency-closure rows with role `background`: for each lesson, take every chapter assigned `primary` in each S0 prerequisite lesson. Add a background row for each such chapter, even if this lesson's base verdict for that chapter is `unused`; omit it only if this lesson's own base verdict is `primary` or `supporting`. Use a concise rationale such as `Carry-forward from <prerequisite lesson id>: <prerequisite reason>`. Preserve source and chapter IDs exactly. Do not change the base verdicts.

## One check and completion
Run exactly once after updating the map and writing the final `triage.csv`: `python3 work/pipeline/tools/pipeline_check.py s3 processo-civil-i`. This is the S3 stage gate; do not run it while the merged file is partial. If it fails, report the errors to the orchestrator with row IDs; do not make a second unplanned audit pass. Report the command, result, total rows, base rows, and background rows.

Tokens are limited; spend them producing new work (features, lessons, content, pages). Each worker checks its own output exactly once (the project's lint/QA command, plus a source check for each new factual claim made while writing) and then moves on. Do not commission reviewers, editor passes, re-checks, audits of audits, or "independent verification" subagents unless Benecles explicitly asks.
