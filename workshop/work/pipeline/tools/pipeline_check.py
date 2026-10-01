#!/usr/bin/env python3
"""Validate the CUFRGS source pipeline's S0–S4 stage artifacts.

Usage: pipeline_check.py {s0,s1,s2,s3,s4} COURSE [--workspace-root PATH]
       [--map PATH] [--shelf PATH] [--chapters PATH] [--triage PATH]
       [--compendium PATH] [--site PATH]

S1 shelf.csv columns: source_id, role, path, sha256, format, text_status,
and optional lesson_id (for a slide deck). A missing source uses text_status=missing.
S2 chapters/<source_id>/index.json has a chapters list; each item has id,
path, pdf_start, pdf_end, word_count. Text uses ===== p. N (PDF M) =====.
S3 triage.csv columns: source_id, chapter_id, lesson_id, role, why.
Roles are primary, supporting, background, unused, no_book_covers. The
no_book_covers row has lesson_id but no chapter_id; unused has chapter_id but
no lesson_id. A background row must be exactly the closure of prerequisite
lessons' primary chapter rows. Slide coverage comes from shelf.csv.

S3/S4 policy: supporting units are capped at 10,000 words each and 30,000
supporting words per lesson. An over-10,000-word supporting unit requires a
concrete `Specific need: ...` clause in `why`. Every lesson must receive at
least 5,000 primary words from the sources listed in bibliography.base.
basica_essencial; a shortfall requires a concrete lesson-level
`thin_primary_reason` in course-map.json. Primary rationales must connect to
the mapped syllabus line or learning outcome. Course maps may set
`policy.basica_essencial_source_ids` to exact shelf IDs; when absent, the
checker matches bibliography authors/titles to book_base shelf rows.
S4 also checks each generated 00-index.md, its file hashes and copied source
atoms. `--workspace-root` points to a checkout containing work/pipeline/ and
lets this checker validate a separate checkout without changing defaults.
"""

import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

WORKSHOP = Path(__file__).resolve().parents[3]
SITE = WORKSHOP.parent / "ordenacoes-filipinas"
MARKER = re.compile(r"^===== p\. (.+?) \(PDF (\d+)\) =====$", re.M)
SECTION_MARKER = re.compile(r"^===== § ([^=]+?) =====$", re.M)
ARTICLE_MARKER = re.compile(r"^===== Art\. ([^=]+?) =====$", re.M)
ROLES = {"primary", "supporting", "background", "unused", "no_book_covers"}
ASSIGNED_ROLES = {"primary", "supporting", "background"}
LEGAL_SOURCE_IDS = {"constituicao-federal-1988"}
LEGAL_SOURCE_PREFIXES = ("lei-",)
ARTICLE_ID = re.compile(r"^(?:ADCT )?Art\. (.+)$")
BODY_ARTICLE = re.compile(r"(?m)^\s*Art\.\s*([0-9]+(?:-[A-Z])?(?:º|°)?)(?![\w-])")
SPECIFIC_NEED = re.compile(r"\bSpecific need:\s*(.+)", re.I)
WORD_COUNT_MARKERS = (MARKER, SECTION_MARKER, ARTICLE_MARKER)
MIN_PRIMARY_WORDS = 5_000
MAX_SUPPORTING_ITEM_WORDS = 10_000
MAX_SUPPORTING_TOTAL_WORDS = 30_000
SIZE_EXEMPT_SOURCE_IDS = {
    "constituicao-federal-1988",
    "lei-9868-1999",
    "lei-9882-1999",
    "lei-11417-2006",
}
SIZE_EXEMPT_CHAPTERS = {
    ("mendes-branco-curso-2023", "04-direitos-fundamentais-em-especie"),
    ("mendes-branco-curso-2023", "11-tributacao-financas-publicas-e-controle-da-atividade-finance"),
    ("tavares-curso-2020", "61-chapter-lx-das-fun-es-essenciais-justi-a-e-da-pol-cia-judici-ria"),
    ("sarlet-marinoni-mitidiero-curso-2020", "14-direitos-fundamentais-em-especie"),
}
CORE_CHAPTER_WORD_LIMIT = 15_000
CHAPTER_WORD_LIMIT = 100_000


def read_json(path, errors):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        errors.append(f"cannot read JSON {path}: {exc}")
        return {}


def read_csv(path, errors):
    try:
        with path.open(newline="") as handle:
            return list(csv.DictReader(handle))
    except OSError as exc:
        errors.append(f"cannot read CSV {path}: {exc}")
        return []


