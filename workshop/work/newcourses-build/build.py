"""Page layer for the courses built from the 2026-09-28 draft queue (Constitucional I, Processo Civil I-a).

One renderer for every lesson: the reviewed draft.md (or case-dossier.md) is the body; the per-lesson spec JSON in
specs/<course>/<key>.json supplies title lines, deck, one bet per page and the recall quiz; each course has one hero
drawing whose highlight moves with the lesson. Components are the house ones (kit.py, latam common.py), so the pages
match the Latam and Contratos courses exactly.

    python3 build.py [constitucional|processo-civil ...]      # default: all courses

Paths are relative to this file, so it runs both on the Mac and in a cloud checkout of study-lab-private
(set STUDY_LAB to the study-lab checkout if it is not the default)."""
import html as H, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(HERE)
DRAFTS = os.path.join(WORK, 'course-drafts-2026-09-28')
SITE = os.environ.get('STUDY_LAB') or next(p for p in [
    os.path.join(WORK, '..', '..', '..', '2026-09-05', 'okay-couple-things-so-first-of', 'work', 'study-lab-publish'),
    '/home/user/study-lab'] if os.path.isdir(os.path.join(p, 'courses')))
SITE = os.path.abspath(SITE)

sys.path.insert(0, os.path.join(WORK, 'contract-build', 'generators'))
sys.path.insert(0, os.path.join(WORK, 'latam-build'))
sys.path.insert(0, os.path.join(SITE, 'tools'))
import kit
import common as latam            # longform(), lex(), bet(), EXTRA_CSS: the Latam lesson components
from polish import apply_polish as _polish
kit.apply_polish = lambda p: _polish(p, quiet=False)
kit.VER = '20260927h'

# ---------------------------------------------------------------- markdown → house blocks
def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<em>\1</em>', t)
    t = re.sub(r'(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])', r'<em>\1</em>', t)
    t = re.sub(r'"([^"<>]+)"', '\u201c\\1\u201d', t)   # house style: curly quotes
    return t.replace(' -- ', ', ')

def parse(md):
    """→ list of ('h1'|'h2'|'h3', text) and ('p'|'ul'|'ol'|'table'|'quote', payload)."""
    out, lines, i = [], md.split('\n'), 0
    while i < len(lines):
        s = lines[i].rstrip()
        if not s.strip():
            i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', s)
        if m:
            lvl = min(len(m.group(1)), 3)
            out.append((f'h{lvl}', m.group(2).strip())); i += 1; continue
        if s.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
                    rows.append(cells)
                i += 1
            out.append(('table', rows)); continue
        if re.match(r'^\s*([-*]|\d+[.)])\s+', s):
            kind = 'ol' if re.match(r'^\s*\d+[.)]\s+', s) else 'ul'
            items = []
            while i < len(lines) and lines[i].strip():
                l = lines[i]
                mm = re.match(r'^\s*([-*]|\d+[.)])\s+(.*)$', l)
                if mm: items.append(mm.group(2).strip())
                elif items: items[-1] += ' ' + l.strip()
                i += 1
            out.append((kind, items)); continue
        if s.startswith('>'):
            q = []
            while i < len(lines) and lines[i].startswith('>'):
                q.append(lines[i].lstrip('>').strip()); i += 1
            out.append(('quote', ' '.join(q))); continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,4}\s|\s*\||\s*([-*]|\d+[.)])\s|>)', lines[i]):
            para.append(lines[i].strip()); i += 1
        out.append(('p', ' '.join(para)))
    return out

def render_table(rows):
    head, body = rows[0], rows[1:]
    if not body:
        body, head = [head], [''] * len(head)
    n = len(head)
    body = [(r + [''] * n)[:n] for r in body]
    return kit.wide(kit.table([inline(h) for h in head], [[inline(c) for c in r] for r in body]))

def render_blocks(blocks):
    """Paragraph-level blocks → longform flow; tables break out to the wide column."""
    html, flow = '', []
    def flush():
        nonlocal html
        if flow: html += latam.longform(*flow); flow.clear()
    for kind, x in blocks:
        if kind == 'p': flow.append(f'<p>{inline(x)}</p>')
        elif kind == 'h3': flow.append(f'<h3>{inline(x)}</h3>')
        elif kind in ('ul', 'ol'): flow.append(f'<{kind}>' + ''.join(f'<li>{inline(it)}</li>' for it in x) + f'</{kind}>')
        elif kind == 'quote': flow.append(latam.lex('Texto', inline(x)))
        elif kind == 'table': flush(); html += render_table(x)
    flush()
    return html

