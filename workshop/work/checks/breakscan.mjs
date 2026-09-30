// Site-wide scan for three bug classes (Claude, 30/09):
//  SHORT  = an animated stroke (.draw/.grow) longer than its dasharray: the line never finishes drawing
//  CROSS  = a line/path runs through a label's box
//  CLASH  = two labels overlap (heroes and SVGs outside <figure> included)
import { createRequire } from 'node:module'; import fs from 'node:fs/promises'; import path from 'node:path';
const require = createRequire(import.meta.url);
const { chromium } = require('/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const SITE = process.argv[2], OUT = process.argv[3], BASE = 'http://127.0.0.1:8790/';
const probe = () => {
  const out = [];
  const svgs = [...document.querySelectorAll('body svg')].filter(s => !s.parentElement.closest('svg') && s.getBoundingClientRect().width > 40);
  svgs.forEach((svg, si) => {
    const where = svg.closest('figure') ? 'figure' : (svg.classList.contains('hero-fork') ? 'hero' : 'other');
    const cap = (svg.closest('figure')?.querySelector('figcaption')?.textContent || svg.getAttribute('class') || '').trim().slice(0, 50);
    const issues = [];
    for (const el of svg.querySelectorAll('.draw, .grow')) {
      if (!el.getTotalLength) continue;
      const cs = getComputedStyle(el); const da = parseFloat(cs.strokeDasharray);
      let L; try { L = el.getTotalLength(); } catch { continue; }
      if (da && L > da + 2) issues.push(`SHORT len ${L | 0} > dash ${da}`);
    }
    const texts = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim()).map(t => { try { return { t, b: t.getBBox(), s: t.textContent.trim().slice(0, 30) }; } catch { return null; } }).filter(x => x && x.b.width);
    for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
      const a = texts[i].b, b = texts[j].b;
      if (Math.min(a.x + a.width, b.x + b.width) - Math.max(a.x, b.x) > 2 && Math.min(a.y + a.height, b.y + b.height) - Math.max(a.y, b.y) > 2) issues.push(`CLASH "${texts[i].s}" × "${texts[j].s}"`);
    }
    const strokes = [...svg.querySelectorAll('line, path, polyline')].filter(e => { const cs = getComputedStyle(e); return cs.stroke !== 'none' && parseFloat(cs.strokeWidth) > 0.5 && cs.opacity !== '0'; });
    for (const { t, b, s } of texts) {
      const inner = { x: b.x + 1, y: b.y + b.height * 0.25, w: b.width - 2, h: b.height * 0.5 };
      for (const e of strokes) {
        let L; try { L = e.getTotalLength(); } catch { continue; } if (!L || L > 6000) continue;
        let hit = false;
        for (let d = 0; d <= L; d += 3) { const p = e.getPointAtLength(d); if (p.x > inner.x && p.x < inner.x + inner.w && p.y > inner.y && p.y < inner.y + inner.h) { hit = true; break; } }
        if (hit) { issues.push(`CROSS "${s}"`); break; }
      }
    }
    if (issues.length) out.push({ si: si + 1, where, cap, issues: [...new Set(issues)] });
  });
  return out;
};
const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } }); const page = await ctx.newPage();
const rows = ['course,page,svg,where,caption,issue'];
for (const c of (await fs.readdir(path.join(SITE, 'courses'))).filter(d => !d.startsWith('.'))) {
  const pages = (await fs.readdir(path.join(SITE, 'courses', c))).filter(f => /^(aula|unidade|suplemento|revisao)[^.]*\.html$/.test(f) && !f.includes('original'));
  for (const p of pages) {
    try { await page.goto(`${BASE}courses/${c}/${p}`, { waitUntil: 'load', timeout: 30000 });
      for (const r of await page.evaluate(probe)) for (const i of r.issues) rows.push([c, p, r.si, r.where, JSON.stringify(r.cap), JSON.stringify(i)].join(','));
    } catch (e) { rows.push([c, p, 0, 'error', '""', JSON.stringify(e.message.slice(0, 60))].join(',')); }
  }
}
await browser.close(); await fs.writeFile(OUT, rows.join('\n') + '\n'); console.log(rows.length - 1, 'issues');
