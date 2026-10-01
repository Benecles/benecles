# Flight log

Diagnostics from every launch (a shipped or gated piece of work), turned into rules that apply **immediately** to everything still in flight. This is the SpaceX loop:
- Rocket 1 flies.
- Its data changes rocket 2 before launch, rocket 3 while it's being built, and rocket 4 while it's still a design.

**Every agent, every stage:** read the entries newer than your last read before starting a stage. If an entry applies to work you already did and haven't shipped, fix it now. Don't wait for a gate to tell you.

**After every gate:** the CEO adds entries here: what failed or worked, the rule, which stages it applies to. One entry per finding, numbered, newest last. Rules here outrank older text in briefs.

Stages: `S0–S4` (sources), `S5a` (blueprint), `S5` (writing), `FIG` (figures, kit), `SHIP` (PRs, checks), `ALL`.

| # | Date | Launch | Finding | Rule | Applies to |
|---|---|---|---|---|---|
| F-001 | 01/10 | PIPE-2b gate | Lenza §6.10 held the rest of the book (692k words); S2 passed it | Section splits end at the book's own chapter end. S2 FAILs on core-book files > 15k and any file > 100k | S0–S4 |
| F-002 | 01/10 | PIPE-3 gate | Whole CF/88 (110k) attached to every lesson; Aula 01 primary was 1.2k | Statutes and the CF only by article. Supporting ≤ 10k/item, ≤ 30k/lesson; primary ≥ 5k from the básica essencial | S0–S4 |
| F-003 | 01/10 | LBL-1 gate | SVGs re-serialized through the DOM (`<path/>` → `<path></path>`, +83 KB) | Patch SVG attributes in place; text outside SVGs stays byte-identical | FIG, SHIP |
| F-004 | 01/10 | VIS-1 forensics | Good figures were built with a kit and given their own rounds; bad ones were hand-typed in bulk (8–26 elements) | Every figure comes from `tools/figkit/` and passes the Figure Library's 5-point test. No hand-typed SVG | FIG, S5 |
| F-005 | 01/10 | FIG-1 build | The 30/09 CSS forced every label to 14 px `!important`, breaking exact layouts | Kit SVGs carry `.figkit`; the course rule is `svg.fig:not(.figkit) text`. Never add blanket label CSS again | FIG |
| F-006 | 01/10 | FIG-1 build | Two-line labels at 12 px leading clashed; a ruler's limit line cut its title band | Kit leading is ≥ 14 px for mono labels and ≥ 18 px for serif lines. Lines skip text bands. The specimen probe must show 0 CROSS / 0 CLASH | FIG |
| F-007 | 01/10 | FIG-1 build | A timeline implied exact years (1993, 2008) where the lesson only says "anos 1990" / "mais recentemente" | Draw only the precision the text has: ordinal labels instead of invented dates | FIG, S5 |
| F-008 | 01/10 | FIG-1 build | Old aula 27 data didn't add up (7,714 ≠ 7,632 + 83) | Never chart numbers that fail their own arithmetic. Check sums before drawing | FIG, S5 |
| F-009 | 01/10 | Chairman | One composition for every screen; no phone variants | Don't build phone versions of figures | FIG |
| F-010 | 01/10 | VIS-2 | The catalogue was committed to the site repo | Workshop artifacts (catalogues, reports, scripts) live in the workshop repo; the site repo gets only what readers load, plus `tools/` | ALL |
