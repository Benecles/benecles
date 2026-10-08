# Reconstruction Pipeline Protocol

How to turn a body of source material (a professor's assigned bibliography, a set of lecture transcripts, any corpus someone would otherwise have to read themselves) into one continuous, well-structured document that delivers the same substance at equal or greater depth, without anyone having to read all the originals.

This is a standalone methodology file, not tied to the KnowledgeSystem vault. Read it whenever starting a reconstruction job on a new corpus (a new course, a new body of transcripts, anything the same shape), whether the reader is Claude or another model.

## Origin

This descends from a hand-built two-prompt workflow ("Obsidian Law Clerk") the owner ran manually through Gemini: paste a raw lecture transcript, get back a Master Index of chapters, then request chapters one at a time and paste each into an Obsidian note. That workflow is preserved as a worked example further down, because it is the calibration reference for everything below, not just history.

The workflow was later automated into an agentic protocol that removed the manual chapter-by-chapter relay. That automation quietly broke the thing that made the original work. This document is the correction, generalized past the original's single use case (one lecture, one sitting) to arbitrary corpus size.

## The two failure modes, and why they're opposite mistakes

**Failure mode one: collapsing Architect and Executor into one continuous pass.** An agent that reads everything and writes everything in one unbroken context loses three things at once that the manual relay had for free: each writing unit no longer gets a fresh context (so instructions from a hundred pages back are diluted by everything written since), each unit's brief is no longer literally the prompt it's answering (it's buried mid-conversation instead of being the most recent thing the model sees), and units start imitating each other's shape because the most recent example of "what a unit looks like" is always the model's own prior output. This produces bland, self-similar sections regardless of how different the underlying source material actually was.

**Failure mode two: replacing structural anti-compression with a numeric target.** The original method never states a word count anywhere. It gets depth by maximizing the number of chapters and by deliberately leaving each chapter under-budget rather than at the ceiling, explicitly so a chapter can still breathe. A later version of this pipeline was given a numeric target instead ("aim for 8,000-12,000 words per module") and every module it produced landed in an unnaturally tight band regardless of real source density, because a stated number becomes the objective and starves the qualitative goal of preserving whatever depth the source actually has. **Never state a target length anywhere in a reconstruction brief.** Let length be an output of unit count and source density, never an input.

Both mistakes look like reasonable simplifications in isolation. They compound: numeric targets are what make collapsed single-pass execution look acceptable, because a target gives the illusion of a stopping rule the qualitative approach doesn't need.

## The mechanism

```
full read  ->  blueprint  ->  bounded execution (fresh context per unit)  ->  assembly
```

**Read everything in the declared scope before blueprinting anything.** Sampling can locate work, it cannot certify coverage. If the scope is too large to read in full at once, shrink the declared scope, not the reading.

**The blueprint is a detailed prompt for future execution, not a table of contents.** For each unit it must specify: what source span it draws from, the specific content, examples, distinctions, and arguments to pull out of that span, and enough concrete direction that the unit-writer doesn't have to independently rediscover structure. A one-line chapter title is not a blueprint entry. A worked example from an actual blueprint that produced good output: *"This chapter serves as the philosophical foundation. Start by enriching the fox/hedgehog metaphor to explain legal coherence versus ad-hoc problem solving. Then detail the three perspectives: Ontological, Ideological, Methodological. Emphasize Methodological as the core of legal argumentation. Use a quote-callout for the definition of legal argumentation and a list defining the three actors across Civil, Criminal, and Labor law."* That is roughly 100-150 words of instruction. It reliably produced 500-700 words of real, structured prose. That ratio, not a stated target, is what "enough detail per unit" looks like in practice.

**Maximize unit count, and leave slack.** More narrow units beat fewer broad ones. Each unit should be written with room to spare in whatever output budget is available, not built to just barely fit at the ceiling, because a unit written at its ceiling degrades. Thinner source material earns fewer or shorter units. Do not pad it to match richer material elsewhere in the same document. Both directions of this rule matter equally; the failure mode this whole document exists to prevent is length becoming uniform when the underlying material isn't.

**Each unit is written in as close to a fresh context as practically achievable, receiving only its own blueprint entry and its own source span.** This is the part automation is tempted to skip because it's inconvenient, and it's the part that most needs to survive automation. If the runtime genuinely cannot start a new context per unit, at minimum re-read that unit's own blueprint entry and source span immediately before writing it, rather than relying on it still being salient from earlier in a long session.

**Recursion, not a fixed number of layers.** The invariant underneath all of this is simple: never write prose for a unit larger than can be held at full resolution while writing it. A single lecture transcript satisfies that in one Architect pass over one flat list of chapters. A large corpus, a whole course's worth of required and supplementary reading, will not: the top-level blueprint's own units (an "Aula," a "week," a single dense 60-page source reconstructed at full depth) may themselves be too large to write as one unit. When that happens, that unit becomes the root of its own Architect pass, reading only its own material, producing its own blueprint of sub-units, before any prose gets written for it. Depth of nesting is whatever it needs to be given the actual volume: two layers for a short corpus, three or more for a large one. Decide this per-unit as the work reveals its own scale, not as a fixed plan chosen in advance.

**Assembly happens after every unit is written**, concatenated in the order the top-level blueprint declares, with brief connective material between major sections so a reader always knows roughly where they are in the whole.

## Choosing who plays Architect

The rule that survives is: **the Architect must read the full material in its declared scope before blueprinting.** Which model does that reading is a separate, tunable decision, not fixed to "always the strongest available model."

The original strong-model-always rule was calibrated for a specific hard case: a rambling, unstructured live transcript where the actual argument order has to be discovered and imposed. That's a genuine reasoning-heavy task. Most corpora are not that case. Published academic writing, books, structured lecture notes, already carry real internal structure, an argument, sections, a stated throughline. Architecting already-structured material is a comparatively easy job, and reading it in full is the expensive part in raw volume terms, not the hard part in reasoning terms. Assigning that read-and-outline pass to a cheaper, high-volume model is the right call whenever the source material has real structure to begin with, and it is also the right call for straightforward cost reasons: a stronger model re-reading everything just to hand off a blueprint burns exactly the resource that should be spent on prose quality, or is available more cheaply elsewhere.

Use judgment on where the actual difficulty sits for a given corpus, and route Architect accordingly. Reserve the strongest available reasoning for genuinely difficult structural judgment (chaotic sources, real interpretive disagreement to adjudicate, high-stakes accuracy questions) and for final assembly and review, where catching one bad section is worth more than doing the whole read.

## Editorial stance

- **No compression.** Every real distinction, example, and argument in the source gets the space it deserves. This is a reconstruction at full depth, not a summary.
- **Explain, do not transcribe.** Restructure and explain the argument in fresh prose. Short attributed quotes of a sentence or clause are fine where a specific formulation matters. Do not retype or lightly reword long passages of the original; that is reproduction wearing a costume, not reconstruction, and it is also a real copyright problem at any scale beyond a short quote.
- **No provenance apparatus in the body text.** Inline tags marking every claim's source (`[Fonte primária]`, `[Inferência]`, etc.) look rigorous but create false confidence if nobody is going to audit them, and they clutter prose that's meant to be read start to finish. Ordinary scholarly attribution in running prose, naming who argues what, is expected and different from this.
- **Depth from treatment, not from new facts.** Enrichment is welcome: defining terms the source assumes, adding examples, drawing connections across the corpus that no single source drew because none of them were writing for this reader. New *substantive* claims, dates, attributions, causal links, are not welcome unless they trace to something real; specialist or obscure material is exactly where fluent-sounding fabrication is hardest to catch and most damaging.
- **Missing is missing.** If a source is genuinely unavailable, say so plainly rather than producing a thin section that quietly papers over the gap.
- **Research is encouraged where it resolves a real question**, especially getting a source's core position right on a point that recurs across multiple units, and especially for grounding material the reader has no prior context for. It is not required as a citation ritual for every claim.
- **Keep the reader oriented.** Brief connective tissue between units, what this section is, how it follows from the last one, is worth the space.
- No em dashes, if that's a standing preference for the deliverable in question; check the specific project's own conventions.

## Verification

Prototype before scaling. Produce the first unit (or first few, if the corpus is heterogeneous, one of each kind), then check it against its actual source before authorizing the rest. This is the calibration checkpoint the manual relay got for free, since the human was reading every chapter as it came back, and it is the single highest-leverage step in the whole pipeline: it is far cheaper to correct the approach once than to redo the whole corpus.

Spend real verification effort proportional to the corpus's actual risk profile. Mainstream, well-represented material is comparatively safe; a wrong claim tends to collide with what any capable model otherwise knows. Narrow, specialist, or recently-published scholarship is not self-correcting in the same way, and deserves closer checking of substantive claims, especially attributions and positions, against the real source.

## Worked example (verbatim, for calibration)

Preserved because the ratios above are drawn directly from it, not asserted in the abstract.

**System framing, given once at the start of the conversation:**

> You're my obsidian formatting intern for today... Your job is to take this raw data and polish it up, according to a procedure... I will feed you the raw text from about two to three hours of class, after which you will provide me with an index of the contents... After you write the index up, with chapters, subchapters, and brief descriptions of each subchapter... I will then prompt you for each chapter individually.

**The length instruction, stated entirely in structural terms, no number given:**

> if we want the maximal density of knowledge, then we want the most chunks of data possible... I think you should aim for a decent, somewhat hefty paragraph of instructions and notes and editorial details for each paragraph, the more the merrier... I would rather twenty chapters where you in the future can say this isn't enough for a real hefty chapter but still have freedom to work within your per prompt token window than to make 10 chapters where you're consistently near the limit... Some of my notes will obviously be more sparse than others... you don't need to consistently be hitting 20 chapters or something, some of them will be shorter and that's fine

**A representative blueprint entry** (one of ten produced from an approximately 8,000-word raw transcript):

> Chapter 3: A Distinção entre Texto e Norma (O Precedente da "Casa"). Editor Notes for Future Generation: This section must be rich with examples. Explain the vital doctrinal difference between "Text" (the raw written law) and "Norm" (the result of interpretation). Anchor this heavily in the professor's primary example: Article 5, XI of the Federal Constitution (Inviolabilidade Domiciliar). Use an [!EXAMPLE] callout to detail the STF's expansive interpretation of the word "casa"... Use a [!CAUTION] callout to discuss normative complexity and ambiguity when facts arise that the legislator did not originally foresee.

That single paragraph of instruction, when executed, produced a full section: a named subsection distinguishing Texto from Norma, the constitutional article quoted, a worked example of the STF's expanded reading of "casa" across several contexts, and a closing callout on normative ambiguity, several hundred words of finished prose from roughly 90 words of brief. This ratio held consistently across all ten chapters and is the actual empirical basis for "detailed brief in, substantial prose out," not the number of words requested.