def course_map(path, errors):
    data = read_json(path, errors)
    lessons = data.get("lessons", [])
    if not isinstance(lessons, list) or not lessons:
        errors.append("course map has no lessons")
        return []
    return lessons


def check_s0(args, errors):
    lessons = course_map(args.map, errors)
    live = args.site / "courses" / args.course
    pages = {p.name for p in live.glob("aula-*.html")}
    if not pages:
        errors.append(f"no live lesson pages found in {live}")
    ids = [lesson.get("id") for lesson in lessons]
    if len(ids) != len(set(ids)):
        errors.append("duplicate lesson IDs in course map")
    missing = sorted(pages - set(ids))
    extra = sorted(set(ids) - pages)
    if missing:
        errors.append("live pages absent from map: " + ", ".join(missing))
    if extra:
        errors.append("map IDs without live pages: " + ", ".join(map(str, extra)))
    positions = {lesson_id: i for i, lesson_id in enumerate(ids)}
    for i, lesson in enumerate(lessons):
        lesson_id = lesson.get("id", f"row {i+1}")
        for field in ("syllabus_line", "learning_outcome", "exam"):
            if not lesson.get(field):
                errors.append(f"{lesson_id}: missing {field}")
        prereqs = lesson.get("prerequisites", [])
        if not isinstance(prereqs, list):
            errors.append(f"{lesson_id}: prerequisites must be a list")
            continue
        for prereq in prereqs:
            target = prereq.get("id") if isinstance(prereq, dict) else None
            reason = prereq.get("reason") if isinstance(prereq, dict) else None
            if target not in positions:
                errors.append(f"{lesson_id}: unknown prerequisite {target}")
            elif positions[target] >= i:
                errors.append(f"{lesson_id}: prerequisite {target} does not point backward")
            if not reason:
                errors.append(f"{lesson_id}: prerequisite {target} lacks a reason")
    bibliography = read_json(args.map, []).get("bibliography", {})
    if not bibliography.get("base") or not bibliography.get("supplementary"):
        errors.append("bibliography must contain base and supplementary lists")
    return f"{len(lessons)} mapped / {len(pages)} live lessons"


def check_s1(args, errors):
    rows = read_csv(args.shelf, errors)
    if not rows:
        errors.append("shelf has no sources")
        return "0 sources"
    required = {"source_id", "role", "path", "sha256", "format", "text_status"}
    for n, row in enumerate(rows, 2):
        absent = sorted(required - row.keys())
        if absent:
            errors.append(f"shelf row {n}: missing columns {', '.join(absent)}")
            break
        if not row["source_id"] or not row["role"]:
            errors.append(f"shelf row {n}: source_id and role required")
        if row["text_status"] not in {"text layer", "OCR done", "needs OCR", "missing"}:
            errors.append(f"shelf row {n}: invalid text_status")
        if row["text_status"] != "missing" and not row["path"]:
            errors.append(f"shelf row {n}: available source lacks path")
    return f"{len(rows)} shelf sources"


