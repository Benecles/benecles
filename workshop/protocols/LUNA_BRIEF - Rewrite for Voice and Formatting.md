# Brief for Luna: rewrite the three study packs for voice and formatting

This applies to all three courses' `luna_output/` source material: Teoria do Delito, Metodologia Jurídica, Controle de Constitucionalidade. The owner read spot-checks from all three and the verdict was blunt: the writing is bad, the formatting is nearly absent, and the material spends its opening real estate on things the reader doesn't need. Read this whole brief before touching anything.

## The owner's own words, verbatim

"There are some problems. First off, no markdown! Second off, the explanations come off as clunky, it's a terrible way to teach! ... the explanation quality is pretty bad for stuff that I already know, which is what I used to benchmark whether it was good or not at explaining, and it spends way too long in the beginning providing me useless information on what I ought or ought not to consider as sources and explaining provenance ... it's meant to TEACH, it's meant to give me INFORMATION, it's not meant to tell me where it got it from, separate the backend from the user experience, I shouldn't CARE as the reader. ... no use of markdown as a visual aid to help digest the information, callouts, tables, the use of subheaders, different callouts like citations and whatnot, with different colors."

## The concrete diagnosis

Sample checked: `Controle de Constitucionalidade/luna_output/06 Natureza do vício de inconstitucionalidade.md`. Two failures, both systemic across the corpus:

**1. Almost no markdown craft.** One table in the whole file. No bold on key terms when they're introduced (`vício orgânico`, `nomodinâmica`, `pressupostos objetivos` all appear as plain text mid-sentence, easy to skim past). No callouts. No blockquoted definitions. Sub-headers exist but are too coarse (nine `##` sections for a topic that has at least twenty distinct sub-concepts worth their own visual break). The result is walls of dense paragraph text that all look the same weight, so nothing stands out as more or less important.

**2. Backend process leaked into reader-facing content.** Section 10 of that file is titled "Nota sobre a lacuna bibliográfica" and its entire content is: the Lenza and Mendes/Branco chapters weren't available for this reconstruction pass. That is a note to whoever ran the pipeline, not something a student reading to learn the material needs. Section 9 does the same thing in smaller form: "A sequência didática estabelece... Ela não desenvolve, porém, os efeitos das decisões..." — narrating what the source deck covered or didn't cover, instead of just teaching what's known. **None of this belongs in the reader-facing file.** If a source gap matters enough to flag, it gets one line inside a `[!CAUTION]` callout attached to the specific claim it affects, never its own section, never a paragraph of meta-narration about the reconstruction process.

## The real disease: zero-information restatement, not "academic tone"

Heavy academic register is not the problem by itself, this is legal textbook material, some formality is expected and fine. The actual problem is saying the same proposition multiple times in a row, in different words, without adding any new information each time. The owner's own example of what this looks like, exaggerated for clarity: "The cat is yellow, having this auburn color on the feline means that the mammal at hand may or may not present colors that are not blue or red, which means the yellow coloration present on that life form adequately presupposes pigmentation which induces upon that entity the visible quality of appearing, not to one but to multiple people, all things considered, that may forthright present visibly a situation such as to resemble the characterization to all who may witness it, of being particularly under the characteristic shade that may or may not be called, at least by the majority of those that have observed it, yellow." That sentence says "the cat is yellow" roughly six times and teaches nothing on repetitions two through six. That is not academic prose, that is padding, and it is the specific failure mode to hunt for line by line.

The real file has the same disease at smaller scale: "O vício ajuda a diagnosticar a desconformidade, mas não determina sozinho se a decisão será incidental ou concentrada..." followed shortly by more sentences that restate the same "classification isn't determinative of X" point in new phrasing. **Test for this directly while rewriting**: for every sentence, ask whether it asserts something the previous sentence didn't already assert. If the honest answer is no, the sentence is padding, cut it or fold whatever fragment of new information it carries into the sentence before it. A paragraph that used to be six sentences making one point should often become two sentences making that same point, once the restatement is gone. Do not preserve length by finding new synonyms for the same claim.

## The actual bar: the owner's own notes

The owner's personal "Notas Polidas" are the gold standard he benchmarks against. Read these two files completely before writing anything, they are the target voice and format, not just inspiration:

- `/Users/benecles/Documents/Notes Systems/KnowledgeSystem/Gallery/Outputs/Notas Polidas/Teoria do Delito/Teoria Geral do Crime e Tipicidade.md`
- `/Users/benecles/Documents/Notes Systems/KnowledgeSystem/Gallery/Outputs/Notas Polidas/Controle de Constitucionalidade/Mapa — Princípios de interpretação constitucional.md`

