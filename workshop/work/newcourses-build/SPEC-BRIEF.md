# Page-spec brief (cloud session, 2026-09-29)

Claude is turning finished drafts (`course-drafts-2026-09-28/<course>/<packet>/draft.md`) into public pages with one shared renderer. The renderer handles the body text. You write, per lesson, the **editorial pieces around it** as JSON: title lines, deck, meta description, one "bet" per page, and the recall quiz. Everything you write must be supported by that lesson's own draft (and its ledger); never add law, cases or facts that are not in the draft.

Read first: `/home/user/study-lab-private/Documents/Protocols/Writing Standard.md` (Parts C and D are binding for every string you write), and look at how a live page uses these pieces: `/home/user/study-lab/courses/direito-latino-americano/aula-09.html` (hero h1 in two lines, deck, the `.bet` block, the `.quiz` at the end). Its generator is `/home/user/study-lab-private/Documents/Codex/2026-09-23/you-h/work/latam-build/a09.py`.

## Output: one JSON file per lesson
Path: `/home/user/study-lab-private/Documents/Codex/2026-09-23/you-h/work/newcourses-build/specs/<course>/<key>.json`

```json
{
  "key": "08",
  "date": "23/09",
  "pages": [
    {
      "file": "aula-08.html",
      "h1a": "A resposta", "h1b": "do réu",
      "title": "Resposta do réu e contestação",
      "desc": "meta description in Portuguese, 140-160 characters, plain, no quotes",
      "deck": "One or two sentences (max ~40 words) that pose the page's question. You may wrap one or two key phrases in <strong class=\"dif\">…</strong> or <strong class=\"conc\">…</strong> (conc = trap/exam, dif = connection).",
      "bet": {
        "after_chapter": 1,
        "question": "A short concrete fact pattern taken from the draft's own examples, ending in a real decision.",
        "options": [["Option text", ""], ["Option text", "*"], ["Option text", ""]],
        "reveal": "<p>Two or three sentences explaining the right option with the rule from the draft.</p>"
      }
    }
  ],
  "quiz": [["Question?", "Answer in 1-3 sentences, from the draft."]]
}
```
- `h1a` + `h1b`: the page title split into two short lines (each ≤ ~22 characters), a plain noun phrase, no slogans, no question marks.
- `bet`: 3 or 4 options, exactly one marked `"*"` (the correct one); plausible wrong options that match real exam traps the draft warns about. `after_chapter` = the number of the `##` section after which it appears (1 = after the first section). One bet per page.
- `quiz`: 5 or 6 recall questions covering the whole lesson (all pages), answers self-contained.
- Portuguese (Brazil), house register. No em dashes. No visible sourcing (no page numbers, "segundo o texto", "o material"). Named authors are fine where the draft names them.

When done, run: `python3 -c "import json,glob;[json.load(open(f)) for f in glob.glob('/home/user/study-lab-private/Documents/Codex/2026-09-23/you-h/work/newcourses-build/specs/*/*.json')];print('ok')"` and then lint your prose by writing all deck/bet/quiz strings of each file to a temporary .md and running `python3 /home/user/study-lab-private/Documents/Protocols/tools/slop_lint.py <tmp.md>`; fix hits once. Write only in `specs/<course>/`. No git.

## Splitting long drafts (added)
If a draft (or dossier) runs over ~4,500 words, split it into two pages at the most natural `##` (or `#`) heading, roughly in the middle of the argument. Page 2 gets `"start": "<the exact heading text, without #>"` and its own file name (`aula-NN-<topic>.html`, a short slug). Drafts that already have two `#` parts split there. Never split a draft under ~4,500 words. Case dossiers are `aula-NN-casos.html`, one page unless over ~4,500 words.
Also: if you find visible source talk in the draft (sentences about "o material", "a ementa disponível", OCR, Moodle, what the sources do not say, "esta página"), list each one with its line number in your final message so Claude can remove it.