def chapter_catalog(args, errors, validate_text):
    catalog = {}
    indexes = sorted(args.chapters.glob("*/index.json"))
    if not indexes:
        errors.append(f"no chapter indexes in {args.chapters}")
    for index_path in indexes:
        source_id = index_path.parent.name
        entries = read_json(index_path, errors).get("chapters", [])
        if not entries:
            errors.append(f"{source_id}: empty chapter index")
        # Section-split chapters can share a PDF page at a heading boundary.
        # Treat all children with one `parent` as a single page-span unit while
        # still validating every child's own marker sequence below.
        parent_groups = {}
        for entry in entries:
            if entry.get("locator", "page") != "page" or not entry.get("parent"):
                continue
            parent_groups.setdefault(entry["parent"], []).append(entry)
        page_units = []
        seen_parents = set()
        for entry in entries:
            if entry.get("locator", "page") != "page":
                continue
            parent = entry.get("parent")
            if parent:
                if parent in seen_parents:
                    continue
                seen_parents.add(parent)
                siblings = parent_groups[parent]
                spans = [(e.get("pdf_start"), e.get("pdf_end")) for e in siblings]
                spans = [(start, end) for start, end in spans if isinstance(start, int) and isinstance(end, int) and end >= start]
                if spans:
                    page_units.append((min(start for start, _ in spans), max(end for _, end in spans), parent))
            else:
                start, end = entry.get("pdf_start"), entry.get("pdf_end")
                if isinstance(start, int) and isinstance(end, int) and end >= start:
                    page_units.append((start, end, entry.get("id")))
        prior_end = None
        for start, end, chapter_id in page_units:
            if prior_end is not None and start != prior_end + 1:
                errors.append(f"{source_id}/{chapter_id}: gap or overlap after PDF {prior_end}")
            prior_end = end
        parent_markers = {}
        parent_ranges = {}
        for entry in entries:
            chapter_id = entry.get("id")
            key = (source_id, chapter_id)
            if not chapter_id or key in catalog:
                errors.append(f"{source_id}: absent or duplicate chapter id {chapter_id}")
                continue
            catalog[key] = entry
            if not validate_text:
                continue
            rel_path = entry.get("path", "")
            text_path = index_path.parent / rel_path
            try:
                content = text_path.read_text()
            except OSError as exc:
                errors.append(f"{source_id}/{chapter_id}: cannot read text: {exc}")
                continue
            locator = entry.get("locator", "page")
            if locator == "page":
                start, end = entry.get("pdf_start"), entry.get("pdf_end")
                if not isinstance(start, int) or not isinstance(end, int) or end < start:
                    errors.append(f"{source_id}/{chapter_id}: invalid PDF span")
                    continue
                markers = [int(m.group(2)) for m in MARKER.finditer(content)]
                if markers != list(range(start, end + 1)):
                    errors.append(f"{source_id}/{chapter_id}: page markers do not cover its PDF span continuously")
                parent = entry.get("parent")
                if parent:
                    parent_markers.setdefault(parent, set()).update(markers)
                    parent_ranges.setdefault(parent, []).append((start, end))
                body = MARKER.sub("", content)
            elif locator == "section":
                sections = [m.group(1).strip() for m in SECTION_MARKER.finditer(content)]
                if sections != [str(chapter_id)]:
                    errors.append(f"{source_id}/{chapter_id}: section marker does not match its index id")
                body = SECTION_MARKER.sub("", content)
            elif locator == "article":
                if not ARTICLE_MARKER.search(content):
                    errors.append(f"{source_id}/{chapter_id}: no article markers found")
                body = ARTICLE_MARKER.sub("", content)
            elif locator == "document":
                body = content
            else:
                errors.append(f"{source_id}/{chapter_id}: unsupported locator {locator}")
                continue
            actual_words = len(body.split())
            stated_words = entry.get("word_count")
            if not isinstance(stated_words, int) or actual_words < 1 or abs(actual_words - stated_words) > max(10, actual_words * 0.1):
                errors.append(f"{source_id}/{chapter_id}: implausible word count ({stated_words} stated, {actual_words} found)")
        for parent, spans in parent_ranges.items():
            expected = set(range(min(start for start, _ in spans), max(end for _, end in spans) + 1))
            if parent_markers.get(parent, set()) != expected:
                errors.append(f"{source_id}/{parent}: child page markers do not cover the parent span continuously")
    return catalog


def check_s2(args, errors):
    shelf = read_csv(args.shelf, errors)
    roles_by_source = {}
    for row in shelf:
        source_id = row.get("source_id", "")
        if source_id:
            roles_by_source[source_id] = row.get("role", "")
        if row.get("text_status") in {"text layer", "OCR done"}:
            if source_id and not (args.chapters / source_id / "index.json").is_file():
                errors.append(f"{source_id}: available shelf source has no chapter index")
    catalog = chapter_catalog(args, errors, True)
    entries_by_path = {}
    for (source_id, chapter_id), entry in catalog.items():
        rel_path = Path(entry.get("path", "")).as_posix()
        entries_by_path[(source_id, rel_path)] = (chapter_id, entry)

    # The 15k cap applies only to course-relevant section-split units in a
    # book_base source. Whole chapters outside the course remain whole.
    for (source_id, rel_path), (chapter_id, entry) in entries_by_path.items():
        if roles_by_source.get(source_id) != "book_base" or not entry.get("parent"):
            continue
        text_path = args.chapters / source_id / rel_path
        try:
            actual_words = len(text_path.read_text().split())
        except OSError as exc:
            errors.append(f"{source_id}/{rel_path}: cannot read text for size gate: {exc}")
            continue
        if actual_words > CORE_CHAPTER_WORD_LIMIT:
            errors.append(
                f"{source_id}/{rel_path}: section-split core chapter has {actual_words:,} words "
                f"(limit {CORE_CHAPTER_WORD_LIMIT:,}; chapter {chapter_id}, parent {entry['parent']})"
            )

    # The 100k cap applies to every chapter text file, including files not yet
    # listed in index.json. Exemptions are the named primary source texts and
    # four explicitly allowed non-core whole chapters.
    for text_path in sorted(args.chapters.rglob("*.txt")):
        try:
            source_id = text_path.relative_to(args.chapters).parts[0]
        except (ValueError, IndexError):
            continue
        if source_id in SIZE_EXEMPT_SOURCE_IDS:
            continue
        rel_path = text_path.relative_to(args.chapters / source_id).as_posix()
        indexed = entries_by_path.get((source_id, rel_path))
        if indexed and (source_id, indexed[0]) in SIZE_EXEMPT_CHAPTERS:
            continue
        try:
            actual_words = len(text_path.read_text().split())
        except OSError as exc:
            errors.append(f"{source_id}/{rel_path}: cannot read text for size gate: {exc}")
            continue
        if actual_words > CHAPTER_WORD_LIMIT:
            errors.append(
                f"{source_id}/{rel_path}: chapter text has {actual_words:,} words "
                f"(limit {CHAPTER_WORD_LIMIT:,})"
            )
    return f"{len(catalog)} indexed chapters"