Study what they actually do:

- **Callouts, used constantly and by type.** `[!INFO]` for context/definitions, `[!CAUTION]` for a claim that needs conferring or is doctrinally contested, `[!EXAMPLE]` for a worked example, `[!QUOTE]` for a direct quote of a source formulation, `[!NOTE]` for a small aside. Every one of these appears multiple times per file. This is not decoration, it's how the reader's eye finds the thing they need.
- **Bold on every key term**, every time a term is introduced and often when it recurs: `**Parte objetiva:**`, `**dolo**`, `**Coação moral irresistível:**`. A skim of just the bold words should reconstruct the outline of the page.
- **Tables for anything comparative or enumerable.** Elements of a concept, situations vs. treatment, type vs. definition vs. example: three columns, done, instead of a paragraph doing the same job worse.
- **Examples live inside the flow**, usually in an `[!EXAMPLE]` callout right where the concept is introduced, not deferred to a separate "aplicação" section at the end.
- **Short, direct sentences.** Compare the tone: the owner's note says "A ideia nunca pode delinquir." and moves on. The bad file says "Essa última pergunta impede que a classificação seja confundida com uma teoria automática de nulidade" when it could just say what the classification does and doesn't do, directly, in fewer words with less hedging.
- **Sub-headers are granular.** A 300-word block gets its own `###` if it's a distinct sub-concept. Don't make the reader hold nine sections' worth of undifferentiated argument in their head.
- **Caveats are inline and tiny.** When the source material is uncertain or a formulation is doctrinally contested, that's a one- or two-sentence `[!CAUTION]` callout sitting next to the specific claim, not a section, not a paragraph, not a confession about what wasn't available.

## What to do

For every file in the three `luna_output/` directories (excluding blueprints, registers, and handoff notes, this is about the actual teaching content):

1. **Read the file and its own source material again** (the original Aula PDF, deck, or transcript it was built from). You are not inventing new content, you are re-expressing the same verified content in the format above. If a fact wasn't confirmed the first time, it stays unconfirmed now, don't upgrade certainty just because the format changed.
2. **Rewrite for voice**: direct, confident, teaching sentences. Say the thing once, clearly, instead of stating it and then hedging it three ways. Cut restatement sentences that just rephrase the sentence before them without adding information.
3. **Rewrite for structure**: break into finer `###`/`####` sub-headers where a sub-concept deserves its own visual block. Bold every key term on introduction. Turn any comparative or enumerable content into a table.
4. **Add callouts deliberately, not decoratively**: `[!INFO]` for a definition or piece of context that deserves to stand apart from the main teaching flow, `[!EXAMPLE]` for worked examples (pull them out of buried mid-paragraph mentions and give them their own block where that helps), `[!QUOTE]` for any direct quotation of a statute, case, or source formulation that's already being quoted, `[!CAUTION]` for a specific claim that's contested, unconfirmed, or needs the reader to double check before relying on it in an exam or a filing.
5. **Delete every meta-commentary section.** No "o que a apresentação não desenvolve," no "nota sobre lacuna bibliográfica," no paragraph narrating what the source deck did or didn't cover. If something is missing because a source wasn't available, that's either a one-line `[!CAUTION]` next to the specific affected claim, or it's simply absent, don't write a paragraph about the absence.
6. **Keep every actual fact, citation, article number, and case reference exactly as verified.** This is a formatting and voice rewrite, not a content rewrite. Do not drop verified content to hit a length target, and do not add unverified content to fill out a callout.

## Findings from a full editorial read-through (2026-08-27)

Claude read all 14 already-rewritten files in Controle de Constitucionalidade end to end (not sampled) after the first pass. The prose-quality fix worked: content stayed accurate, well-cited, current, and the padding disease is gone. But the formatting instruction above was under-applied in a specific, repeatable way. Fix these directly, they are not new taste, they are the same rules above enforced harder:

1. **Two callouts per file is not "used constantly."** Nearly every rewritten file has exactly one `[!INFO]` and one other callout, both glued to the very top, then zero callouts for the rest of the file no matter how long it runs. A 5,000-word file covering four major cases and a doctrinal debate (Kelsen vs. Schmitt) used exactly two callouts total. That is decoration, not the tool. **Concrete check**: after finishing a file, count callouts and count major sub-sections (`###`/`####`). If sub-sections outnumber callouts by more than roughly 2:1, go back and find the definitions, worked examples, direct quotes, and contested claims inside the body that should have gotten one.

