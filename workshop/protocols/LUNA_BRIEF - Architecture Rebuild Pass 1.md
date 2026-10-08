# Luna brief: architecture rebuild, pass 1

## What changed

The earlier rewrite pass fixed prose quality and added callouts. That part worked. But it left the underlying structure alone, and the structure is the actual problem.

**Read `/Users/benecles/Documents/Protocols/Study Pack Architecture.md` in full before doing anything.** That document is now the governing spec. This brief is just the work order for the first pass.

The short version of what's different:

- **File boundaries are no longer sacred.** Every file in the corpus exists because a source document existed — a slide deck, or a week on the calendar. That's a deck inventory, not a concept map. Where the course's actual spine disagrees with the source's file boundaries, the spine wins.
- **Why before what.** Units open with the problem the concept solves, not with a definition. The reader needs to know what question is on the table before getting any answer to it.
- **The goal is a mental model, not coverage.** If a reader finishes holding every fact and still says "I don't get it," the unit failed. Facts are the bricks; the model is the build.
- **Diagrams.** There are currently zero in the entire corpus, and law is unusually diagrammable. This is the biggest single gap.
- **The earlier benchmark (the owner's Notas Polidas) is a formatting reference, not a ceiling.** Don't aim to match them structurally — they're lecture-shaped too.

## This pass: one file

Redo **`Coursework/Teoria do Delito/luna_output/01 Semana 01 - Conceito analítico e arquitetura do delito.md`** against the new architecture.

Yes, that file was already rewritten once and it came out decent by the old standard. That's exactly why it's the test case: we get a direct before/after on the same content, and Semana 1 is the unit that establishes the spine for the whole course, so it's the one that most needs to be right.

Copy the current version aside before touching it (per the preserve-before-rewrite rule — it applies every time, regardless of git status).

What to change:

1. **Open with the problem, not the concept.** Right now it opens by explaining what the analytical concept of crime is. It should open with why anyone needed one: what goes wrong when you don't separate these judgments, what bad conclusions people reach without the filter cascade.
2. **State the spine and put a diagram on it.** Teoria do Delito's spine is a cascade with exit points: *something happened → was it human conduct → does it match a type → is it nevertheless permitted → can this person be blamed → what follows.* That is a flowchart, and it belongs near the top of Semana 1 as an actual diagram, not a table. Every later week will refer back to it.
3. **Follow the six-part unit arc** from the architecture doc: the problem, the shape of the answer, the components, the assembly, the model under load, the boundaries. The current version has good components and good worked cases but essentially no *assembly* section — nothing that shows how the pieces interact at the seams. That's the part that turns a parts list into a model.
4. **Add diagrams where prose is currently doing a diagram's job.** Candidates in this unit: the filter cascade, the relationship between fato/norma/juízo, and the exclusions-of-conduct branch points.
5. **Keep every fact, citation, article number and case reference.** Rearranging is fine. Losing content or upgrading certainty is not. Don't compress: the last correct pass on this file ran about 0.77x the source word count, and that was cleanup of genuine meta-commentary, not content loss. Going below ~0.6x means something real got dropped.

## Answer this first

Before adding diagrams at scale we need to know what the build pipeline can actually render. You wrote the PDF/EPUB build script, so: **can it render mermaid, inline SVG, both, or neither, as it currently stands?** If mermaid needs a JS library that Chrome-headless won't load offline, say so and recommend the alternative. Answer this in your report even if the answer is inconvenient — it decides the diagram format for the whole corpus.

## Standing rules, unchanged

- No meta-commentary about sources, provenance, or what you couldn't access. If a gap affects a specific claim, that's one `[!CAUTION]` line next to that claim, nothing more.
- No zero-information restatement. Every sentence asserts something the previous one didn't.
- No em dashes.
- Callouts distributed through the body by function, roughly one per major section, never clustered at the top as decoration.
- Tables whenever three or more items share a set of attributes.

## When you're done

Stop. One file only, don't touch Semanas 2 through 15 or the index files, don't rebuild any PDF or EPUB.

Report: word count before and after, callout count, table count, diagram count and format used, and your answer on the mermaid/SVG question. Then it comes back to Claude for review before anything else gets dispatched.

This is a loop and it will run for many rounds. Don't try to get it perfect in one shot — get this one file into a shape worth reacting to.