def normalized_words(text):
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    ascii_text = "".join(char for char in decomposed if not unicodedata.combining(char))
    return set(re.findall(r"[a-z0-9]+", ascii_text))


def word_count(text):
    for marker in WORD_COUNT_MARKERS:
        text = marker.sub("", text)
    return len(text.split())


def concrete_explanation(text):
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    if len(words) < 8 or len(text.strip()) < 40:
        return False
    filler = {"a", "as", "ao", "aos", "com", "da", "das", "de", "do", "dos", "e", "em", "na", "no", "o", "os", "para", "por", "que", "se", "um", "uma", "needed", "necessary", "important", "relevant", "useful", "essential", "because", "this", "that"}
    return len(normalized_words(text) - filler) >= 5


def bibliography_authors(reference):
    author_line = reference.split(".", 1)[0]
    surnames = set()
    for author in author_line.split(";"):
        name = author.split(",", 1)[0].strip()
        tokens = normalized_words(name)
        if tokens:
            surnames.add(sorted(tokens)[-1])
    return surnames


def essential_source_ids(args, shelf_rows, errors):
    """Resolve essential bibliography references to book_base shelf IDs.

    Reusable exact override in course-map.json:
      "policy": {"basica_essencial_source_ids": ["source-id", ...]}
    Without it, match author surnames and distinctive title words against
    book_base IDs and source filenames. Multiple acquired editions may match.
    """
    course = read_json(args.map, errors)
    policy = course.get("policy", {}) if isinstance(course, dict) else {}
    explicit = policy.get("basica_essencial_source_ids") if isinstance(policy, dict) else None
    shelf_by_id = {row.get("source_id", ""): row for row in shelf_rows if row.get("source_id")}
    if explicit is not None:
        if not isinstance(explicit, list) or not explicit or not all(isinstance(item, str) and item for item in explicit):
            errors.append("policy.basica_essencial_source_ids must be a non-empty list of shelf source IDs")
            return set()
        for source_id in explicit:
            if source_id not in shelf_by_id:
                errors.append(f"policy.basica_essencial_source_ids references unknown shelf source {source_id}")
            elif shelf_by_id[source_id].get("role") != "book_base":
                errors.append(f"policy.basica_essencial_source_ids source {source_id} is not a book_base shelf item")
        return set(explicit)

    bibliography = course.get("bibliography", {}) if isinstance(course, dict) else {}
    base = bibliography.get("base", {}) if isinstance(bibliography, dict) else {}
    references = base.get("basica_essencial", []) if isinstance(base, dict) else []
    if not isinstance(references, list) or not references:
        errors.append("course map has no bibliography.base.basica_essencial list")
        return set()

    matched = set()
    for reference in references:
        authors = bibliography_authors(str(reference))
        title = str(reference).split(".", 2)[1] if "." in str(reference) else str(reference)
        generic = {"a", "as", "ao", "aos", "com", "da", "das", "de", "do", "dos", "e", "em", "na", "no", "o", "os", "para", "por", "um", "uma", "direito", "constitucional", "curso", "livro", "volume", "edicao", "edicoes", "esquematizado", "sao", "paulo", "editora", "saraiva", "malheiros", "juspubdivm", "isbn"}
        title_tokens = normalized_words(title) - generic - authors
        candidates = []
        for row in shelf_rows:
            if row.get("role") != "book_base":
                continue
            source_id = row.get("source_id", "")
            identity = normalized_words(source_id + " " + Path(row.get("path", "")).name)
            author_hits = authors & identity
            title_hits = title_tokens & identity
            if author_hits and (title_hits or not title_tokens):
                candidates.append(source_id)
        if not candidates:
            errors.append(f"cannot match essential bibliography reference to a book_base shelf source: {reference}")
        matched.update(candidates)
    return matched


