# Public course site QA

Audit target: `courses/teoria-geral-dos-contratos/` (index, aulas 01–08, revisão P1). Initial pass inspected all ten pages, local references, duplicate IDs, content length, source/provenance language, SVG color declarations, and browser console output. Follow-up verification ran on 2026-09-24 after the requested fixes.

## Findings and follow-up status

- **P2 — Aula 08 phone overflow: resolved.** The CSS now constrains the mobile scrolly and stage widths and keeps horizontal scrolling inside the figure (`aula-08.html:44,51–52`). The parent’s updated 390 px browser measurement reports a 390 px document width. I could not independently rerun all ten viewport checks because the browser surface was unavailable in this subagent session; the course preview server remained reachable.
- **P3 — Review heading level: resolved.** The answer heading is now `h3` (`revisao-p1.html:60`). A static heading-level pass over all ten pages found no skipped heading levels.
- **Aulas 01–03 mobile diagrams: updated.** The mobile markup now gives each 600 px figure a focusable, labelled horizontal scroll region (`aula-01.html:13–17,46–47`; corresponding markup and rules are present in Aulas 02–03). This keeps diagram labels at their intended size and exposes arrow-key instructions.

No remaining concrete defects were found in this follow-up.

## Verification results and limits

- All ten HTML pages and `assets/curso.css` return HTTP 200 from the local preview. Static checks found no missing local files or fragments, duplicate IDs, or heading-level jumps.
- The initial browser pass found no console warnings or errors before these edits. The browser surface was unavailable for a fresh post-edit console or ten-page viewport pass; only the Aula 08 post-fix width result above was supplied by the parent.
- The initial pass found no visible backend, provenance, slide-deck, or gabarito language. Hits for “fonte(s)” are ordinary legal concepts (“fonte de deveres”, “fontes possíveis para a forma”); Aula 08 `data-slides` values are hidden metadata.
- No literal hex colors were found in SVG `fill`/`stroke` declarations; diagrams use CSS classes and variables. SVG glyph bounds were not exhaustively measured because page evaluation did not expose `getBBox()` for SVG text nodes.

## Orchestrator integration check after follow-up

Using the localhost browser at a 390×844 viewport after all listed edits, Codex opened `index`, `revisao-p1`, and `aula-01`–`aula-08`. Every page reported `document.documentElement.scrollWidth === innerWidth === 390`. Codex visually checked the updated phone diagrams in Aulas 01 and 05–08 and the review/index pages. These checks close the viewport limitation noted in the subagent's follow-up. The initial 1440px and console checks remain the desktop/error evidence.
