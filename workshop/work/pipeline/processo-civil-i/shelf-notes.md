# S1 shelf notes — Processo Civil I

## Inventory

`shelf.csv` has 42 canonical rows: 40 physical files and two explicit missing-source rows (Cintra cap. 10; standalone Moodle exercise list). It covers the six books in `Livros/`, assigned readings and Moodle supplements, the syllabus and CPC capture, six Moodle model images, five detached Moodle exports, all eight exam PDFs, four peer-note PDFs, and the 28-question intake extract. `source_id` and `source_role` are stable fields; `role` is retained for the current S1 checker. Exact byte duplicates are grouped as `aliases` after SHA-256 calculation. The Moodle model scans include legacy/Obsidian duplicates; the Costa and Passos slide PDFs are exact aliases of their Moodle readings. No originals were moved or changed.

The five `_A classificar/.../Detached Moodle exports/` files remain in place and are each represented as an HTML (`.php`) row. The HTML pages are content-linked to AR, certidão de NE, edital, mandado cumprido, and mandado não cumprido image sources; they include saved Moodle page structure and are not byte duplicates of those images. The semester schedule's Moodle copy is noted alongside the authoritative Anotações copy; the syllabus map records the header-layout difference.

No standalone Moodle exercise-list file was found in the inspected dated, legacy, or Obsidian course inventories. The separate 28/09 intake `batches/exams/questions.csv` is included as a derived starting point, not as authority; it has 28 questions extracted from three older exams.

## Reuse and OCR

- Reused the local 28/09 Passos OCR at `work/source-intake-2026-09-28/processo-civil/units/shared/passos-assigned-ocr.txt` (also `batches/ocr-refinement/passos-pp123-142-ocr.txt`). It remains raw/unverified; a spot-read of PDF p. 2 matched the scan.
- The two 28/09 Costa text files (`batches/p1/costa-text-layer.txt` and `batches/scan-recovery/costa-ocr.txt`) contain only scan markers/watermarks, so no usable Costa OCR could be reused. Local Tesseract OCR was run to a temporary file and spot-read against PDF p. 2. The source remains a scan; OCR is raw.
- Reused available 28/09 Lucon OCR and recorded it as local OCR. Barbosa Moreira and Taruffo were OCRed locally with Tesseract; representative pages were spot-read. Tesseract was also used locally on the six unique Moodle model images and the 2019/2 and damaged 2025/2 exam scans. No cloud vision was used.
- The books/assigned-reading inventory confirmed local text layers for the remaining PDF readings. Peer notes have selectable text but are guidance only and cannot support course claims.

## Scope cautions for the next stages

- CPC capture is the dated Planalto HTML snapshot from 2026-09-28 (`cpc-lei-13105-2015-2026-09-28.html`). Refresh from Planalto before S4 statute slices; this was left outside S1 scope.
- The file named `2025_2 - P1 - mily.pdf` identifies Sérgio Mattos in the scanned exam text, despite the master brief describing the eight exams as Scarparo's. It is included as a candidate source pending the chairman's decision about its place in the Scarparo bank.
- Cintra, *Intervenção de terceiro por ordem do juiz*, cap. 10, remains `missing` as directed. No content was inferred from peer notes or memory.
