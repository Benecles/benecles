# S2 — chapters and complete source files

Branch: `codex/tgc-pipe-2`, stacked on S1 `688acc7`.

## Outputs

- **Venosa, 17th ed. (2016):** 50 top-level TOC chapters represented by 59 chapter/section files. Oversized top-level chapters are subdivided at complete TOC subsection boundaries; the index records parent warnings. The EPUB TOC omits chapter 26.
- **Caio Mário, vol. III (2014):** 22 top-level TOC chapters represented by 25 chapter/section files. Chapters XXXVII, XLVI, and XLVIII are section-split at numbered subsection boundaries. EPUB page anchors are preserved; there is no source PDF.
- **Slides:** 8 decks, each in its own complete page-marked file.
- **Exercises, answer keys, and peer-shared past material:** 8 sources, each in its own complete page-marked file.
- All generated text in `chapters/` is git-ignored. The indexes are tracked. `shelf.csv` retains its original descriptive columns and now includes stable `source_id`, `source_role`, and `lesson_id` columns for the S2 inputs.

## Reuse and extraction limits

The slide decks and exercise/exam sources were checked against the S1 local text extractions before new extraction. PDF page text was extracted locally; scanned past exams used local Tesseract. No scanned images were sent to a cloud service.

The two supplementary answer keys and the extra-questions PDF yielded no readable source words after local extraction/OCR; page markers and separate indexes preserve their page spans, but their source text remains an extraction gap. The old P1 files are peer-shared scans; handwritten responses may have OCR errors. Current-term official P1/P2/recovery papers and keys remain unavailable per S1.

S1's article-level extracts for CC/CDC/CF and Lei 13.874/2019 art. 7 remain missing. No whole statute or CF file was added. The two available basic books predate Lei 13.874/2019, as already recorded in S1.

## Checker evidence

Known-bad fixture (one core-book file with 15,001 body words and a page-span gap) was rejected before accepting the final output. The invocation reported a gap after PDF 1 and a 15,007-word core file (including marker tokens); the final checker excludes marker tokens from its word cap.

Final check: `python3 work/pipeline/tools/pipeline_check.py s2 teoria-geral-dos-contratos` → `S2 PASS: 100 indexed chapters`.
