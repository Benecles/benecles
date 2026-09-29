# Tooling addendum

Applies from pass 2 onward. If pass 2 is already finished with hand-written SVG, this changes how the diagrams get authored on the next touch rather than requiring an immediate redo.

## Diagrams: author in mermaid, ship SVG

`mmdc` (mermaid-cli) is now installed globally and verified working. It is configured to use the system Chrome rather than downloading its own Chromium, so it needs a puppeteer config file:

```json
{ "executablePath": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "args": ["--no-sandbox", "--disable-gpu"] }
```

```
mmdc -p puppeteer.json -i diagram.mmd -o diagram.svg
```

Workflow: author the diagram as `.mmd`, compile to static SVG at build time, embed the SVG in the HTML. No runtime JavaScript, works in both the Chrome PDF path and EPUB.

**Why this is a rule and not a preference.** Hand-written SVG uses absolute coordinates. `<path d="M730 210 V255 H470"/>` cannot be verified by reading it, which is exactly how the conduct-branch diagram ended up asserting that coação física irresistível sits on the "had bodily control" branch while the table beneath it said the opposite. In mermaid that relationship is `Q -->|não| SEM` — readable, reviewable, and obviously wrong when it is wrong. The format removes an entire error class.

Suggested storage: keep `.mmd` sources next to the markdown they belong to (a `diagrams/` subfolder per course is fine), and have the build compile them. That way a diagram can be corrected by editing four words instead of recomputing coordinates.

Correct version of the conduct-branch diagram, for reference:

```
flowchart TD
    Q{"Houve controle corporal?"}
    Q -->|não| SEM["Ausência de conduta<br/>reflexo, convulsão, inconsciência,<br/>coação física irresistível"]
    Q -->|sim| PROX{"Qual é o problema seguinte?"}
    PROX --> TIPO["tipicidade e erro de tipo"]
    PROX --> JUST["antijuridicidade e justificação"]
    PROX --> CULP["culpabilidade<br/>coação moral irresistível<br/>afeta exigibilidade"]
```

## PDF path

Confirmed correct: Chrome headless print-to-pdf, which you had already moved to. Keep it. Do not go back to drawing into a PDF library's primitives.

## Linter

`tools/lint_study_packs.py` now exists. It checks em dashes, section numbering continuity, callout density and clustering, meta-commentary phrases, malformed tables, and diagrams that duplicate an adjacent table. It skips archived material and operator-facing scaffolding.

```
python3 tools/lint_study_packs.py "Coursework/<course>/luna_output"
```

**Run it on every file you touch, before reporting back.** It exits non-zero on ERROR-level findings. Warnings are advisory, not verdicts: a legitimately prose-heavy section can be under the callout threshold, and the meta-commentary check matches phrases that occasionally appear innocently. Use judgment on warnings, but do not leave errors.

Current state so you know what is pre-existing rather than yours: Controle has four section-numbering breaks (files 02, 13, 19, 20), and Teoria do Delito's four index files plus the un-rewritten Semana 15 still carry em dashes and inherited numbering breaks from the mechanical split. Metodologia Jurídica is clean.