EXAM = re.compile(r'^(para a prova|síntese para a prova|armadilhas)', re.I)

def sections(blocks):
    """Split at h2 (h1s inside a draft are part titles, handled by the page split). → [(title|None, blocks)]"""
    secs, cur = [], [None, []]
    for b in blocks:
        if b[0] == 'h2' or (b[0] == 'h1' and EXAM.match(b[1])):
            if cur[0] is not None or cur[1]: secs.append(cur)
            cur = [b[1], []]
        elif b[0] == 'h1':
            continue
        else:
            cur[1].append(b)
    if cur[0] is not None or cur[1]: secs.append(cur)
    return secs

def split_pages(blocks, starts):
    """starts: heading texts (any level) at which pages 2..n begin."""
    pages, cur = [], []
    targets = list(starts)
    for b in blocks:
        if targets and b[0] in ('h1', 'h2', 'h3') and b[1].strip().lower().startswith(targets[0].lower()):
            pages.append(cur); cur = []; targets.pop(0)
        cur.append(b)
    pages.append(cur)
    assert not targets, f'page split marker not found: {targets}'
    return pages

# ---------------------------------------------------------------- page assembly
def words(blocks):
    n = 0
    for k, x in blocks:
        if isinstance(x, str): n += len(x.split())
        elif k == 'table': n += sum(len(c.split()) for r in x for c in r)
        else: n += sum(len(i.split()) for i in x)
    return n

def bet_html(b):
    return latam.bet(b['question'], [(t, '*' if w.startswith('*') else '') for t, w in b['options']], b['reveal'],
                     kicker='Antes de ler: como você decidiria?')

def body_html(blocks, spec_page, quiz=None, first_num=1):
    b, n = '', first_num
    secs = sections(blocks)
    bet = spec_page.get('bet')
    if bet and bet.get('after_chapter') == 0:
        b += bet_html(bet); bet = None
    for idx, (title, bl) in enumerate(secs):
        if title is None:
            b += render_blocks(bl); continue
        exam = bool(EXAM.match(title))
        b += kit.chapter(f'{n:02d}', f'c{n}', inline(title), '', 'conc' if exam else ('dif' if n % 2 else ''))
        b += render_blocks(bl)
        if bet and bet.get('after_chapter') == n - first_num + 1:
            b += bet_html(bet); bet = None
        n += 1
    if bet: b += bet_html(bet)
    if quiz:
        b += kit.chapter(f'{n:02d}', f'c{n}', 'Teste', 'Responda antes de abrir.', 'conc')
        b += kit.quiz([(inline(q), inline(a)) for q, a in quiz])
    return b, n

# ---------------------------------------------------------------- course heroes
def track(stations, current, done, quiet=False):
    """A horizontal procedure/timeline: stations [(label, sub)], current: set of indexes, done: indexes before."""
    k = len(stations)
    x0, x1 = 70, 1010
    xs = [x0 + i * (x1 - x0) / (k - 1) for i in range(k)]
    cur = sorted(current)
    o = f'<path d="M{x0} 72H{x1}" style="fill:none;stroke:var(--grid-major);stroke-width:3"/>'
    if cur and not quiet:
        o += f'<path class="draw" d="M{x0} 72H{xs[cur[-1]]:.0f}" style="fill:none;stroke:var(--ink);stroke-width:3"/>'
    for i, (x, (a, sub)) in enumerate(zip(xs, stations)):
        on, past = i in current, i < (cur[0] if cur else 0)
        if quiet: on, past = False, True
        col = 'var(--conc)' if on else ('var(--ink)' if past else 'var(--ink-2)')
        r = 11 if on else 7
        fill = col if (on or past) else 'var(--paper)'
        o += (f'<g class="pop" style="--d:{.15 + i * .12:.2f}s;font:12px var(--mono);letter-spacing:.06em">'
              f'<circle cx="{x:.0f}" cy="72" r="{r}" style="fill:{fill};stroke:{col};stroke-width:2"/>'
              + (f'<circle cx="{x:.0f}" cy="72" r="18" style="fill:none;stroke:var(--conc);stroke-width:1"/>' if on else '')
              + f'<text x="{x:.0f}" y="{30 if i % 2 == 0 else 114}" text-anchor="middle" style="fill:{col};font-weight:{700 if on else 500}">{a}</text>'
              f'<text x="{x:.0f}" y="{46 if i % 2 == 0 else 131}" text-anchor="middle" style="fill:var(--ink-2);font-size:11px">{sub}</text></g>')
    return o

