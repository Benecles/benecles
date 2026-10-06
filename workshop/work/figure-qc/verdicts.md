# Figure QC, 01/10 (CEO)

All 784 live figures, collapsed to 400 distinct figures (scrolly steps grouped), judged against `protocols/Figure Library.md`. Ids are VIS-2 catalogue ids (`work/vis-catalog/catalog.csv` on the site repo's `codex/vis-2` branch); `+N` means the following N steps of the same scrolly figure. **Rule: whatever isn't listed as keep or acceptable in a course is a redo.**

## Opening strips (decided once, not per page)
- **Keep as navigation:** Processo (stage of the procedure), Delito (step of the cascade), Const I and Metodologia (point in history). Each repeats one strip with the current lesson lit. It's meaningful, cheap and consistent.
- **Remove:** one-off doodle heroes. That means every Controle hero (triangles, rulers-without-rule, wavy lines), the Contratos one-offs and the thin Latam route lines. The title and lede stand alone. A hero comes back only when it passes the library test.

## Keep (exemplar level)
- **Latam:** dla-a01-s1, dla-a01-s3+3, dla-a02-s7+1, dla-a03-s5 (tally), dla-a03-s6+1, dla-a05-s3+3, dla-a06-s3+2, dla-index-s2
- **Metodologia:** met-a01-s2, met-a01-s3, met-a01-s4 (glossed page), met-a01-s5 and every Atlantic map step, met-index-s1
- **Processo:** pci-a07-s2+2 (calendar)
- **Fronts:** ctl-index-s1, tdl-index-s1, tgc-index-s1

## Acceptable (passes the test, not exemplary)
- **Latam:** dla-a01-s13+2 (strata), dla-a09-s2+1, dla-a09-s4+1 (decision paths)
- **Processo:** pci-a05-s2+2, pci-a05-s3+3, pci-a06-citacao-s2, pci-a06-citacao-s3+1, pci-a09-s2+2 (decision paths with legal exits); pci-a01-s2 (the petição form); pci-a08-s2+2 (the contestação form)
- **Const I:** dci-a02-s2+1 (classification grid), dci-a03-republica-s2+1 and dci-a03-s2+1 (constitutions as strata)
- **Delito:** the cascade (tdl-u01-s2+4, tdl-u01-casos-s2+4 and its copies on other units), tdl-u01-s8, tdl-u14 ficha de imputação, tdl-u15 folha de decisão, tdl-s16-s2+3
- **Contratos:** tgc-a05-s7+3 (the retratação race: letters in transit), tgc-a05-s5+1, tgc-a08-s5+3 (performance timeline), tgc-a04-s2+3, tgc-a09-s2+3
- **Controle (seeds for the pipeline rebuild):** ctl-a05-s7+1 (CF vs Pacto statute excerpts), ctl-a11-s6, ctl-a11-s9

## Redo, by course (what fails, and the genre to rebuild in)
| Course | Distinct figures | Redo (approx.) | Dominant failure | Rebuild genres |
|---|---|---|---|---|
| Controle | 121 | ~115 | triangles, sentences in boxes, the black shield (ctl-a03-s13) | goes through the Source Pipeline: ruler, statute cut, who-decides matrix, docket |
| Contratos | 81 | ~65 | tables of text (a05-s4, a06-s7, a06-s11, a06-s12, a08-s9…s15), sparse two-node sketches | document anatomy (the contract itself, its clauses), timeline, tally |
| Delito | 79 | ~45 | text boxes (u03, u05, s17–s20); single box on a canvas (s20-s2) | decision path, **scale** (u04-s2 degrees of dolo is literally a ruler), case file |
| Latam | 29 | ~10 | "livro-razão" ledgers that are empty tables (a01-s7, a02-s3, a03-s3, a04-s2, a08-s6) | tally, timeline, map |
| Processo | 30 | ~6 | sentences in boxes (a01-s2, a02-s2, a04-s2, a10-s2) | calendar, document anatomy, decision path |
| Const I | 43 (38 are strips) | ~2 | a04-s2 boxes | strata, statute cut |
| Metodologia | 17 | ~3 | big-text decision panels (a04-s4, a05-s1, a15-s1) | document anatomy, map |

**Order:** Controle through the pipeline (in progress). Then Contratos (worst ratio, books on disk), then the Delito redos. Every rebuild is generated from `tools/figkit/` genre components, and a genre without a component gets one first.
