"""Install only Aula 11-mérito's two kit panels, without visiting other pages.

Run when the page editor is ready to integrate figures:
    python3 tools/figkit/inject_processo_a11_merito.py
The transform uses textual section anchors; it does not reserialize existing SVG.
"""

from pathlib import Path
import re

from processo_a11_merito import grounds_panel, phase_panel, specimen_entry


PAGE = Path(__file__).resolve().parents[2] / 'courses/processo-civil-i/aula-11-merito.html'
SPECIMEN = Path(__file__).resolve().parents[2] / 'specimen/figuras.html'


def _figure(panel, label):
    ident = re.search(r'id="([^"]+)"', panel).group(1)
    return (f'<div class="wide figkit-placement"><figure aria-label="{label}" '
            'style="margin:30px 0 34px;padding:14px;background:var(--paper);'
            'border:1.5px solid var(--ink);box-shadow:5px 5px 0 var(--grid-major)">'
            f'<style>#{ident}{{display:block;width:100%;height:auto}}</style>'
            f'{panel}</figure></div>')


def install(source):
    for chapter, panel, label in (
        ('c2', grounds_panel(), 'Dois fundamentos e um objeto decidido'),
        ('c5', phase_panel(), 'Parcela resolvida e fase cognitiva em curso'),
    ):
        ident = re.search(r'id="([^"]+)"', panel).group(1)
        if f'id="{ident}"' in source:
            continue
        pattern = rf'(<section class="chapter" aria-labelledby="{chapter}">.*?</section>)'
        match = re.search(pattern, source, flags=re.S)
        if not match:
            raise ValueError(f'Aula 11-mérito section {chapter} is absent')
        source = source[:match.end()] + '\n' + _figure(panel, label) + source[match.end():]
    return source


def install_specimen(source):
    if 'id="specimen-pci-a11m"' in source:
        return source
    anchor = '<script src="../courses/processo-civil-i/assets/aula-17.js"></script>'
    if source.count(anchor) != 1:
        raise ValueError('figure specimen insertion anchor is absent or duplicated')
    return source.replace(anchor, specimen_entry() + '\n' + anchor)


if __name__ == '__main__':
    before = PAGE.read_text(encoding='utf-8')
    after = install(before)
    if after != before:
        PAGE.write_text(after, encoding='utf-8')
    before_specimen = SPECIMEN.read_text(encoding='utf-8')
    after_specimen = install_specimen(before_specimen)
    if after_specimen != before_specimen:
        SPECIMEN.write_text(after_specimen, encoding='utf-8')
    print(f'{PAGE}: {int(after != before)} page updated; specimen: {int(after_specimen != before_specimen)} updated')