PC_STATIONS = [('PETIÇÃO', 'demanda'), ('LIMINAR', 'e audiência'), ('SUJEITOS', 'partes e terceiros'), ('ATOS', 'citação e prazos'),
               ('RESPOSTA', 'contestação'), ('SANEAMENTO', 'nulidades'), ('SENTENÇA', 'julgamento')]
CI_STATIONS = [('1787 · 1791', 'EUA e França'), ('1824', 'Império'), ('1891', 'República'), ('1934', 'social'), ('1937', 'Estado Novo'),
               ('1946', 'redemocratização'), ('1967 · 69', 'regime militar'), ('1988', 'Cidadã')]

MJ_STATIONS = [('SÉC. XII', 'escolas medievais'), ('SÉC. XVI', 'humanismo'), ('CASUÍSMO', 'o caso e o sistema'), ('AMÉRICA', 'prática colonial'),
               ('LITERATURA', 'pragmática'), ('COSTUME', 'direito indiano'), ('SÉC. XIX', 'ensino jurídico'), ('HOJE', 'dogmática')]

# ---------------------------------------------------------------- course definitions
# (key, packet dir, source file, [page files], [split markers for pages 2..n], hero highlight, short label)
COURSES = {
    'processo-civil': dict(
        slug='processo-civil-i', course='Processo Civil I-a', code='DIR02002', prof='Prof. Eduardo Scarparo',
        kick=['Processo Civil I-a', 'DIR02002', 'UFRGS · 2026/2'], stations=PC_STATIONS, exam=('P1', '07/10/2026'),
        scope='A P1 cobre as Aulas 01 a 09. As Aulas 10 e 11, sobre saneamento e julgamento conforme o estado do processo, são dadas depois da prova.',
        lessons=[
            ('01', 'unit-01-petition-demand-amendment', 'draft.md', {0}, 'Petição inicial'),
            ('02', 'unit-02-preliminary-dismissal-hearing', 'draft.md', {1}, 'Improcedência liminar e audiência'),
            ('03', 'unit-03-integrated', 'draft.md', {2}, 'Partes e litisconsórcio'),
            ('04', 'unit-04-intervention-assistance', 'draft.md', {2}, 'Assistência'),
            ('05', 'unit-05-intervention-impleader-other', 'draft.md', {2}, 'Denunciação e outras intervenções'),
            ('05c', 'unit-05-intervention-impleader-other-cases', 'case-dossier.md', {2}, 'Casos de denunciação'),
            ('06', 'unit-06-procedural-acts-service', 'draft.md', {3}, 'Atos, citação e intimação'),
            ('07', 'unit-07-deadlines-preclusion', 'draft.md', {3}, 'Prazos e preclusão'),
            ('08', 'unit-08-defendant-response', 'draft.md', {4}, 'Resposta do réu'),
            ('08r', 'unit-15-counterclaim-default', 'draft.md', {4}, 'Reconvenção e revelia'),
            ('09', 'unit-09-nullities', 'draft.md', {5}, 'Nulidades'),
            ('10', 'unit-10-case-management', 'draft.md', {5}, 'Julgamento conforme o estado e saneamento'),
            ('11', 'unit-11-judgments-partial-merits', 'draft.md', {6}, 'Sentença, extinção e mérito'),
        ]),
    'constitucional': dict(
        slug='direito-constitucional-i', course='Direito Constitucional I', code='DIR03045', prof='Profa. Roberta Baggio',
        kick=['Direito Constitucional I', 'DIR03045', 'UFRGS · 2026/2'], stations=CI_STATIONS, exam=('Prova', '05/10/2026'),
        scope='A prova de 05/10 cobre as Aulas 01 a 04, com o caso da ADI 3.345.',
        lessons=[
            ('01', 'unit-01-history-origins', 'draft.md', {0}, 'Origens do constitucionalismo'),
            ('02', 'unit-02-constitution-types', 'draft.md', {1, 7}, 'Classificação das constituições'),
            ('03', 'unit-03-brazilian-constitutionalism', 'draft.md', {1, 2}, 'Formação constitucional do Brasil'),
            ('04', 'unit-04-force-supremacy-guardian', 'draft.md', {7}, 'Supremacia e guarda da Constituição'),
            ('04c', 'unit-04-force-supremacy-guardian-cases', 'case-dossier.md', {7}, 'Caso: ADI 3.345'),
            ('05', 'unit-05-constituent-power', 'draft.md', {7}, 'Poder constituinte'),
            ('06', 'unit-06-reform-limits', 'draft.md', {7}, 'Reforma e seus limites'),
            ('06c', 'unit-06-reform-limits-cases', 'case-dossier.md', {7}, 'Casos: limites da reforma'),
            ('07', 'unit-07-efficacy-applicability', 'draft.md', {7}, 'Eficácia e aplicabilidade'),
            ('08', 'unit-08-rules-principles', 'draft.md', {7}, 'Regras e princípios'),
            ('09', 'unit-09-principled-application-limits', 'draft.md', {7}, 'Aplicação dos princípios'),
            ('10', 'unit-10-norms-over-time-reception', 'draft.md', {7}, 'Normas no tempo e recepção'),
            ('11', 'unit-11-norms-in-space-international-rights', 'draft.md', {7}, 'Normas no espaço e tratados'),
            ('12', 'unit-12-rights-concept-evolution', 'draft.md', {7}, 'Direitos fundamentais: conceito'),
            ('13', 'unit-13-rights-catalogue', 'draft.md', {7}, 'O catálogo de direitos'),
            ('14', 'unit-14-rights-functions-holders', 'draft.md', {7}, 'Funções e titulares'),
            ('15', 'unit-15-rights-applicability-horizontal-effect', 'draft.md', {7}, 'Aplicabilidade e eficácia horizontal'),
            ('16', 'unit-16-rights-limits', 'draft.md', {7}, 'Limites dos direitos'),
            ('17', 'unit-17-rights-religion-conscience', 'draft.md', {7}, 'Religião e consciência'),
            ('18', 'unit-18-rights-expression', 'draft.md', {7}, 'Liberdade de expressão'),
            ('19', 'unit-19-rights-information', 'draft.md', {7}, 'Direito à informação'),
            ('20', 'unit-20-rights-property', 'draft.md', {7}, 'Propriedade'),
            ('21', 'unit-21-rights-sexual-liberty', 'draft.md', {7}, 'Liberdade sexual'),
            ('21c', 'unit-21-rights-sexual-liberty-cases', 'case-dossier.md', {7}, 'Casos: ADPF 132 e RE 778.889'),
            ('22', 'unit-22-rights-social-enforceability', 'draft.md', {7}, 'Direitos sociais'),
            ('23', 'unit-23-rights-housing', 'draft.md', {7}, 'Moradia'),
            ('24', 'unit-24-rights-environment', 'draft.md', {7}, 'Meio ambiente'),
            ('25', 'unit-25-rights-indigenous-identity', 'draft.md', {7}, 'Identidade indígena'),
        ]),
    'metodologia': dict(
        slug='metodologia-juridica', course='Metodologia Jurídica', code='DIR03044', prof='',
        kick=['Metodologia Jurídica', 'DIR03044', 'UFRGS · 2026/2'], stations=MJ_STATIONS, exam=None,
        scope='Estas são as aulas cujos textos já foram publicados no Moodle; as Aulas 10 a 13 entram quando os textos forem postados.',
        lessons=[
            ('01', 'lesson-01', 'draft.md', {0}, 'Escolas jurídicas medievais'),
            ('02', 'lesson-02', 'draft.md', {1}, 'Recepção e humanismo'),
            ('03', 'lesson-03', 'draft.md', {2}, 'Casuísmo e sistema I'),
            ('04', 'lesson-04', 'draft.md', {3}, 'Prática jurídica colonial'),
            ('05', 'lesson-05', 'draft.md', {4}, 'Literatura normativa pragmática'),
            ('06', 'lesson-06', 'draft.md', {3}, 'O jurista hispano-colonial'),
            ('07', 'lesson-07', 'draft.md', {5}, 'O costume no direito indiano'),
            ('08', 'lesson-08', 'draft.md', {2}, 'Casuísmo e sistema II'),
            ('09', 'lesson-09', 'draft.md', {2}, 'Casuísmo e sistema III'),
            ('14', 'lesson-14', 'draft.md', {6}, 'Educação jurídica no Brasil'),
            ('15b', 'lesson-15b', 'draft.md', {7}, 'Relação e norma'),
        ]),
}
EXTRA = '@media (max-width:560px){.hero h1{hyphens:auto;-webkit-hyphens:auto;overflow-wrap:break-word}}'
PAGE_HIGHLIGHT = {('constitucional', 'aula-03-republica.html'): {3, 4, 5, 6, 7}}

