# S3 — lesson source triage

Branch: `codex/tgc-pipe-3`, stacked on S2 `188fce4`.

## Coverage

- `triage.csv` contains a base verdict and reason for each of the 100 indexed chapters against each of the 17 S0 lessons (1,700 chapter×lesson rows).
- It also carries 75 background rows: the exact union of primary chapters from each lesson's S0 prerequisites, except where a prerequisite chapter is already assigned directly to that lesson.
- `primary` assignments use the two available básica essencial books only. `supporting` material follows the ≤10,000-word item and ≤30,000-word lesson limits. No unavailable legal articles or newer book editions were supplied by model memory.
- Available slide decks are associated to lessons by their own topic headings in `shelf.csv`; Aulas 15–17 have explicit missing-source rows. Their absence is a warning, with no substitute deck assigned.

## Checks

The deliberate known-bad matrix, with one unused chapter×lesson cell removed, failed as required:

```text
FAIL: chapter ('BASE-PEREIRA-CAIO-MARIO-III', 'capitulo-xxxvii-part-02') has no lesson-specific verdict for aula-01.html
S3 FAIL: 1 error(s); 1774 triage rows / 100 chapters
```

Final check:

```text
python3 work/pipeline/tools/pipeline_check.py s3 teoria-geral-dos-contratos
WARN: aula-15.html: slide source explicitly marked missing in shelf (missing-slides-aula-15); no substitute assigned
WARN: aula-16.html: slide source explicitly marked missing in shelf (missing-slides-aula-16); no substitute assigned
WARN: aula-17.html: slide source explicitly marked missing in shelf (missing-slides-aula-17); no substitute assigned
S3 PASS: 1775 triage rows / 100 chapters
```

Other edition, statutory-extract, exam, and OCR limits remain in `triage-notes.md`.
