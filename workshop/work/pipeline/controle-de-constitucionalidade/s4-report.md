# PIPE-4 S4 rebuild report

Word counts use whitespace splitting (`wc -w` style) on unique generated text files listed by each compendium index; `00-index.md` is excluded from content totals. Supporting subtotal counts files with the `30-` prefix. Baseline values were calculated from the original unmodified PIPE-4 state at `11f06cba182255be6f93b87f8a8cd61a6a25fdde`, before the rebuild.

| Median over 36 lessons | Before (words) | After (words) |
|---|---:|---:|
| All compendium content | 202,491.5 | 45,921.0 |
| Primary subtotal | 17,947.0 | 13,604.0 |
| Supporting subtotal | 169,233.0 | 885.0 |

## Aula 01 complete generated file list

Counts by filename role/prefix: `10`: 1, `20`: 5, `30`: 1, `50`: 1.

| File | Role | Words |
|---|---|---:|
| `10-slides.txt` | slides | 403 |
| `20-primary-001-lenza-esquematizado-2022-6.1.txt` | primary | 4,065 |
| `20-primary-002-mendes-branco-curso-2023-10-controle-de-constitucionalidade-01.txt` | primary | 661 |
| `20-primary-003-mendes-branco-curso-2023-10-controle-de-constitucionalidade-02.txt` | primary | 1,225 |
| `20-primary-004-mendes-branco-curso-2023-10-controle-de-constitucionalidade-04.txt` | primary | 588 |
| `20-primary-005-mendes-branco-curso-2023-10-controle-de-constitucionalidade-05.txt` | primary | 1,396 |
| `30-supporting-001-barroso-controle-2012-01.01.txt` | supporting | 885 |
| `50-exercises-and-exams.txt` | exercises/exams | 12 |

## Pull demonstration and checker

`pull_source.py aula-30 lei-9868-1999 "Art. 13, Art. 21" ...` appended two exact article files and two article-level provenance rows to Aula 30. The final Aula 30 compendium also carries the specific ADC article atoms: CF/88 `Art. 102`, `Art. 103`, and Lei 9.868 `Art. 13` through `Art. 28`; no whole-law atom is assigned.

Final check command: `python3 work/pipeline/tools/pipeline_check.py s4 controle-de-constitucionalidade`.
Output: `S4 PASS: 36/36 lesson manifests / 593 provenance rows`; Aulas 31–36 each emitted the permitted missing-slide WARN.
