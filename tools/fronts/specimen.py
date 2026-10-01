#!/usr/bin/env python3
"""Render specimen/register.html: every state of the class register, with the reason for each.
Same code path as the real fronts (front._register), so the specimen can't drift. Run after changing the register."""
import html, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import front

L = lambda n, t, d=None, m=20, **k: {"label": f"Aula {n:02d}" if n else "Leitura complementar", "title": t, "href": "#" + t, "_minutes": m, **({"reg": {"does": d}} if d else {}), **k}
DATA = {
    "units": [
        {"title": "Uma unidade com várias aulas tem cabeçalho", "lessons": [
            L(1, "Aula comum", "Distinguir o que esta linha diz: o que a aula deixa você fazer.", 20),
            L(2, "Aula em duas páginas", "Partes: os traços mostram em qual página você está.", 25),
            L(2, "Aula em duas páginas (continuação)", "A segunda página da mesma aula.", 20),
            L(3, "Leitura complementar de uma aula", "Mesmo número, traço vazado: material opcional.", 10, complementary=True),
            L(4, "Aula sem linha de função", None, 40),
        ]},
        {"title": "Unidade de uma aula só", "lessons": [L(5, "Unidade de uma aula só", "Sem cabeçalho: ele repetiria a linha.", 15)]},
        {"title": "Depois da primeira prova", "lessons": [
            L(6, "Aula da segunda prova", "A barra muda de cor com a prova.", 60),
            L(7, "Aula sem prova conhecida", "Sem barra: nenhuma fonte diz em que prova ela cai.", 5),
            L(0, "Leitura sem número", "Sem número de aula: só o ponto.", 10, complementary=True),
        ]},
    ],
    "reg": {"exams": [{"label": "P1", "date": "07/10", "covers": ["#Aula comum", "#Aula em duas páginas", "#Aula em duas páginas (continuação)", "#Leitura complementar de uma aula", "#Aula sem linha de função", "#Unidade de uma aula só"]},
                      {"label": "P2", "covers": ["#Aula da segunda prova"]}]},
}
WHY = [
    ("Linha", "Número, título, a linha do que a aula deixa você fazer, e o relógio. O título diz o tema; a linha diz a função."),
    ("Relógio", "O setor pintado é o tempo de leitura (60 min = mostrador cheio), calculado das palavras da página a 180 por minuto. Uma aula de uma sessão fica entre 15 e 25. Fatias muito finas ou muito cheias saltam aos olhos: são aulas a aprofundar ou dividir."),
    ("Partes", "Uma aula longa vira duas ou três páginas; os traços dizem em qual delas você está. Leituras complementares não contam como parte."),
    ("Complementar", "O número vazado e o título mais leve dizem que é opcional, sem rótulo escrito."),
    ("Sem linha de função", "Fica um vazio silencioso, nunca um texto de preenchimento."),
    ("Unidade", "Número e título da unidade sobre uma régua. Uma unidade de uma aula só não tem cabeçalho, porque ele repetiria a linha."),
    ("Prova", "Uma barra fina na cor da prova corre pelas aulas que ela cobre e termina numa dobra tracejada com o nome e a data. Só marca o que uma fonte afirma; o resto fica sem barra."),
    ("Igual em todo curso", "O desenho acima do registro é livre e próprio de cada curso. O registro é um instrumento só: mesma anatomia, tipos, sinais e espaçamento nos sete."),
]
body = front._register(DATA, "specimen")
why = "".join(f"<dt>{html.escape(a)}</dt><dd>{html.escape(b)}</dd>" for a, b in WHY)
page = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Registro de aulas · espécime · Ordenações Filipinas</title>
<link rel="stylesheet" href="../courses/processo-civil-i/assets/curso.css">
<link rel="stylesheet" href="../assets/front.css">
<style>main{{max-width:980px;margin:32px auto;padding:0 clamp(16px,4vw,48px)}}.why{{margin:40px 0 64px;display:grid;grid-template-columns:11rem 1fr;gap:10px 24px;font:15px/1.5 var(--serif,Georgia,serif)}}.why dt{{font:600 13px/1.5 var(--mono)}}.why dd{{margin:0;color:var(--ink-2)}}@media(max-width:600px){{.why{{grid-template-columns:1fr}}.why dd{{margin-bottom:10px}}}}</style>
</head><body><main>{body}<dl class="why">{why}</dl></main></body></html>
"""
out = front.R / "specimen" / "register.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print("wrote", out.relative_to(front.R))
