#!/usr/bin/env python3
"""Render the states page for the shared professor profile card."""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "fronts"))
import professor_card


def sample(title: str, reason: str, slot: str, state: str, class_name: str = "", ident: str = "") -> str:
    ident_attr = f' id="{html.escape(ident, quote=True)}"' if ident else ""
    return (f'<article class="sample {class_name}" data-state="{html.escape(state, quote=True)}"{ident_attr}><p class="sample-state">{html.escape(title)}</p>'
            f'<div class="sample-content">{slot}</div><p class="reason">{html.escape(reason)}</p></article>')


def static_card(profile: dict, course: str, label: str, ident: str, root: str = "../") -> str:
    button_id = f"professor-demo-button-{ident}"
    card_id = f"professor-demo-card-{ident}"
    other = [item for item in profile.get("courses", []) if item.get("slug") != course]
    courses = ""
    if other:
        links = []
        for item in other:
            href = item.get("href", "")
            href = href if href.startswith("#") else root + href
            links.append(f'<a href="{html.escape(href, quote=True)}">{html.escape(item["title"])}</a>')
        courses = '<p class="professor-card-courses">Também: ' + ' · '.join(links) + '</p>'
    return (f'<span class="professor-anchor"><button id="{button_id}" class="professor-name" type="button" '
            f'aria-label="{html.escape(profile["name"], quote=True)}, abre perfil" '
            f'aria-expanded="true" aria-controls="{card_id}">{html.escape(label)}</button>'
            f'<section id="{card_id}" class="professor-card is-open" role="region" aria-labelledby="{card_id}-name">'
            f'<div id="{card_id}-name" class="professor-card-name" role="heading" aria-level="2">{html.escape(profile["name"])}</div>'
            f'<p class="professor-card-title">{html.escape(profile["title"])}</p>'
            f'<p class="professor-card-bio">{html.escape(profile["bio"])}</p>{courses}</section></span>')


def main() -> None:
    profiles = professor_card.public_profiles()
    closed = professor_card.name_slot("controle-de-constitucionalidade", "Prof. Marcelo Schenk Duque", "../")
    open_card = static_card(profiles["direito-latino-americano"], "direito-latino-americano", "Profa. Roberta Baggio", "open")
    phone = static_card(profiles["processo-civil-i"], "processo-civil-i", "Prof. Eduardo Scarparo", "phone")
    dark = static_card(profiles["teoria-geral-dos-contratos"], "teoria-geral-dos-contratos", "Profa. Giovana Benetti", "dark")
    two_course = static_card({
        "name": "Pessoa docente de demonstração",
        "title": "EXEMPLO · DUAS DISCIPLINAS",
        "bio": "Perfil fictício usado para mostrar a lista de disciplinas.",
        "courses": [
            {"slug": "demo-two-courses", "title": "Curso de demonstração I", "href": "#course-one"},
            {"slug": "demo-course-two", "title": "Curso de demonstração II", "href": "#course-two"},
        ],
    }, "demo-two-courses", "Pessoa docente de demonstração", "multi")
    body = "\n".join([
        '<header class="specimen-head"><p class="eyebrow">COMPONENTE · PERFIL DO DOCENTE</p><h1>Uma ficha sob o nome</h1>',
        '<p>A ficha abre junto ao nome e deixa a leitura no lugar.</p><button id="theme-toggle" type="button" aria-pressed="false">Alternar tema escuro</button></header>',
        '<main class="samples">',
        sample("01 · Fechada", "O nome continua discreto no kicker e o foco de teclado fica visível.", closed, "closed"),
        sample("02 · Aberta", "A ficha abre abaixo do nome, sem deslocar o título.", open_card, "open"),
        sample("03 · Telefone · 375 px", "A largura cabe entre duas margens de 16 px.", phone, "phone", "phone-sample"),
        sample("04 · Duas disciplinas", "Exemplo estrutural fictício: demonstra o link adicional sem atribuir dois cursos a alguém real.", two_course, "two-course", ident="course-two"),
        sample("05 · Tema escuro", "A borda e o papel acompanham as cores do tema.", dark, "dark", "dark-sample"),
        '</main>',
    ])
    html_doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Perfil do docente · Ordenações Filipinas</title>
  <link rel="stylesheet" href="../courses/controle-de-constitucionalidade/assets/controle.css">
  <link rel="stylesheet" href="../assets/front.css">
  {professor_card.stylesheet_link("../")}
  <style>
    .specimen-head,.samples{{width:min(100% - 32px,1120px);margin-inline:auto;box-sizing:border-box}}
    .specimen-head{{padding:38px 0 24px;border-bottom:1.5px solid var(--ink)}}
    .specimen-head .eyebrow,.sample-state{{font:500 11px/1.4 var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--ink-2)}}
    .specimen-head h1{{margin:8px 0;font:750 clamp(34px,5vw,58px)/1 var(--sans);color:var(--ink)}}
    .specimen-head>p:not(.eyebrow){{font:18px/1.45 var(--serif);color:var(--ink-2)}}
    #theme-toggle{{padding:7px 10px;border:1px solid var(--ink);background:var(--paper);color:var(--ink);font:500 11px var(--mono);cursor:pointer}}
    .samples{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:18px;padding:24px 0 60px}}
    .sample{{min-height:188px;padding:16px;border:1px solid var(--ink);background:var(--paper);box-shadow:5px 5px 0 var(--grid-major);box-sizing:border-box}}
    .sample-state{{margin:0 0 18px}}
    .sample-content{{position:relative;min-height:48px;padding:14px 0 6px;font:500 11px/1.5 var(--mono);color:var(--ink-2)}}
    .reason{{margin:25px 0 0;border-top:1px solid var(--grid-major);padding-top:10px;font:14px/1.45 var(--serif);color:var(--ink-2)}}
    .phone-sample{{width:375px;max-width:100%;grid-column:span 1}}
    .phone-sample .sample-content{{min-height:170px;padding:14px 16px 6px}}
    .phone-sample .professor-card{{width:343px;max-width:calc(100vw - 32px)}}
    .dark-sample{{color-scheme:dark;--paper:#14171d;--paper-2:#1e2229;--grid-major:#252a32;--ink:#e5e3da;--ink-2:#a3a6a6;--muted:#868a8e;--conc:#dd8b6b;--conc-wash:#372824;--dif:#7fb0dd;--dif-wash:#1e2c3b;--mix:#b99ad0;--mix-wash:#2b2635}}
    .dark-sample .sample-content{{padding:14px 12px 6px;background:var(--paper-2)}}
    @media(max-width:480px){{.phone-sample .professor-card{{width:calc(100vw - 32px)}}}}
  </style>
</head>
<body>
{body}
{professor_card.script_tags("../")}
<script>
  document.getElementById('theme-toggle').addEventListener('click', function () {{
    const dark = document.documentElement.dataset.theme !== 'dark';
    if (dark) document.documentElement.dataset.theme = 'dark';
    else delete document.documentElement.dataset.theme;
    this.setAttribute('aria-pressed', String(dark));
  }});
</script>
</body>
</html>'''
    target = ROOT / "specimen" / "professor.html"
    target.write_text(html_doc, encoding="utf-8")
    print(f"rendered {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
