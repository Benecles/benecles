#!/usr/bin/env python3
"""CUFRGS slop linter: enforces Part D of `CUFRGS Writing Standard.md`.

    python3 slop_lint.py FILE_OR_DIR [...] [--quiet]

Reads .html (visible text only; figures, scripts and styles are ignored), .md and .txt.
Each file counts as one lesson for per-lesson limits.
Exit code 1 if any file has a hard hit, an em dash, or a limit exceeded.
Passing is a floor, not a verdict: Claude's read decides.
"""
import html, os, re, sys

HARD = {
    'negativa "mais do que um/uma/simples X"': r'\bmais do que (?:um|uma|simples)\b',
    'puffery': r'\b(?:papel (?:crucial|fundamental|central|decisivo|essencial)|desempenha(?:m)? (?:um )?papel|pedra angular|divisor de águas|ganha(?:m)? destaque|merece(?:m)? atenção especial|reflete(?:m)? a (?:importância|relevância)|evidencia(?:ndo|m)? a (?:importância|relevância)|revela(?:-se|m-se) (?:essencial|fundamental|crucial))\b',
    'gerúndio de significância': r',\s(?:evidenciando|reforçando|consolidando|demonstrando|ressaltando|sublinhando|refletindo|destacando|evidenciando) (?:a|o|as|os|sua|seu) (?:importância|relevância|papel|centralidade|compromisso|necessidade|peso|força|valor)\b',
    'conector formulaico / metatexto': r'\b(?:vale (?:a pena )?(?:ressaltar|destacar|notar|lembrar|mencionar)|cabe (?:ressaltar|destacar|notar|lembrar)|é (?:importante|interessante|fundamental) (?:notar|ressaltar|destacar|observar|lembrar|mencionar)|nesta aula (?:veremos|vamos)|como (?:vimos|veremos)|vamos entender|em conclusão|por fim, mas não menos importante|à luz do exposto)\b',
    'atribuição vaga': r'\b(?:especialistas (?:apontam|afirmam|destacam)|muitos autores|a doutrina moderna|há quem (?:diga|sustente|defenda)|alguns críticos)\b',
    'fala com o leitor': r'\b(?:você já deve ter percebido|não se preocupe|pense nisso|perceba que|repare:?)\b',
    'calque de IA': r'\b(?:no cenário (?:atual|jurídico|brasileiro)|navegar (?:por|pel[oa]s?)|abordagem holística|robust[oa]s?|(?-i:jornada)|mergulh(?:ar|amos|e) (?:em|n[oa]s?))\b',
    'tríade de efeito ("X, Y e, sobretudo, Z")': r'\b(?:e, sobretudo,|e, acima de tudo,)',
}
LIMIT = {  # pattern, max per lesson
    'não é X, (é|e sim|mas) Y': (r'\bnão (?:é|era|são|foi|está)\b[^.;:!?]{1,70}?[,;]\s(?:é|era|são|e sim|mas sim|senão)\b', 1),
    'não se trata de (só para distinção jurídica real)': (r'\bnão se trata (?:apenas )?de\b', 1),
    'não apenas/só… mas (também)': (r'\bnão (?:apenas|só|somente)\b[^.!?]{1,90}?\bmas\b', 1),
    'em suma / em síntese / em resumo': (r'\b(?:em suma|em síntese|em resumo)\b', 1),
    'ou seja': (r'\bou seja\b', 1),
    'dessa forma / desse modo': (r'\b(?:dessa|desta) (?:forma|maneira)|\bdesse modo\b', 1),
    'nesse sentido': (r'\bnesse sentido\b', 1),
    'além disso / ademais': (r'\b(?:além disso|ademais)\b', 2),
    'tique da casa ("A pergunta é/decisiva", "Tudo começa/depende")': (r'\b(?:a pergunta (?:é|decisiva|decide|muda|central)|tudo (?:começa|depende))\b', 1),
    'intensificadores': (r'\b(?:crucial|extremamente|significativ[oa]s?|realmente|(?<!matéria )(?<!questão )(?<!situação )(?<!circunstância )(?<!erro )(?<!estado )(?<!prova )de fato|claramente|evidentemente|decisiv[oa]s?|central|centrais|fundamental|fundamentais|essencial|essenciais)\b', 3),
}
REVIEW = {  # reported for a human look, never fails (definition lists use the same shape)
    'dois-pontos de efeito curto': r'(?:(?<=[.!?]\s)|^)[A-ZÁÉÍÓÚÂÊÔÃÕÇ][^.:!?]{2,28}:\s[^.:!?]{2,45}[.!]',
}
# terms of art never count as intensifiers
TERMS = r'\b(?:direitos? fundamenta(?:l|is)|princípios? fundamenta(?:l|is)|preceito fundamental|elementos? essencia(?:l|is)|erro essencial|qualidades? essencia(?:l|is)|requisitos? essencia(?:l|is)|funç(?:ão|ões) essencia(?:l|is)|serviços? essencia(?:l|is)|banco central|garantias? fundamenta(?:l|is)|constituciona(?:l|is) fundamenta(?:l|is)|centra(?:l|is) sindica(?:l|is)|núcleo essencial|questão central|figura central|posição central|conceito (?:estendido |extensivo )?de fato|estado de fato|situação de fato)\b'

