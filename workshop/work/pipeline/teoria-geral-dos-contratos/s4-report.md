# S4 — lesson compendia

Branch: `codex/tgc-pipe-4`, stacked on S3 `b03496d`.

The builder assembled all 17 lesson compendia from S0–S3: 174 files and 177 provenance rows. Every lesson has `00-index.md`, a mapped slide file or explicit missing-slide placeholder, its S3-assigned primary/supporting/background material, and an exercises/exams file. The three missing-slide cases are retained as warnings for Aulas 15–17.

The available article-level statute/CF extracts are still missing from S1. S4 therefore contains no whole statute or Constitution source. Venosa (2016) and Caio Mário (2014) remain the older local editions, not sources for post-2019 amendments; the missing current-term exams and unreadable answer-key extracts remain documented in `triage-notes.md`.

## Check

```text
python3 work/pipeline/tools/pipeline_check.py s4 teoria-geral-dos-contratos
WARN: aula-15.html: slide source explicitly marked missing in shelf (missing-slides-aula-15); no substitute assigned
WARN: aula-16.html: slide source explicitly marked missing in shelf (missing-slides-aula-16); no substitute assigned
WARN: aula-17.html: slide source explicitly marked missing in shelf (missing-slides-aula-17); no substitute assigned
S4 PASS: 17/17 lesson manifests / 177 provenance rows
```

The S4 check validated manifest coverage and row counts, generated-file SHA-256 values against the manifests, and byte-for-byte provenance from S2 source atoms. No statute/CF whole-document source was assembled.
