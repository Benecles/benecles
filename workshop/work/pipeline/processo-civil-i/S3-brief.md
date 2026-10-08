# PROC-R2 S3 lesson triage: worker protocol

## Inputs and rules
- Master: `work/briefs/2026-10-06-processo-r2.md` (read S3 and the course's evaluation/syllabus scope).
- Pipeline: `protocols/Source Pipeline.md` (read S3 in full).
- Course map: `work/pipeline/processo-civil-i/course-map.json` and `.md`.
- Source shelf: `work/pipeline/processo-civil-i/shelf.csv`.
- S2 catalog: `work/pipeline/processo-civil-i/chapters/*/index.json` (all 40 available source indexes and 1,276 indexed chapter entries at the passed S2 gate; open source text only as needed to disambiguate a chapter title or assigned reading).
- Read current `FLIGHT-LOG.md` S3 rules and search `BUGS.md` for relevant existing symptoms before changing anything.

## Goal
For your one assigned lesson, produce a complete base-verdict matrix over **every** indexed S2 chapter, exactly one row per indexed chapter entry (currently 1,276 entries). Select narrowly: assigned readings first, then at most one relevant, bounded treatise chapter as the lesson's primary book source. Never assign an entire book to a lesson. Every chapter must be `primary`, `supporting`, or `unused` for this lesson, with one concrete line of reason. Be conservative: a near-match is unused. The reasons are internal triage data, not reader-facing prose.

Do not emit `background` rows. After all base matrices land, the orchestrator will derive those mechanically from the prerequisite lessons' primary rows in S0, omitting a chapter where the receiving lesson already has a direct primary or supporting assignment. Do not emit `no_book_covers`; the course has books.

## Role rules
- `primary`: the lesson's assigned reading material and/or its one narrowly relevant treatise chapter; mapped lecture slides may be primary only when the S1 row explicitly maps them to this lesson. Primary rationale must connect the source to this lesson's topic/outcome. Any direct-fit primary source may be assigned primary; only rows whose source ID resolves to a basic-essential book count toward the separate 5,000-word threshold, so a lesson with thin essential coverage may need a concrete lesson-level `thin_primary_reason`. For book chapters, avoid selecting multiple treatise chapters as primary simply to meet a word target. If basic-essential primary coverage is thin, explain the real source gap in your handoff; never stretch an irrelevant chapter.
- `supporting`: directly useful but not the assigned reading or selected treatise primary. Supporting units must be ≤10,000 words each and ≤30,000 words total for this lesson; an over-10,000-word unit is allowed only when `why` includes a concrete clause beginning `Specific need:`. Do not use peer notes as legal authority; mark only genuinely useful study context as supporting.
- `unused`: the chapter does not directly feed this lesson. Give a brief, specific rationale (e.g., it covers another stage/topic, a different lesson's assigned reading, or unrelated administrative/exam material). Avoid empty boilerplate and do not mark course-wide references unused if a real connection is clear.
- Preserve S2 chapter IDs and source IDs exactly. Use the S1 shelf role/title and S0 lesson map to distinguish treatises, assigned reading, slides, statutes, exams, and guidance.
- For a multi-lesson item, classify its fit for this one lesson only. If direct fit is uncertain, unused.

## Output contract
Write only your assigned file: `work/pipeline/processo-civil-i/triage/parts/<LESSON_SLUG>.csv`, where `<LESSON_SLUG>` is the exact lesson ID with `.html` removed and any remaining path separators replaced by `-`.
CSV header, exactly: `source_id,chapter_id,lesson_id,role,why`
Use one row for every `(source_id, chapter_id)` in the full S2 catalog, each with this lesson ID and role `primary`, `supporting`, or `unused`. Preserve UTF-8 and use a CSV writer (proper quoting for commas/newlines); keep each `why` to one line. No other output file may be changed.

## One check and completion
Check your own output exactly once: mechanically compare its chapter-key set with all `chapters` entries from the S2 indexes; assert every key occurs once, every row has the assigned lesson ID and a valid role/reason, and totals respect the supporting caps (including `Specific need:` when required). Then report the exact output path, chapter row count, primary chapter/source choices, supporting word total, and whether a `thin_primary_reason` may be necessary. Do not run the full course S3 check, review another worker's output, or make other workers' changes.

Tokens are limited; spend them producing new work (features, lessons, content, pages). Each worker checks its own output exactly once (the project's lint/QA command, plus a source check for each new factual claim made while writing) and then moves on. Do not commission reviewers, editor passes, re-checks, audits of audits, or "independent verification" subagents unless Benecles explicitly asks.
