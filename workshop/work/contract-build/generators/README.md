# Contratos page generators (Claude)

`kit.py` is the SVG/page kit; `lNN.py` builds `aula-NN.html`; `rev2.py` builds `revisao-p2.html`; `artigos.py` builds `artigos.html` (lesson links computed from the lesson text, so run it last).
`OUT` in each file points at the publishing checkout `work/study-lab-publish/courses/teoria-geral-dos-contratos/`.
Run with `python3 lNN.py` from this folder. Bump `VER` in kit.py when CSS/JS change (cache busting).
`qa.js` is the browser QA helper (`__check(document, window)`, `__runAll(pages, width)`); serve the checkout and eval it in the page.
`revisao-p1.html` and `index.html` are hand-edited HTML, not generated.
`cartoes.py` builds `cartoes.html` from the lesson quizzes; rerun it after changing any lesson quiz. `artigos.py` likewise after lesson text changes.
