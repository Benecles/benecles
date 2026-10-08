# PROC-R2 S3 essential-primary gap repair

## Context
The full S3 gate now maps `policy.basica_essencial_source_ids` exactly to `didier-curso-vol1-2017` and `marinoni-novo-curso-vol1-2017`, the two basic-essential citations in the course map. Six lessons have fewer than 5,000 directly matched primary words from those volumes. A nonessential assigned reading or other treatise may remain primary if it directly fits the lesson, but its words do not count toward the separate threshold.

## Inputs
- Master brief: `work/briefs/2026-10-06-processo-r2.md`.
- S3: `protocols/Source Pipeline.md`.
- Current `FLIGHT-LOG.md` S3 entries and `BUGS.md` S3 entries.
- `course-map.json`, `shelf.csv`, both essential-volume indexes under `chapters/`, the assigned lesson's checked `triage/parts/<slug>.csv`, and the merged `triage.csv`.

## Task
For your assigned lesson only, determine whether either basic-essential volume has a chapter that genuinely matches the mapped title, scope, syllabus, and outcome. Keep one treatise chapter as direct primary, after assigned reading; do not inflate primary coverage with loosely related material.

- If an essential chapter genuinely matches, change only the relevant row in your own `triage/parts/<slug>.csv` from `unused` to `primary`, with a concrete one-line rationale. If a different nonessential treatise chapter is currently primary, downgrade it to supporting only if the support caps remain valid; otherwise leave it primary and explain why. Preserve every other base row and the exact 1,276-key coverage.
- If neither essential book has a directly relevant chapter, leave your checked matrix unchanged and write one sentence to `work/pipeline/processo-civil-i/triage/thin-primary/<slug>.md`. Name both essential volumes considered and the assigned/nonessential source chapter that actually carries the mapped subject. Explain why 5,000 directly matched essential-primary words are unavailable. Do not describe missing sources or omissions unless the inspected indexes support it.

## Check and report
Run exactly one targeted check after your decision: confirm the lesson file still has one unique row per S2 key (1,276 total), exact lesson ID and valid roles/reasons; if you changed rows, recalculate this lesson's supporting totals. Do not run the global S3 gate. Report the output path, whether you changed the matrix or added a thin-primary sentence, and the check result.

Tokens are limited; spend them producing new work (features, lessons, content, pages). Each worker checks its own output exactly once (the project's lint/QA command, plus a source check for each new factual claim made while writing) and then moves on. Do not commission reviewers, editor passes, re-checks, audits of audits, or "independent verification" subagents unless Benecles explicitly asks.
