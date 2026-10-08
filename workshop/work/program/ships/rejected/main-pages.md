Rejected by Claude 30/09 ~01:30. Redo with these rules:
1. HOME: no visible heading or deck. The owner removed "O semestre, desenhado." on purpose ("show, don't tell"; the shelf leads). Keep only the sr-only h1.
2. FRONTS are GENERATED: every change goes through R/d1/front.py and R/d1/data/<course>.json, and then `python3 R/d1/front.py <course>`. Hand edits to rendered index.html are lost at the next render and are not accepted.
3. Do NOT carry the REJECTED front drawings (ships/rejected/front-drawings.md): Const I, Processo and Controle fronts must keep their pre-front-drawings drawing state until the drawings redo is approved. Staging currently holds the rejected drawings; restore the previous drawing fields in the data JSON (R/program-old/front-drawings/ or the d1 data backups) before building on it.
4. Keep the exam card (Design Direction §4.4); don't replace it with a route. Unit cards follow the official syllabus units only: no invented "reader's map" groupings (Latam).
5. Reading guides, jump links, responsive fixes and markup repairs are welcome, done through the generator. Rewrite weak visible text to the Writing Standard.