def build(cname):
    C = dict(COURSES[cname])
    cj = os.path.join(HERE, 'specs', cname, 'course.json')
    if os.path.exists(cj):
        j = json.load(open(cj))
        if j.get('prof'): C['prof'] = j['prof']
        if j.get('exam'): C['exam'] = ('Prova', j['exam'])
        if j.get('exam_scope'): C['scope'] = j['exam_scope']
    out = os.path.join(SITE, 'courses', C['slug']) + '/'
    os.makedirs(out + 'assets', exist_ok=True)
    for a in ('curso.css', 'curso.js'):
        src = os.path.join(SITE, 'courses', 'direito-latino-americano', 'assets', a)
        open(out + 'assets/' + a, 'w').write(open(src).read())
    kit.OUT, kit.COURSE = out, C['course']
    specs = {k: json.load(open(os.path.join(HERE, 'specs', cname, f'{k}.json'))) for k, *_ in C['lessons']}
    # flat page sequence for prev/next
    seq = []
    for key, pdir, srcf, hl, short in C['lessons']:
        for pg in specs[key]['pages']:
            seq.append((key, pg['file'], pg))
    index = []
    for key, pdir, srcf, hl, short in C['lessons']:
        sp = specs[key]
        files = [pg['file'] for pg in sp['pages']]
        starts = [pg['start'] for pg in sp['pages'][1:]]
        md = open(os.path.join(DRAFTS, cname, pdir, srcf)).read()
        blocks = parse(md)
        pages = split_pages(blocks, starts)
        assert len(pages) == len(files) == len(sp['pages']), (key, len(pages), len(files), len(sp['pages']))
        num = 1
        for pi, (f, pblocks) in enumerate(zip(files, pages)):
            pg = sp['pages'][pi]
            last = pi == len(files) - 1
            body, num = body_html(pblocks, pg, sp.get('quiz') if last else None, num)
            j = next(i for i, s in enumerate(seq) if s[1] == f)
            prev = ('index.html', '← Curso', C['course']) if j == 0 else (seq[j - 1][1], '← ' + label_of(seq[j - 1]), seq[j - 1][2]['title'])
            nxt = ('index.html', 'Curso →', 'Todas as aulas') if j == len(seq) - 1 else (seq[j + 1][1], label_of(seq[j + 1]) + ' →', seq[j + 1][2]['title'])
            mins = max(5, round(words(pblocks) / 200))
            part = f' · {pi + 1}/{len(files)}' if len(files) > 1 else ''
            tb = [('Aula', f"{sp['date']} · {short}{part}"), ('Leitura', f'≈ {mins} min'),
                  ('Antes', prev[2] if j else 'Início do curso'), ('Depois', nxt[2])]
            hero = track(C['stations'], PAGE_HIGHLIGHT.get((cname, f), hl), set())
            kit.page(f, key, pg['title'], pg['desc'], C['kick'], pg['h1a'], pg['h1b'], pg['deck'], hero, tb, body, prev, nxt,
                     extra_css=latam.EXTRA_CSS + EXTRA, toplabel=f"{label_of((key, f, pg))} · {sp['date']}")
            index.append((key, f, pg, sp['date'], short, mins))
    front(C, index)
    return index