SYLLABUS_STOP_WORDS = {
    "a", "as", "ao", "aos", "com", "da", "das", "de", "do", "dos", "e", "em", "na", "nas", "no", "nos", "o", "os", "para", "por", "que", "se", "um", "uma", "x",
    "aula", "aluno", "analisar", "aplicar", "avaliar", "compreender", "constitucional", "constitucionalidade", "constituição", "controle", "decidir", "direito", "distinguir", "explicar", "identificar", "norma", "órgão", "orgao", "verificar",
}


def primary_matches_syllabus(lesson, assignment):
    syllabus = normalized_words(str(lesson.get("syllabus_line", "")) + " " + str(lesson.get("learning_outcome", ""))) - SYLLABUS_STOP_WORDS
    rationale_and_title = normalized_words(assignment.get("why", "") + " " + assignment.get("title", ""))
    return bool(syllabus & rationale_and_title)


def validate_legal_atom(assignment, errors):
    source_id = assignment["source_id"]
    chapter_id = assignment["chapter_id"]
    entry = assignment.get("entry", {})
    content = assignment.get("content", "")
    if entry.get("locator") != "article":
        errors.append(f"{source_id}/{chapter_id}: legal source must use locator=article, not {entry.get('locator', 'page')}")
        return
    match = ARTICLE_ID.fullmatch(chapter_id)
    if not match:
        errors.append(f"{source_id}/{chapter_id}: legal chapter_id must be `Art. <exact label>` (or `ADCT Art. <exact label>` for ADCT)")
        return
    if chapter_id.startswith("ADCT Art. ") and source_id != "constituicao-federal-1988":
        errors.append(f"{source_id}/{chapter_id}: ADCT prefix is only valid for the Constituição Federal")
    markers = [marker.group(1).strip() for marker in ARTICLE_MARKER.finditer(content)]
    if len(markers) != 1:
        errors.append(f"{source_id}/{chapter_id}: legal atom must contain exactly one outer article marker (found {len(markers)})")
        return
    expected_label = match.group(1).strip()
    actual_label = markers[0]
    body_labels = {body.group(1).strip() for body in BODY_ARTICLE.finditer(content)}
    stale_cf_label = (
        source_id == "constituicao-federal-1988"
        and expected_label in {"167-D", "167-E", "167-F", "167-G"}
        and actual_label == "167"
    )
    if actual_label != expected_label and not stale_cf_label:
        errors.append(f"{source_id}/{chapter_id}: chapter_id does not match its exact article marker `Art. {actual_label}`")
    if stale_cf_label and expected_label not in body_labels:
        errors.append(f"{source_id}/{chapter_id}: stale outer Art. 167 marker lacks matching body heading Art. {expected_label}")
    if chapter_id.startswith("ADCT Art. ") and expected_label not in body_labels and not stale_cf_label:
        # ADCT atoms disambiguate repeated marker labels by their deterministic ID.
        # Their own heading must still be present so a main-text article cannot be relabeled ADCT.
        errors.append(f"{source_id}/{chapter_id}: ADCT atom lacks matching body heading Art. {expected_label}")


