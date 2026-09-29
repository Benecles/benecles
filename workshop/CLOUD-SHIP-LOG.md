# Cloud ship log (atomic cycles, 2026-09-29)

One line per shipped step: what changed, the study-lab commit on `main`, and where the source lives. Each step is built, QA'd, merged to `main` (live) and logged before the next starts. If the cloud session stops mid-cycle, the last line here is the last thing that is live.

| # | Step | Live commit | Notes |
|---|---|---|---|
| 1 | PC Aula 07: calendar scrolly for the 2025 P1 deadline count | `6030351` | PR #5; figs.py fig_pc07; build.py figure hook |
| 2 | Home: patch notes section 'O que mudou' (24/09 to 29/09); stale empty-card text fixed | `9e01738` | PR #6; edit between PATCHNOTES markers in index.html; add a line per future ship |
| 3 | Home: own drawings on the three new course cards; patch note; baton pins (stale schematics, Controle granularity) | `72f7003` | PR #7 |
