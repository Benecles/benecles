#!/usr/bin/env python3
"""Apply exact span edits for TXT-L1. Usage: apply.py SITE_ROOT"""
from pathlib import Path
import sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
changes = {
    "tools/fronts/data/direito-latino-americano.json": [
        ('"n_aulas": 9,', '"n_aulas": "nove",'),
        ("Fabiano Engelmann e Júlia Bandeira, “A construção da autonomia política do judiciário na América Latina”", "Fabiano Engelmann e Júlia Veiga Vieira Mâncio Bandeira, “A construção da autonomia política do judiciário na América Latina”"),
        ("Corte Constitucional colombiana:", "Corte Constitucional da Colômbia:"),
        ("Avaliar os limites constitucionais colombianos à justiça de transição e à JEP.", "Avaliar limites constitucionais à transição e à Jurisdição Especial para a Paz (JEP)."),
        ("O estado de coisas inconstitucional atravessa o continente.", "O estado de coisas inconstitucional (ECI) atravessa o continente."),
        ("Corte IDH: Gomes Lund vs. Brasil, Gelman vs. Uruguai e OC‑28/2021",
         "Corte Interamericana de Direitos Humanos (Corte IDH): Gomes Lund vs. Brasil, Gelman vs. Uruguai e Opinião Consultiva 28/2021"),
        ("SCJ do Uruguai (Sentencias 20/2013 e 65/2014) e TCP da Bolívia (SCP 0084/2017)",
         "<i>Suprema Corte de Justicia</i> (Suprema Corte de Justiça; SCJ) do Uruguai (Sentencias 20/2013 e 65/2014) e Tribunal Constitucional Plurinacional (TCP) da Bolívia (SCP 0084/2017)"),
        ("Os oito eixos com respostas, três quadros comparativos e dez problemas mistos resolvidos.",
         "Os oito eixos com respostas, três quadros comparativos e 10 problemas mistos resolvidos."),
    ],
    "courses/direito-latino-americano/aula-02.html": [
        ("Dezenove países, quatro formas de organizar o controle de constitucionalidade.",
         "19 países, quatro formas de organizar o controle de constitucionalidade."),
        ("Na Colômbia, os 74 ministros estudados são da <strong>Corte Suprema de Justicia</strong>.",
         "Na Colômbia, os 74 ministros estudados são da <strong><i>Corte Suprema de Justicia</i></strong> (Suprema Corte de Justiça; CSJ)."),
        ("nove deles indicados por Pinochet.", "nove deles indicados por Augusto Pinochet."),
        ("o governo eleito de Perón destituiu", "o presidente eleito Juan Perón destituiu"),
        ("Nos primeiros meses de governo, Menem ampliou", "Nos primeiros meses do governo do presidente Carlos Menem, ampliou"),
        ("A profissionalização começou sob Vargas,", "A profissionalização começou sob o governo de Getúlio Vargas,"),
        ("Durante o governo Allende,", "Durante o governo de Salvador Allende,"),
        ("o AI-2 aumentou o STF de 11 para 16 ministros", "o Ato Institucional nº 2 (AI-2) aumentou o STF de 11 para 16 ministros"),
        ("com o AI-5, em 1968,", "com o Ato Institucional nº 5 (AI-5), em 1968,"),
        ("Sete países criaram tribunais constitucionais autônomos, separados do Judiciário ordinário,", "Sete países criaram tribunais constitucionais autônomos (TCs), separados do Judiciário ordinário,"),
        ("Sala Constitucional da CSJ", "Sala Constitucional da Corte Suprema de Justicia (CSJ)"),
        ("Sala Constitucional do TSJ", "Sala Constitucional do Tribunal Supremo de Justicia (TSJ)"),
    ],
    "courses/direito-latino-americano/aula-01.html": [],
}
report = ["# TXT-L1 span change log", "", "Changes are exact text substitutions; repeated mentions are expanded at first reference only.", ""]
for relpath, pairs in changes.items():
    path = root / relpath
    text = path.read_text()
    report += [f"## `{relpath}`", ""]
    if not pairs:
        report.append("- Reviewed against the brief; no text changes were needed.")
    for old, new in pairs:
        if new in text:
            report.append(f"- `{old}` → `{new}`")
            continue
        count = text.count(old)
        if count == 0:
            raise SystemExit(f"No match in {relpath}: {old!r}")
        text = text.replace(old, new, 1)
        report.append(f"- `{old}` → `{new}` (one of {count} matching mentions)")
    path.write_text(text)
    report.append("")
(Path(__file__).with_name("changes.md")).write_text("\n".join(report))
print(f"Applied {sum(map(len, changes.values()))} span edits to {len(changes)} pages.")
