# newcourses-build: page layer for the courses built from drafts

`build.py` turns reviewed drafts into public CUFRGS pages for **Processo Civil I-a**, **Direito Constitucional I** and **Metodologia Jurídica** (cloud session, 2026-09-29).

- **Inputs:** `../course-drafts-2026-09-28/<course>/<packet>/draft.md` (or `case-dossier.md`) and one spec per lesson, `specs/<course>/<key>.json`: `date`, `pages[]` (`file`, `h1a`, `h1b`, `title`, `desc`, `deck`, `bet`, and `start` = the heading where page 2+ begins), `quiz[]`. Optional `specs/<course>/course.json` overrides prof/exam/scope. Spec rules: `SPEC-BRIEF.md`.
- **Course registry:** `COURSES` in `build.py` (slug, code, professor, exam, scope sentence, hero stations, and the lesson list `(key, packet, source file, highlighted stations, short label)`). A lesson appears on the site only if it is in this list and has a spec.
- **Rendering:** Markdown → house blocks (`##` = chapter, tables → `kit.table` in `.wide`, lists/`>` quotes into longform), one bet per page, quiz on the last page, endnav across the whole course, titleblock with reading time. Components come from `contract-build/generators/kit.py` and `latam-build/common.py`; assets are copied from the Latam course. The polish layer (`study-lab/tools/polish.py`) is applied after each write.
- **Run:** `python3 build.py [processo-civil|constitucional|metodologia]` (default: all). It then runs `tools/fontes_info.py` and `tools/offline_build.py`. It finds the study-lab checkout at the Mac publish path or `/home/user/study-lab`; override with `STUDY_LAB=/path`.
- **QA used in the cloud:** `contract-build/generators/qa.js` injected by Playwright at 1280 and 390 px, light and dark, plus a horizontal-overflow check; all pages clean at ship time.
- **Known gaps (design pass):** no genre figures or scrollies yet beyond the hero track; no cartões/revisão pages for these courses.
