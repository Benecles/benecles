# Luna brief: pass 3, structural fixes to Teoria do Delito

Pass 2 came back well. All fifteen Semanas rewritten, word counts consistent at 5,600 to 7,500, callouts distributed through the body rather than clustered, spine re-invoked in the units I checked, linter clean on Semana 1. Semana 12 opens with the question and gives the three-filter table before the details, which is the right shape. Keep doing that.

This pass is structural only. No new authoring except one rewrite. Diagrams come in pass 4, so do not start them here.

## 1. Three things are shipping into the PDF that must not

`is_teaching_file()` in `tools/rebuild_study_packs.py` ends with a bare `return True`, so for Teoria every `.md` in `luna_output/` is built into the reader's pack. That currently includes about 14,000 words nobody should ever see:

- `Registro de Cobertura 2026-2.md` (6,912 w) — corpus authentication, file hashes, what the Moodle scrape did or did not contain
- `Mapa Exato de Fontes 2026-2.md` (773 w) — scrape provenance
- `Teoria do Delito: Guia de estudo.md` (6,259 w) — **the abandoned first-pass output**, the one that compressed 186,000 words to 6,000. It was superseded but never moved out of the build folder.

Fixes:

- Move `Teoria do Delito: Guia de estudo.md` to `Superseded/`. It is dead content.
- Give Teoria an explicit allowlist in `is_teaching_file()` rather than `return True`. Match the pattern used for controle and metodologia. Coverage registers and source maps are operator records: they stay in the repo, they never enter a build.
- Check the same failure in the other two courses. Metodologia and Controle have explicit patterns already, but verify nothing operator-facing slips through them.

## 2. Semana 15 is six documents in one file

At 46,455 words it is eight times its siblings, and the reason is that the mechanical split keyed on `# Semana N` headings, so everything trailing the last one fell into the final bucket. It currently contains:

| Line | Document |
|---|---|
| 1 | Semana 15: Participação, Acessoriedade e Comunicabilidade |
| 739 | Brandão: Teorias da Conduta |
| 1151 | Roxin: Política Criminal e Método do Sistema |
| 1629 | Roxin: Tipo, Dever, Omissão e Imprudência |
| 2132 | Roxin: Justificação e Conflito Social |
| 2547 | Roxin: Culpabilidade, Responsabilidade e Desistência |

The five trailing documents are textbook reconstructions, not week 15 material. They are the direct equivalent of Controle's `21 Adendo doutrinário - Lenza` and `22 Adendo doutrinário - Mendes e Branco`.

Split into six files. Keep `15 Semana 15` as the week. Number the rest as doctrinal addenda following the existing convention:

```
16 Adendo doutrinário - Brandão (Teorias da Conduta).md
17 Adendo doutrinário - Roxin (Política criminal e método).md
18 Adendo doutrinário - Roxin (Tipo, dever, omissão e imprudência).md
19 Adendo doutrinário - Roxin (Justificação e conflito social).md
20 Adendo doutrinário - Roxin (Culpabilidade e desistência).md
```

Each split file gets its own proper opening and section numbering starting at 1. The linter currently reports numbering errors on this file purely because six numbering sequences are concatenated; splitting resolves them. Verify the linter is clean afterwards.

Merging the four Roxin parts into one file is acceptable if they read as one continuous argument. Use judgment; say which you chose.

## 3. Rewrite `Guia Mestre de Estudo.md`

9,810 words, reader-facing, and opening with this:

> Esta versão é uma camada de orientação, não um dossiê semestral completo. Ela foi rebaixada para `rough_draft` porque não possui o blueprint e o ledger de cobertura exigidos...

That is pipeline status reporting addressed to an operator, printed at the top of a student's study guide. The document is full of it.

Rewrite it as what the architecture calls the course spine document: what the delito cascade is, why the units are ordered as they are, how to use the pack, and what a reader should be able to do by the end. It should get considerably shorter — most of its current length is provenance hedging. Strip every reference to blueprints, ledgers, corpus status, what was or was not recovered, and `rough_draft` classification.

`Mapa do Curso.md` (330 w) is fine in substance; it just needs the em dashes removed.

## 4. Verification before reporting

Run the linter on the whole folder and report the output:

```
python3 tools/lint_study_packs.py "Coursework/Teoria do Delito/luna_output"
```

It now excludes coverage registers and source maps automatically, so a clean run means the reader-facing set is clean. Errors must be zero.

Then rebuild the Teoria PDF and run a contact sheet over it:

```
python3 tools/contact_sheet.py "Study Packs/Teoria do Delito - Complete Study Pack (Louro Classico).pdf" sheet.png 20 30
```

Report the new page count. The old build was 470 pages and included the 14,000 words being removed here, so expect a drop.

## Report back

Which files moved to Superseded, what the new `is_teaching_file` allowlist is, how Semana 15 was split and whether you merged the Roxin parts, the before and after word count on Guia Mestre, the linter output, and the new PDF page count.

Do not start diagrams. That is pass 4, and it comes with a claim-manifest requirement that is not written yet.
