# Master brief · TYPE-1: expressive inline typography (CEO, 06/10)

**What the chairman asked.** Take more freedom with bold, italics and, above all, the things plain markdown can't do; use the house blue and orange in the text proper more often and in more interesting ways. Treat it as an investigation that ends in a specimen the chairman picks from, then a rollout.

**The rule that keeps it from becoming slop:** every typographic move *means* something the reader can learn once and then read at a glance. Colour is a legend, not decoration. Bold-for-emphasis is the measured AI tell (avoid-ai-writing; Writing Standard D8); bold-as-signal is not.

## The proposed vocabulary (CEO's direction; the specimen tests it)
| Mark | Means | Example |
|---|---|---|
| **Blue bold** (`--dif`) | what the court/law *decided*: the holding, the operative rule | "a Corte declarou **o estado de coisas inconstitucional**" |
| **Orange bold** (`--conc`) | the limit, the trap, what the decision did *not* do | "**não anulou o referendo**" |
| *Italics* | foreign terms, case names, works | *Gelman*, *chuzadas*, *Ley de Caducidad* |
| Small caps | court and organ names on first mention | CORTE CONSTITUCIONAL |
| Highlighter wash (paper marker, house colour at low opacity) | the one sentence per section worth memorising; at most one per chapter | — |
| Dotted underline + hover/tap card | a term of art, defined on the spot (ECI, *tutela*, *amparo*, repercussão geral) | — |
| Inline article chip (mono, hairline box) | a statute/article citation the reader may want to look up | `art. 23 CADH` |
| Party colour in comparisons | when two jurisdictions are compared in prose, each keeps its colour (e.g. Brasil blue, Colômbia orange) matching the figures | — |
| Tabular figures | votes, dates, sums in running text | 6 × 3 |
| Desktop sidenotes | asides that would otherwise be parentheses; in the margin the wide column leaves | — |

**Caps (per lesson):** blue bold ≤ 1 per paragraph and only on a holding; orange bold ≤ 1 per paragraph and only on a limit; highlighter ≤ 1 per chapter; no bold on anything else. Never colour a whole sentence of ordinary prose.

## Deliverables
1. `specimen/tipografia.html`: one real Latam passage (Aula 05 or 06, holdings + limits + a comparison) in three switchable intensities (restrained / proposed / bold), each mark with its reason. Night mode included (blue/orange must keep contrast ≥ 4.5:1 on both papers).
2. After the chairman picks: the shared CSS classes (`.held`, `.limit`, `.mark`, `.term`, `.art`, party classes), a `slop_lint` rule enforcing the caps, and a rollout on the Latam pages first (span-level, Writing Standard rules apply), then the other courses.
3. Writing Standard C10/D8 updated to the chosen vocabulary.

**Never:** colour as decoration; rainbow text; bold strings longer than ~6 words; marks that disagree with the figures' colour legend; anything that fails contrast in night mode.