2. **Table trigger, stated as a rule, not a suggestion**: any time the text is about to present three or more items that share the same set of attributes — cases with (date, holding, relevance), doctrinal positions with (author, claim, basis), classification types with (name, definition, example) — stop and make it a table before writing the prose version. Concretely observed misses: a four-case chronology building to a súmula vinculante, left entirely in prose; a two-position doctrinal debate (Kelsen vs. Schmitt) covering three subsections, never tabled; four precedents on the same narrow doctrine, left as four separate prose subsections with no summary table. Other files in the same corpus handled nearly identical content (case chronologies, doctrinal comparisons) with tables correctly, so this is inconsistency, not a capability gap. Do it every time the trigger condition is met.

3. **Direct quotations of binding text default to `[!QUOTE]`.** If a sentence is the literal text of a súmula, statute article, or holding, and it's already being presented as a quotation, it belongs in a `[!QUOTE]` callout, not a plain paragraph with quotation marks. Found at least one súmula's full operative text sitting in regular prose.

4. **Proofread section numbering before calling a file done.** Two files had a skipped section number (jumped from 6 to 8, and from 11 to 13) — almost certainly from cutting the banned meta-commentary sections without renumbering what followed. After deleting or merging sections, renumber everything after the cut and verify the sequence is unbroken before moving to the next file.

5. **Cross-file overlap**: when two files in the same course cover a lot of the same cases and mechanisms (this happened between two files that both fully re-explained Rcl 4.335, HC 82.959, SV 26, and the same abstrativização mechanisms with near-duplicate tables), this is likely inherited from the original one-file-per-slide-deck structure and isn't necessarily wrong to preserve, but don't let the second occurrence balloon to the same length as the first. If a file is substantially re-covering ground a numbered sibling already built out in full, it can cross-reference the earlier file for the shared mechanism and spend its own words on what's actually new to it.

## Process change: checkpoint before running the whole corpus

Do not run this brief across an entire course and then report back "done." Last time, a version of this brief was run on all three courses in one shot with no checkpoint, and one course (Teoria do Delito, which turned out to have a different source structure than assumed) came back 96.6% compressed before anyone caught it. This time:

1. Rewrite **one file** first.
2. Stop and report: which file, its word count before and after, callout count, and a short note on any table-trigger content it contained and whether it got tabled.
3. Wait for confirmation before continuing to the rest of that course.

This is slower per-course but it means a systematic problem gets caught on file one, not file twenty-two.

## Preserve before rewrite, every time

Before overwriting any file in `luna_output/`, copy the current version into a `Superseded/` (or equivalent) subfolder first, even though this directory has no git tracking, especially because it has no git tracking. This applies to every file this brief touches, not just the final PDF/EPUB artifacts already covered under "When done" below.

## What NOT to do

- Don't invent examples, mnemonics, or doctrinal framing that wasn't in the original source material just to make a callout look fuller.
- Don't turn every paragraph into a callout; callouts mark the things that deserve to stand apart, if everything is boxed nothing is.
- Don't lose the distinction between what's settled and what's contested. If the source hedges because the doctrine actually is split, that hedge is real content, keep it, just say it once, cleanly, ideally inside a `[!CAUTION]` rather than three qualifying clauses in the main sentence.
- No em dashes anywhere, no provenance tags in body text (standing rule for this whole corpus already).

## The rebuild step

The PDF and EPUB build scripts from the original pass are gone (they lived in a session scratchpad, not saved to the repo). Once the markdown rewrite is done for a course, you'll need to rebuild the printable PDF and Kindle EPUB from the new source, which means the HTML/CSS conversion step needs to actually render Obsidian callout syntax (`> [!TYPE] Title` followed by `>` blockquote lines) as visually distinct colored boxes, not as a plain blockquote. Give each callout type its own left-border color and a small icon or label matching its type (INFO blue, CAUTION amber/red, EXAMPLE green, QUOTE gray/purple, NOTE gray), consistent with how Obsidian itself renders them, since that's the visual language the owner already reads daily. Verify by opening a rendered PDF page and confirming the callouts are visibly boxed and colored, not just indented text.

## When done

Overwrite the files in place in each course's `luna_output/`. Rebuild all three PDFs and both EPUBs in `Documents/Law School/Study Packs/`, replacing the current ones (move the current ones to `Study Packs/Superseded/` first, don't just delete them). Report back which files were rewritten, and flag anything where the original source didn't have enough distinct sub-concepts or comparative content to justify heavy table/callout use, some sections will legitimately stay closer to prose, that's fine, the point is that dense enumerable material gets structured and prose material doesn't get artificially chopped up.