def check_assignment_policy(args, lessons, assignments, shelf_rows, errors):
    essential_ids = essential_source_ids(args, shelf_rows, errors)
    lesson_by_id = {lesson.get("id"): lesson for lesson in lessons}
    shelf_roles = {row.get("source_id", ""): row.get("role", "") for row in shelf_rows}
    support_totals = {lesson_id: 0 for lesson_id in lesson_by_id}
    primary_totals = {lesson_id: 0 for lesson_id in lesson_by_id}
    checked_legal_atoms = set()
    for assignment in assignments:
        role = assignment.get("role", "")
        if role not in ASSIGNED_ROLES:
            continue
        source_id = assignment.get("source_id", "")
        chapter_id = assignment.get("chapter_id", "")
        lesson_id = assignment.get("lesson_id", "")
        content = assignment.get("content", "")
        words = assignment.get("word_count")
        if words is None:
            words = word_count(content)
            assignment["word_count"] = words
        if shelf_roles.get(source_id) == "statute" or source_id in LEGAL_SOURCE_IDS or source_id.startswith(LEGAL_SOURCE_PREFIXES):
            legal_key = (source_id, chapter_id)
            if legal_key not in checked_legal_atoms:
                validate_legal_atom(assignment, errors)
                checked_legal_atoms.add(legal_key)
        if role == "supporting":
            support_totals[lesson_id] = support_totals.get(lesson_id, 0) + words
            if words > MAX_SUPPORTING_ITEM_WORDS:
                why = assignment.get("why", "")
                specific = SPECIFIC_NEED.search(why)
                if not specific or not concrete_explanation(specific.group(1)):
                    errors.append(
                        f"{lesson_id}: supporting item {source_id}/{chapter_id} has {words:,} words; over {MAX_SUPPORTING_ITEM_WORDS:,} requires `Specific need:` plus a concrete explanation"
                    )
        elif role == "primary":
            if source_id not in essential_ids:
                errors.append(f"{lesson_id}: primary {source_id}/{chapter_id} is not matched to bibliography.base.basica_essencial")
            elif not primary_matches_syllabus(lesson_by_id.get(lesson_id, {}), assignment):
                errors.append(f"{lesson_id}: primary {source_id}/{chapter_id} rationale/title does not match the mapped syllabus")
            else:
                primary_totals[lesson_id] = primary_totals.get(lesson_id, 0) + words

    for lesson_id, total in support_totals.items():
        if total > MAX_SUPPORTING_TOTAL_WORDS:
            errors.append(f"{lesson_id}: supporting assignments total {total:,} words (limit {MAX_SUPPORTING_TOTAL_WORDS:,})")
    for lesson in lessons:
        lesson_id = lesson.get("id", "unknown lesson")
        total = primary_totals.get(lesson_id, 0)
        if total >= MIN_PRIMARY_WORDS:
            continue
        reason = lesson.get("thin_primary_reason", "")
        if not isinstance(reason, str) or not concrete_explanation(reason):
            errors.append(
                f"{lesson_id}: only {total:,} matched essential-primary words; needs {MIN_PRIMARY_WORDS:,} or a concrete lesson-level thin_primary_reason"
            )


def triage_assignments(args, catalog, rows, errors):
    assignments = []
    for n, row in enumerate(rows, 2):
        if row.get("role") not in ASSIGNED_ROLES:
            continue
        source_id, chapter_id = row.get("source_id", ""), row.get("chapter_id", "")
        entry = catalog.get((source_id, chapter_id))
        if not entry:
            continue
        text_path = args.chapters / source_id / entry.get("path", "")
        try:
            content = text_path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"triage row {n}: cannot read text for {source_id}/{chapter_id}: {exc}")
            continue
        assignments.append({
            "source_id": source_id,
            "chapter_id": chapter_id,
            "lesson_id": row.get("lesson_id", ""),
            "role": row.get("role", ""),
            "why": row.get("why", ""),
            "title": entry.get("title", ""),
            "entry": entry,
            "content": content,
            "word_count": word_count(content),
        })
    return assignments


def check_s3(args, errors, warnings, run_policy=True):
    lessons = course_map(args.map, errors)
    ids = {lesson.get("id") for lesson in lessons}
    catalog = chapter_catalog(args, errors, False)
    rows = read_csv(args.triage, errors)
    if not rows:
        errors.append("triage has no rows")
    verdicts = set()
    primary = {lesson_id: set() for lesson_id in ids}
    background = {lesson_id: set() for lesson_id in ids}
    no_book = set()
    for n, row in enumerate(rows, 2):
        role = row.get("role", "")
        lesson_id = row.get("lesson_id", "")
        key = (row.get("source_id", ""), row.get("chapter_id", ""))
        if role not in ROLES:
            errors.append(f"triage row {n}: invalid role {role}")
        if not row.get("why"):
            errors.append(f"triage row {n}: missing reason")
        if role == "no_book_covers":
            if lesson_id not in ids or key != ("", ""):
                errors.append(f"triage row {n}: malformed no_book_covers note")
            no_book.add(lesson_id)
            continue
        if key not in catalog:
            errors.append(f"triage row {n}: unknown chapter {key}")
            continue
        if role == "unused":
            if lesson_id:
                errors.append(f"triage row {n}: unused chapter must have blank lesson_id")
            verdicts.add(key)
            continue
        if lesson_id not in ids:
            errors.append(f"triage row {n}: unknown lesson {lesson_id}")
            continue
        if role in {"primary", "supporting"}:
            verdicts.add(key)
        if role == "primary":
            primary[lesson_id].add(key)
        if role == "background":
            background[lesson_id].add(key)
    for key in catalog.keys() - verdicts:
        errors.append(f"chapter {key} has no primary/supporting/unused verdict")
    shelf = read_csv(args.shelf, errors)
    slides = {row.get("lesson_id") for row in shelf if row.get("role") == "slides" and row.get("text_status") != "missing"}
    slide_rows = {row.get("lesson_id") for row in shelf if row.get("role") == "slides"}
    for lesson in lessons:
        lesson_id = lesson.get("id")
        if lesson_id not in slides:
            lesson_number = re.search(r"aula-(\d+)", str(lesson_id))
            if lesson_number and 31 <= int(lesson_number.group(1)) <= 36:
                status = "missing slide source row" if lesson_id not in slide_rows else "slide deck marked unavailable"
                warnings.append(f"{lesson_id}: {status}; slide absence is permitted with warning")
            else:
                errors.append(f"{lesson_id}: no available slide deck in shelf")
        if not primary[lesson_id] and lesson_id not in no_book:
            errors.append(f"{lesson_id}: no primary book chapter or no_book_covers note")
        expected = set().union(*(primary.get(p.get("id"), set()) for p in lesson.get("prerequisites", [])))
        if background[lesson_id] != expected:
            errors.append(f"{lesson_id}: background differs from prerequisite primaries")
    assignments = triage_assignments(args, catalog, rows, errors)
    if run_policy:
        check_assignment_policy(args, lessons, assignments, shelf, errors)
    return f"{len(rows)} triage rows / {len(catalog)} chapters"


