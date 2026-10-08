# Master brief · MOT-1: interaction motion that carries information (CEO, 05/10)

**Source of the idea:** fluidfunctionalism.com (chairman's find; a shadcn component library). Its thesis matches our mandate ("function, not description; signs over text"): *motion is information, not decoration*. We take the ideas, not the library (we are a static site with our own CSS; no React, no shadcn).

**What it is.** One shared interaction layer for every pointer target on the site, specified once and shown on a specimen page (`specimen/motion.html`, every state with the reason for it, per mandate #3).

**What it looks and feels like.**
1. **Hover as preview.** In a list of targets (the class register rows, the Latam front dialogue list, quiz `<details>`, bet options, endnav), a single paper-2 highlight *glides* to the row under the pointer instead of each row lighting up on its own. Moving down a list, the reader sees one slab travel and settle, so the row about to be clicked confirms itself before the click. Leaving the list, the slab fades in place, not snapping away.
2. **Grouping by merging.** Adjacent rows that belong together (a lesson's parts, a dialogue pair) share one continuous highlight when either is hovered: the motion says they belong together.
3. **Weight as approach.** Targets gain a little typographic weight on hover (for example 400 → 500 on the row title) through a variable font's weight axis, so text firms up as the pointer arrives. If our faces aren't variable, propose the swap or use the nearest equivalent (letter-spacing tightening is not a substitute; skip it rather than fake it).
4. **Springs, not durations.** Every one of these motions is interruptible: hover off mid-glide and the slab reverses from where it is. Three presets only (fast, moderate, slow), mapped to our existing calm motion register (the slow flag idle is the reference for "slow"). CSS `linear()` spring curves or a ~1 kB JS spring are both fine; pick by what stays interruptible.
5. **Keyboard parity.** Focus moves the same slab; focus-visible stays obvious.

**Where it sits:** `assets/` shared CSS/JS, used by all seven courses' fronts and lessons; the register specimen (`specimen/register.html`) updates to show it.

**What it must never do:** animate content the reader is reading (no moving paragraphs, no parallax, no scroll-jacking); add motion with no information (no idle bounces, no shimmer); delay a click; run under `prefers-reduced-motion` (then: instant highlight, no glide, no weight change); hurt reading on a slow laptop (transform/opacity only, no layout-thrashing properties). Desktop first (chairman rule 05/10): phones get the reduced version until desktop is perfect.

**Done when:** the specimen page shows every state; the register, the Latam front dialogue list, quiz items and bet options use it; check_all passes; a short screen recording or panel screenshots in the PR. The CEO gates the feel on desktop before it spreads to other components.
