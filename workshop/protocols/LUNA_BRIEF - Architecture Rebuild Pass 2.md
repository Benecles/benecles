# Luna brief: architecture rebuild, pass 2

Pass 1 worked on the bones. The six-part arc is there, the problem-first opening is real, the spine is stated, and the assembly section that was missing now exists. Keep all of that.

This pass fixes four things: one substantive error, two diagrams that aren't earning their place, structural bleed in the last two sections, and the PDF pipeline.

Same file: `Coursework/Teoria do Delito/luna_output/01 Semana 01 - Conceito analítico e arquitetura do delito.md`. Preserve the current version aside before editing, as always.

## 1. Fix the legal error in the conduct branch diagram

The third SVG (`Pontos de decisão nas exclusões de conduta`) is wrong in a way that contradicts the file's own text.

Both `coação física irresistível` and `coação moral irresistível` are drawn hanging off the **"sim, houve controle corporal"** branch. But coação física irresistível is the paradigm case of **absence of conduct** — the table directly below the diagram says "Ausência de conduta", and the prose after it says "A coação física irresistível elimina a conduta." The diagram asserts the opposite of the page it sits on.

Compounding it: "força física" already appears on the correct (não) branch inside the reflexo/convulsão box, so the same concept is drawn twice, on contradictory branches.

There is also a dead path: `<path class="ln" d="M730 210 V255 H730"/>` travels to its own x coordinate and renders nothing.

Redraw it so the logic is right: coação física irresistível belongs on the no-control side with the other conduct-defeating states; coação moral irresistível belongs on the control-present side, routed toward culpabilidade/exigibilidade. Then check the redrawn version against the table beneath it and confirm they agree.

**General rule from this:** a diagram is a legal assertion, not an illustration. Verify every branch against the prose and tables around it before shipping. If a diagram and a table disagree, one of them is wrong and it must be resolved, not left for the reader to notice.

## 2. Make the diagrams load-bearing

Two of the three diagrams currently show less than the text they accompany.

**The cascade diagram.** Immediately below it is "Leitura textual da cascata", a table with the same five stages and the same content. The diagram is a picture of the table. Meanwhile the paragraph after the table says something the diagram does not show at all: the cascade is not purely linear — a new fact about causality can knock out tipicidade, a justification can change the analysis of participation, an imputability condition can change the consequence without erasing the event. Those are backward edges, and they are the most interesting thing about the model.

Redraw it to show what the table cannot: the forward path, the exit at each stage, **and** the reopening edges that run backward. Then the table below it becomes a legend rather than a duplicate, and it can be shortened accordingly.

**The fato/norma/juízo diagram.** Three boxes in a row joined by two arrows conveys nothing a sentence doesn't. Either make it show something structural — for instance that the same fato under different normas yields different juízos, which is the actual teaching point of that section — or drop it. A weak diagram costs more than no diagram, because it trains the reader to skim past pictures.

## 3. Stop the bleed in sections 7 and 8

**Section 7 ("Limites do modelo e continuidade")** opens correctly on boundaries, then drifts. From "Uma resposta satisfatória não usa 'tripartido' como fórmula vazia" onward it becomes exam-answer guidance, then a "condições de revisão" table. Both are operational method and belong in section 6 with the roteiro and the recuperação questions. Move them there. Section 7 should end where the boundaries end: what this model does not decide, what is genuinely open, what the next weeks pick up.

**Section 8 ("Síntese")** re-lists the four action models, which were already tabled in 3.4, and re-states the don't-confuse pairs, already tabled in 4.5. That is restatement placed where summarizing feels traditional. A synthesis has to do something the body didn't. Two options that would work: compress the whole model into its shortest runnable form (the questions in order, nothing else), or run the model start to finish on one short unseen case so the reader watches the assembled thing work once. Pick one. Do not re-list.

Expect the file to get shorter in this pass. That is the correct direction here — the growth from 6,188 to 7,563 words was partly real (the new problem-framing and assembly sections) and partly this duplication.

## 4. Fix the PDF path: use Chrome, not ReportLab

Your finding is right and it is a blocker: raw SVG dumped as text into a PDF is worse than no diagram. But the fix is not adding SVG support to ReportLab.

The earlier build scripts for this corpus used **Chrome headless print-to-pdf**, which renders inline SVG and full CSS natively with no JavaScript dependency. That path also handles the callout styling (colored left borders, backgrounds, type labels) directly from the stylesheet instead of needing it reimplemented in a PDF library's drawing primitives.

Switch the PDF builder to Chrome headless. Roughly:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="<output>.pdf" "file://<rendered>.html"
```

Notes from prior use of this path in this corpus:
- Declare `background` directly on `@page` alongside the margin value, not only on `body`/`html`, or continuation pages lose the background in the margin box.
- Chrome prints stderr noise about `task_policy_set` on macOS; it is harmless, the file still writes. Check for the "bytes written" line rather than treating stderr as failure.
- Scope any `::first-letter` styling narrowly if used; a bare `p::first-letter` will catch subtitles and captions too.

Keep the EPUB path as is, since inline SVG already survives it.

Once switched, verify by rendering the Semana 1 PDF and confirming: the three diagrams appear as drawn graphics, the callouts appear as colored boxes with visible type distinction, and no raw markup is visible anywhere in the output.

## Standing rules, unchanged

- No meta-commentary about sources or pipeline access.
- No zero-information restatement.
- No em dashes.
- Callouts distributed through the body by function, roughly one per major section.
- Tables whenever three or more items share attributes.
- Every fact, citation, article number and case reference survives.

## When you're done

Stop again. One file. Don't touch Semanas 2 through 15 or the index files.

Report: word count before and after, what you cut in sections 7 and 8, the corrected branch logic in the conduct diagram, what the redrawn cascade diagram now shows that the table did not, whether you kept or dropped the fato/norma/juízo diagram and why, and confirmation that the Chrome PDF path renders diagrams and callouts correctly.