def split_markdown_row(line):
    return [cell.strip().replace("\\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def s4_role(role_cell):
    match = re.match(r"^(primary|supporting|background)(?:\b|$)", role_cell.strip())
    return match.group(1) if match else ""


def check_s4(args, errors, warnings):
    # Structural S3 checks remain prerequisites for S4, while the shared policy
    # below runs over the generated compendium atoms themselves.
    check_s3(args, errors, warnings, run_policy=False)
    lessons = course_map(args.map, errors)
    catalog = chapter_catalog(args, errors, False)
    triage_rows = read_csv(args.triage, errors)
    shelf = read_csv(args.shelf, errors)
    shelf_by_id = {row.get("source_id", ""): row for row in shelf if row.get("source_id")}
    lesson_ids = {lesson.get("id") for lesson in lessons}
    expected = {lesson_id: {} for lesson_id in lesson_ids}
    for row in triage_rows:
        role = row.get("role", "")
        lesson_id = row.get("lesson_id", "")
        if role not in ASSIGNED_ROLES or lesson_id not in expected:
            continue
        key = (row.get("source_id", ""), row.get("chapter_id", ""), role, row.get("why", ""))
        expected[lesson_id][key] = expected[lesson_id].get(key, 0) + 1

    policy_assignments = []
    checked_manifests = 0
    manifest_rows = 0
    for lesson in lessons:
        lesson_id = lesson.get("id", "")
        slug = Path(lesson_id).stem
        lesson_dir = args.compendium / slug
        index_path = lesson_dir / "00-index.md"
        if not index_path.is_file():
            errors.append(f"{lesson_id}: missing S4 manifest {index_path}")
            continue
        try:
            lines = index_path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            errors.append(f"{lesson_id}: cannot read S4 manifest: {exc}")
            continue
        checked_manifests += 1
        if not lines or lines[0] != f"# Compendium — {lesson_id}":
            errors.append(f"{lesson_id}: S4 manifest title does not match the course map")
        table_header = None
        found_slide_record = False
        listed_files = set()
        observed = {}
        for line in lines:
            if not line.startswith("|") or line.startswith("|---"):
                continue
            cells = split_markdown_row(line)
            if cells and cells[0] == "File":
                table_header = cells
                if cells != ["File", "Source", "Chapter", "Pages", "Role", "Why", "SHA-256"]:
                    errors.append(f"{lesson_id}: unexpected S4 manifest columns")
                continue
            if not table_header:
                continue
            if len(cells) != 7:
                errors.append(f"{lesson_id}: malformed S4 manifest row with {len(cells)} columns")
                continue
            file_name, source_id, chapter_id, _pages, role_cell, why, stated_digest = cells
            manifest_rows += 1
            relative = Path(file_name)
            if relative.is_absolute() or ".." in relative.parts or not relative.parts:
                errors.append(f"{lesson_id}: unsafe S4 file path in manifest: {file_name}")
                continue
            file_path = lesson_dir / relative
            if not file_path.is_file():
                errors.append(f"{lesson_id}: manifest file does not exist: {file_name}")
                continue
            listed_files.add(relative.as_posix())
            try:
                generated_bytes = file_path.read_bytes()
                generated_text = generated_bytes.decode("utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                errors.append(f"{lesson_id}: cannot read UTF-8 manifest file {file_name}: {exc}")
                continue
            actual_digest = hashlib.sha256(generated_bytes).hexdigest()
            if stated_digest != actual_digest:
                errors.append(f"{lesson_id}: SHA-256 mismatch for {file_name}")
            if role_cell.strip() == "slides":
                found_slide_record = True
            role = s4_role(role_cell)
            if not role:
                continue
            assignment_key = (source_id, chapter_id, role, why)
            is_pulled = role == "supporting" and "(pulled)" in role_cell.casefold()
            if assignment_key in expected[lesson_id]:
                observed[assignment_key] = observed.get(assignment_key, 0) + 1
            elif not is_pulled:
                errors.append(f"{lesson_id}: S4 manifest has unassigned {role} item {source_id}/{chapter_id}")

            entry = catalog.get((source_id, chapter_id))
            if entry is None:
                errors.append(f"{lesson_id}: S4 manifest references unknown chapter {source_id}/{chapter_id}")
                continue
            source_path = args.chapters / source_id / entry.get("path", "")
            try:
                source_bytes = source_path.read_bytes()
                source_text = source_bytes.decode("utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                errors.append(f"{lesson_id}: cannot read source atom {source_id}/{chapter_id}: {exc}")
                continue
            is_exercise = shelf_by_id.get(source_id, {}).get("role") in {"past_exam", "exercise", "exercises"} or bool(re.search(r"exam|exerc", source_id, re.I))
            if is_exercise:
                if source_text not in generated_text:
                    errors.append(f"{lesson_id}: S4 exercise file {file_name} does not contain its assigned source atom")
            elif source_bytes != generated_bytes:
                errors.append(f"{lesson_id}: S4 file {file_name} differs from source atom {source_id}/{chapter_id}")
            policy_assignments.append({
                "source_id": source_id,
                "chapter_id": chapter_id,
                "lesson_id": lesson_id,
                "role": role,
                "why": why,
                "title": entry.get("title", ""),
                "entry": entry,
                "content": generated_text,
                "word_count": word_count(generated_text),
            })

        if not table_header:
            errors.append(f"{lesson_id}: S4 manifest has no provenance table")
        if not found_slide_record:
            errors.append(f"{lesson_id}: S4 manifest has no slide provenance row")
        for assignment_key, expected_count in expected[lesson_id].items():
            actual_count = observed.get(assignment_key, 0)
            if actual_count != expected_count:
                errors.append(
                    f"{lesson_id}: S4 manifest has {actual_count} of {expected_count} expected {assignment_key[2]} rows for {assignment_key[0]}/{assignment_key[1]}"
                )
        try:
            actual_files = {path.relative_to(lesson_dir).as_posix() for path in lesson_dir.rglob("*") if path.is_file() and path != index_path}
            for unlisted in sorted(actual_files - listed_files):
                errors.append(f"{lesson_id}: S4 file is absent from manifest: {unlisted}")
        except OSError as exc:
            errors.append(f"{lesson_id}: cannot list S4 files: {exc}")

    check_assignment_policy(args, lessons, policy_assignments, shelf, errors)
    return f"{checked_manifests}/{len(lessons)} lesson manifests / {manifest_rows} provenance rows"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("s0", "s1", "s2", "s3", "s4"))
    parser.add_argument("course")
    parser.add_argument("--workspace-root", type=Path, default=WORKSHOP, help="checkout containing work/pipeline/ (default: checker checkout)")
    parser.add_argument("--map", type=Path)
    parser.add_argument("--shelf", type=Path)
    parser.add_argument("--chapters", type=Path)
    parser.add_argument("--triage", type=Path)
    parser.add_argument("--compendium", type=Path)
    parser.add_argument("--site", type=Path, default=SITE)
    args = parser.parse_args()
    root = args.workspace_root / "work" / "pipeline" / args.course
    args.map = args.map or root / "course-map.json"
    args.shelf = args.shelf or root / "shelf.csv"
    args.chapters = args.chapters or root / "chapters"
    args.triage = args.triage or root / "triage.csv"
    args.compendium = args.compendium or root / "compendium"
    errors = []
    warnings = []
    if args.stage == "s3":
        result = check_s3(args, errors, warnings)
    elif args.stage == "s4":
        result = check_s4(args, errors, warnings)
    else:
        result = {"s0": check_s0, "s1": check_s1, "s2": check_s2}[args.stage](args, errors)
    for warning in warnings:
        print("WARN:", warning)
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    if errors:
        print(f"{args.stage.upper()} FAIL: {len(errors)} error(s); {result}", file=sys.stderr)
        return 1
    print(f"{args.stage.upper()} PASS: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
