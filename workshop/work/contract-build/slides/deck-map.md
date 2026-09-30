# Slide text corpus and lesson crosswalk

Extracted on 2026-09-24 with `pdftotext -layout`. The source PDFs in `/Users/benecles/Desktop/UFRGS 2026-2/Teoria Geral dos Contratos/` were read only. Each UTF-8 text file contains every selectable-text page, headed with the original PDF filename and its 1-based PDF page number.

## Deck inventory

| Original PDF | Pages | Topic span from page text | Extracted text |
|---|---:|---|---|
| `Slides - Aula 1 até 26.pdf` | 26 | Contract concept and legal characterization (pp. 1–21); consumer contracts and consumer/consumer-business definitions (pp. 22–26). | [`Slides - Aula 1 até 26.txt`](text/Slides%20-%20Aula%201%20at%C3%A9%2026.txt) |
| `Aula 2 - Slides 27 a 45.pdf` | 19 | Consumer contracts continued (pp. 1–5); principles: freedom, binding force, relativity, social function, objective good faith, equilibrium, lesion and synallagma (pp. 6–19). | [`Aula 2 - Slides 27 a 45.txt`](text/Aula%202%20-%20Slides%2027%20a%2045.txt) |
| `Slides Aula 3.pdf` | 31 | Principles continuation (pp. 1–7; pp. 2–7 repeat Aula 2 pp. 14–19); formation: proposal/acceptance, formation theories and place (pp. 8–28); negotiated formation and pre-contractual liability (pp. 29–31; p. 31 repeats Slides Aula 5 p. 1). | [`Slides Aula 3.txt`](text/Slides%20Aula%203.txt) |
| `Slides Aula 5 Moodle.pdf` | 16 | Pre-contractual liability (p. 1, duplicate); incidents: third-party beneficiary (pp. 2–5), promise of third-party act (pp. 6–8), person to be named (pp. 9–11), preliminary contract (pp. 12–15), arras (p. 16). | [`Slides Aula 5 Moodle.txt`](text/Slides%20Aula%205%20Moodle.txt) |
| `Moodle Aula 6.pdf` | 19 | Incidents: preliminary contract (p. 1, duplicate); arras (pp. 2–5, p. 2 near-duplicate); classifications: bilateral/unilateral (p. 6), onerous/free (p. 7), commutative/aleatory and related examples (pp. 8–19). | [`Moodle Aula 6.txt`](text/Moodle%20Aula%206.txt) |
| `Slides Exceção e Classificação.pdf` | 7 | Classifications: *exceptio non adimpleti contractus* (p. 1), insecurity exception (p. 2), consensual/formal/real (p. 3), negotiated/adhesion (p. 4), performance timing (p. 5), connected/main/accessory contracts (p. 6), typical/atypical (p. 7). | [`Slides Exceção e Classificação.txt`](text/Slides%20Exce%C3%A7%C3%A3o%20e%20Classifica%C3%A7%C3%A3o.txt) |

**Total:** 118 PDF pages across six source files. All six yielded selectable text; no OCR was used.

## Repeated page text and accounting

The audit-identified cross-deck exact repeats are:

- `Aula 2 - Slides 27 a 45.pdf` pp. 14–19 = `Slides Aula 3.pdf` pp. 2–7 (6 exact page-text matches).
- `Slides Aula 3.pdf` p. 31 = `Slides Aula 5 Moodle.pdf` p. 1 (1 exact match).
- `Slides Aula 5 Moodle.pdf` p. 15 = `Moodle Aula 6.pdf` p. 1 (1 exact match).
- `Slides Aula 5 Moodle.pdf` p. 16 and `Moodle Aula 6.pdf` p. 2 are a near-duplicate pair. Moodle Aula 6 p. 2 omits the two bullets “Regras sobre inadimplemento” and “Arras x cláusula penal” present on Aula 5 p. 16. Keep both source references; p. 16 carries those extra points.

Full extracted-text comparison also found identical page text within decks: Aula 1 pp. 4/5 and 8/9; Aula 5 pp. 6/7 and 13/14; Moodle Aula 6 pp. 16/17; Slides Aula 3 pp. 24/25. Together with the eight cross-deck exact matches above, this is 14 page instances beyond the first occurrence, leaving 104 distinct page-text bodies out of 118. This is a text-level count; identical extracted text does not establish that the visual pages are identical. The near-duplicate is not subtracted because it contains additional text on Aula 5 p. 16.

## Content-based crosswalk to lessons 01–08

Ranges refer to original PDF page numbers. “Canonical” identifies a convenient source for teaching content; repeated source pages remain in the corpus for traceability.

| Lesson | Content boundary from Claude's architecture brief | Slide page ranges |
|---|---|---|
| 01 — Concept and functions; contract in CC/CDC | Concept and economic operation through consumer definitions. | Canonical: Aula 1 pp. 1–26; Aula 2 pp. 1–5 adds consumer rights/abusive terms. |
| 02 — Principles I | Freedom, binding force and relativity/third-party effects. | Aula 2 pp. 6–10. |
| 03 — Principles II | Social function, objective good faith, equilibrium, lesion and synallagma. | Aula 2 pp. 11–19; equivalent continuation at Slides Aula 3 pp. 2–7. |
| 04 — Formation I | Contract process, phases, negotiations and pre-contractual liability. | Slides Aula 3 pp. 8–9 and 29–31; Aula 5 p. 1 repeats Aula 3 p. 31. |
| 05 — Formation II | Offer, acceptance, silence, time and place of formation. | Slides Aula 3 pp. 10–28. The page headings place public offer at p. 22, acceptance at p. 23, formation theories pp. 24–27, and place at p. 28. |
| 06 — Formation incidents | Third-party beneficiary, promise of third-party act, person to be named, preliminary contract and arras. | Aula 5 pp. 2–16; Moodle Aula 6 pp. 1–5 continues/repeats preliminary contract and arras. Treat Aula 5 p. 16 as fuller than Moodle Aula 6 p. 2. |
| 07 — Classification I | Bilateral/unilateral, exceptions, onerous/free and commutative/aleatory. | Moodle Aula 6 pp. 6–19; Slides Exceção e Classificação pp. 1–2 supplies *exceptio* and insecurity exception. |
| 08 — Classification II | Consensual/formal/real, principal/accessory, performance timing, adhesion, mixed/connected; relational/existential. | Slides Exceção e Classificação pp. 3–7 covers the first listed categories through typical/atypical. The requested six-deck set does not visibly cover mixed contracts or relational/existential contracts; the brief assigns those to other readings. |

## Boundary notes

- The split between lessons 02 and 03 is clearest within Aula 2: principles begin at p. 6; social function begins p. 11. Aula 3 starts mid-topic with a principles continuation label and duplicates Aula 2's good-faith/equilibrium run.
- The split between lessons 04 and 05 is less clean in Slides Aula 3. Formation begins p. 8, but proposal/acceptance occupies pp. 10–28 while negotiations and pre-contractual liability return at pp. 29–31. Allocate by page content, not contiguous ranges.
- The split between lessons 07 and 08 is clear by the content headings in Slides Exceção e Classificação: exceptions on pp. 1–2, then other classification axes from p. 3. Moodle Aula 6 pp. 6–19 mostly deepen lesson 07 and do not supply the lesson 08 axes listed in the brief.
- Lesson 01's conceptual material is concentrated in Aula 1, but consumer law resumes in Aula 2 pp. 1–5. The handoff from consumer contracts to principles is at Aula 2 p. 6.
