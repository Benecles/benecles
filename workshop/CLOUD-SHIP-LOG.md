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
| 8 | CI: professor Vivian Caminha on front and home card | `ac3f638` | PR #12 |
| 9 | PARTIAL, not live: CI Aula 02 classification-ledger figure (fig_ci02) | — | Switched off in figs.py: at 390 px the page overflows to 405 px in 2 of 4 QA runs (light and dark). Not the SVG; check the scrolly stage/figcaption on phone, then re-enable and ship. |
| 9b | Diagnosis for step 9 (not live) | — | At 390 px the scrolly's `<figure>` has scrollWidth 358 vs clientWidth 356 and the page grows to 432 px; the SVG is fine. Likely cause: the figcaption (title + '1 / 2') does not wrap. Fix: shorter title in fig_ci02 ('Os eixos da classificação') or let `.stage figcaption` wrap on phones; then re-enable the FIGS line and QA. |