def text_of(path):
    s = open(path, encoding='utf-8', errors='ignore').read()
    if path.endswith('.html'):
        s = re.sub(r'(?is)<(script|style|svg|head|nav)\b.*?</\1>', ' ', s)
        s = re.sub(r'(?i)<br\s*/?>|</(?:p|li|h\d|td|th|div|figcaption|summary)>', '\n', s)
        s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    return re.sub(r'[ \t]+', ' ', s)

def ctx(t, m):
    return re.sub(r'\s+', ' ', t[max(0, m.start() - 50):m.end() + 40]).strip()

def lint(path, quiet):
    t = text_of(path)
    fail, out = False, []
    dashes = [m for m in re.finditer('—', t)]
    if dashes:
        fail = True; out.append(f'  HARD em dash ×{len(dashes)}: …{ctx(t, dashes[0])}…')
    for name, p in HARD.items():
        ms = list(re.finditer(p, t, re.I))
        if ms:
            fail = True
            out.append(f'  HARD {name} ×{len(ms)}')
            out += [f'       …{ctx(t, m)}…' for m in ms[:4]]
    tt = re.sub(TERMS, lambda m: '§' * len(m.group(0)), t, flags=re.I)
    for name, (p, lim) in LIMIT.items():
        ms = list(re.finditer(p, tt, re.I | re.M))
        if len(ms) > lim:
            fail = True
            out.append(f'  OVER {name} ×{len(ms)} (limit {lim})')
            out += [f'       …{ctx(t, m)}…' for m in ms[:4]]
        elif ms and not quiet:
            out.append(f'  ok   {name} ×{len(ms)} (limit {lim})')
    for name, p in REVIEW.items():
        ms = list(re.finditer(p, t, re.M))
        if len(ms) > 3 and not quiet:
            out.append(f'  look {name} ×{len(ms)}: …{ctx(t, ms[0])}…')
    words = len(t.split())
    print(f'{"FAIL" if fail else "PASS"}  {path}  ({words:,} words)')
    if out and (fail or not quiet):
        print('\n'.join(out))
    return fail

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    quiet = '--quiet' in sys.argv
    files = []
    for a in args:
        if os.path.isdir(a):
            for d, _, fs in os.walk(a):
                files += [os.path.join(d, f) for f in sorted(fs) if f.endswith(('.html', '.md', '.txt'))]
        else:
            files.append(a)
    if not files:
        print(__doc__); sys.exit(2)
    bad = sum(lint(f, quiet) for f in sorted(files))
    print(f'\n{len(files) - bad}/{len(files)} pass')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
