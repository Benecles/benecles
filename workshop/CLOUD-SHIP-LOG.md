# Cloud ship log (atomic cycles, 2026-09-29)

One line per shipped step: what changed, the study-lab commit on `main`, and where the source lives. Each step is built, QA'd, merged to `main` (live) and logged before the next starts. If the cloud session stops mid-cycle, the last line here is the last thing that is live.

| # | Step | Live commit | Notes |
|---|---|---|---|
| 1 | PC Aula 07: calendar scrolly for the 2025 P1 deadline count | `6030351` | PR #5; figs.py fig_pc07; build.py figure hook |
| 2 | Home: patch notes section 'O que mudou' (24/09 to 29/09); stale empty-card text fixed | `9e01738` | PR #6; edit between PATCHNOTES markers in index.html; add a line per future ship |
| 3 | Home: own drawings on the three new course cards; patch note; baton pins (stale schematics, Controle granularity) | `72f7003` | PR #7 |
| 4 | CI Aula 04: genealogy scrolly of review models (US, Austria, Brazil) | `c291d18` | PR #8; figs.py fig_ci04 |
| 5 | Home patch notes itemized: every added lesson linked by day; baton pin: blog idea | `f9115b3` | PR #9; lists rebuilt from each course index order |
| 6 | PC Aula 03: litisconsórcio matrix scrolly | `e00848f` | PR #10; figs.py fig_pc03. Session ends here: next figures for the Mac (see baton) |
| 7 | CI: wrong professor name removed from front and home card; CI 02 figure held (pinned) | `a067d57` | PR #11 |
| 7 | CI: wrong professor name removed; CI 02 figure held (pinned) | `a067d57` | PR #11 |
