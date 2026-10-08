# Luna brief: pass 4, build integrity and the two leftovers

Pass 3 did the Semana 15 split cleanly — five doctrinal addenda, correct numbering, linter clean on all of them. Good. Two items from that brief did not get done, and one of them is the important one.

This pass is small and mostly mechanical. Do not start diagrams; that is pass 5 and its spec is being written.

## 1. Kill the directory-as-editorial-state pattern

`is_teaching_file()` in `tools/rebuild_study_packs.py` still ends with a bare `return True` for Teoria. Pass 3 removed the dead file from the folder but left the mechanism that let it ship in the first place.

Fixing the filter is not enough. The deeper defect is that **the filesystem is functioning as editorial state**: whatever happens to be sitting in `luna_output/` determines what a student receives. Any future stray file, backup, scratch draft or superseded version gets built automatically.

Replace directory globbing with an explicit declared manifest. One per course, checked into the repo, listing the files that compose the artifact **in order**:

```yaml
course: Teoria do Delito
title: Teoria do Delito - Complete Study Pack
contents:
  - 01 Semana 01 - Conceito analítico e arquitetura do delito.md
  - 02 Semana 02 - Conduta, sistemas e política criminal.md
  # ... through 15
  - 16 Adendo doutrinário - Brandão (Teorias da Conduta).md
  # ... through 20
  - Mapa do Curso.md
  - Guia Mestre de Estudo.md
```

The builder reads the manifest and builds exactly that, in that order. Then add these checks, failing the build on any of them:

- a file named in the manifest does not exist
- a `.md` file exists in the source directory but is not in the manifest and not in an excluded location — report it rather than silently including or excluding it
- the same file appears twice
- a manifest entry resolves inside `Superseded/`, `_original_source_backup/` or similar

Coverage registers, source maps and blueprints are operator records. They stay in the repo, they never appear in a manifest.

Do this for all three courses, not just Teoria. Controle and Metodologia currently use regex patterns, which are better than `return True` but are still the directory deciding content.

## 2. The two leftovers from pass 3

`Guia Mestre de Estudo.md` and `Mapa do Curso.md` are the only files still failing the linter, on em dashes. But Guia Mestre needs more than that, and the pass 3 brief explained why: it opens by telling the student it was "rebaixada para `rough_draft`" for lacking a blueprint and coverage ledger. That is pipeline status printed at the top of a study guide.

Rewrite it as the course spine document. What the delito cascade is, why the units run in that order, how to use the pack, and what the reader should be able to do by the end. Expect it to get much shorter, since most of its 9,810 words are provenance hedging. Remove every reference to blueprints, ledgers, corpus status, recovery, and `rough_draft`.

`Mapa do Curso.md` just needs the em dashes removed.

## 3. Start collecting dependency metadata

Cheap instrumentation now, linter later. On every teaching file you touch from here on, add frontmatter declaring what the unit introduces and what it depends on:

```yaml
---
unit: Semana 12 - Imputabilidade e erro de proibição
introduces: [imputabilidade, potencial consciência da ilicitude, exigibilidade,
             actio libera in causa, descriminante putativa]
requires: [fato típico, antijuridicidade, erro de tipo]
---
```

Do not build any checking around this yet and do not restructure anything to satisfy it. Just record it accurately. Once there is real data across all units we will design the dependency checks against actual graphs rather than hypothetical ones.

Frontmatter is already stripped at build time, so this will not reach the reader.

## Verification

```
python3 tools/lint_study_packs.py "Coursework/Teoria do Delito/luna_output"
```

Zero errors. Then rebuild all three PDFs from their manifests and report page counts. Teoria was 470 pages including roughly 14,000 words that should now be gone.

Report: the manifest format you settled on, what the integrity checks caught when first run across all three courses (this is the interesting part, so list anything that was in a build folder but should not have been), Guia Mestre word count before and after, linter output, and the three new page counts.