def label_of(s):
    key, f, pg = s
    base = 'Aula ' + re.sub(r'\D', '', key)
    if f.endswith('-casos.html'): return base + ' · casos'
    if re.search(r'aula-\d+-[a-z]', f): return base + ' · II'
    return base

# ---------------------------------------------------------------- course front
def front(C, index):
    src = open(os.path.join(SITE, 'courses', 'direito-latino-americano', 'index.html')).read()
    head = src[:src.find('<body')]
    head = re.sub(r'<title>.*?</title>', f"<title>{C['course']} · CUFRGS</title>", head, flags=re.S)
    desc = f"Guia de estudo de {C['course']} ({C['code']}), UFRGS 2026/2: aulas na ordem do programa, com casos, quadros e testes."
    head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', head)
    head = re.sub(r'<!-- FONTES:START -->.*?<!-- FONTES:END -->', '', head, flags=re.S)
    head = head.replace('</style>', '.front-track{margin:8px auto 0;max-width:1180px;padding:0 clamp(16px,4vw,48px)}'
                        '.front-track svg{width:100%;height:auto;display:block}.front-track .note{font:12px var(--mono);color:var(--ink-2);margin:6px 0 0}'
                        '.lesson-links a.pt2{opacity:.85}</style>', 1)
    groups = {}
    for key, f, pg, date, short, mins in index:
        groups.setdefault((date, short, key.rstrip('rc')), []).append((f, pg, mins))
    cards = ''
    for (date, short, k), pages in groups.items():
        links = ''.join(f'<a href="{f}"' + (' class="pt2"' if i else '') + f'>{H.escape(pg["title"])}</a>' for i, (f, pg, m) in enumerate(pages))
        total = sum(m for *_, m in pages)
        cards += (f'<article class="lesson-group"><h3><span>{date} · Aula {re.sub(r"[^0-9]", "", k)}</span>{H.escape(short)}</h3>'
                  f'<p>{pages[0][1]["deck"]}</p><p class="label" style="margin-top:6px">≈ {total} min de leitura</p><div class="lesson-links">{links}</div></article>')
    n_aulas = len({re.sub(r'\D', '', k) for k, *_ in index})
    allon = set(range(len(C['stations'])))
    kick_exam = f" · {C['exam'][0]} em {C['exam'][1][:5]}" if C['exam'] else ''
    prof = f"<span>{C['prof']}</span>" if C['prof'] else ''
    body = f'''<body>
<nav class="topbar" aria-label="Navegação principal"><a href="../../index.html">← CUFRGS</a><span>{C['code']} · UFRGS · 2026/2</span><button class="theme-toggle" type="button" aria-pressed="false" title="Alternar modo noite"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Modo noite</span></button></nav>
<header class="hero front">
  <div class="kicker label"><span>Guia de estudo</span>{prof}<span>{n_aulas} aulas{kick_exam}</span></div>
  <h1><span class="split">{C['course'].rsplit(' ', 1)[0]}</span><span class="split">{C['course'].rsplit(' ', 1)[1]}</span></h1>
  <p class="deck">{C.get('deck', 'As aulas do programa, na ordem em que o curso as apresenta. Cada aula tem um teste no fim.')}</p>
</header>
<main>
<section class="front-track" aria-label="Mapa do curso"><svg class="hero-fork" viewBox="0 0 1080 170" role="img" aria-label="Percurso do curso">{track(C['stations'], allon, set(), quiet=True)}</svg></section>
<section class="map-section front-sheet" aria-label="Avaliação">
  <aside class="exam-card" aria-labelledby="exam-title">
    <span class="exam-date">{(C['exam'][0] + ' · ' + C['exam'][1]) if C['exam'] else 'Semestre 2026/2'}</span>
    <h2 id="exam-title">{'O que cai' if C['exam'] else 'O que já está aqui'}</h2>
    <p>{C['scope']} Comece pelos testes no fim de cada aula: o que você não souber responder é o que falta ler.</p>
    <a href="{index[0][1]}"><span>Começar pela Aula 01</span><span aria-hidden="true">→</span></a>
  </aside>
</section>
<section class="lessons" id="aulas" aria-labelledby="lessons-title">
  <header class="section-head"><span class="label">Caderno de estudo</span><h2 id="lessons-title">Aulas</h2><p>Na ordem do programa.</p></header>
  <div class="lesson-grid">{cards}</div>
</section>
</main>
<p class="endnote">{C['course']} ({C['code']}) · UFRGS · 2026/2.</p>
<script src="assets/curso.js?v={kit.VER}"></script>
</body>
</html>
'''
    open(kit.OUT + 'index.html', 'w').write(head + body)
    print('wrote index', C['slug'])

if __name__ == '__main__':
    for c in (sys.argv[1:] or list(COURSES)):
        build(c)
    import subprocess
    subprocess.run([sys.executable, os.path.join(SITE, 'tools', 'fontes_info.py')], check=True)   # the ⓘ card on the fronts
    subprocess.run([sys.executable, os.path.join(SITE, 'tools', 'offline_build.py')], check=True)   # modo avião script + manifest
