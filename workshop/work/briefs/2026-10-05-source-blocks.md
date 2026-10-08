# Master brief · SRC-1: source blocks (CEO → orchestrator, 05/10)

**What it is.** The chairman wants the site to carry large stretches of the books and decisions themselves, not only our reading of them. Policy: Writing Standard E2/E3 (rewritten 05/10). Think casebook/reader: our prose leads up to the point, stops, and the source speaks.

**What the reader sees.**
- Mid-chapter, the prose ends a sentence; below it a **source block** opens at full measure width: slightly different paper (paper-2), a rule on the left in the course accent, generous padding.
- **Header** in small caps mono: `AUTOR · *Obra* · cap. N, p. X` or `CORTE CONSTITUCIONAL DA COLÔMBIA · T-025/2004 · 22/01/2004`. Nothing else announces it.
- **Body** in the reading serif, same size as the prose, original paragraphing kept, `[…]` for cuts inside the stretch. Long blocks (300+ words) get a soft fade and "continuar lendo" after ~12 lines, expanding in place.
- Spanish blocks: a "traduzir" toggle under the block swaps to our Portuguese translation (marked as ours).
- Prose resumes directly below. No "como vimos".
- One component, one specimen page (`specimen/fonte.html`) with short, long, collapsed, expanded, Spanish and translated states and the reason for each.

**Where.** Pilot: Direito Latino-americano. Public-domain material first and heaviest (T-025 and Autos 176/008, T-153, Gelman, SCJ 20/2013, ADPF 153/347, SCP 0084/2017, OC-28, the constitutions), then doctrine already on disk (Engelmann & Bandeira, Gargarella, the course articles). Target: the passages a student would otherwise have to open the PDF for; a few blocks per lesson, more where the lesson is about a text.

**How the passages are chosen (orchestrator's HOW, CEO's WHAT):** from the compendium/chapter texts on disk (`work/pipeline/<course>/chapters`, `work/book-extracts/`), by a reader who knows the lesson's blueprint; each block's text is matched byte-for-byte (modulo whitespace) against its source file by script, so nothing is quoted from model memory. Locator goes in the header and in the private ledger.

**Also:** add `<meta name="robots" content="noindex, nofollow">` to every page and a `robots.txt` disallowing all (the chairman keeps the site among a small private group; it shouldn't surface in search).

**Never:** lead-in attribution in prose; blocks used as decoration or padding to hit length; paraphrase dressed as a quote; quoting what our sentence already says; touching figures, bets or quizzes.

**Done when:** component + specimen merged; Latam lessons carry their blocks with a match-check script passing; noindex live; check_all and breakscan 1280 pass; ISSUES line. The CEO gates the look of the block and the first lesson.
