#!/usr/bin/env node
/** Reusable staging screenshot and geometry gate. Read-only against the target site. */
import { createRequire } from 'node:module';
import path from 'node:path';
import fs from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const HERE = path.dirname(fileURLToPath(import.meta.url));
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const VIEWPORTS = [{ name: 'desktop', width: 1280, height: 960 }, { name: 'phone', width: 390, height: 844 }];
const THEMES = ['light', 'dark'];

function args(argv) {
  const out = { manifest: null, output: path.join(HERE, 'output'), baseUrl: 'http://127.0.0.1:8767/', selectorOnly: false };
  for (let i = 0; i < argv.length; i++) {
    const key = argv[i];
    if (key === '--manifest') out.manifest = path.resolve(argv[++i]);
    else if (key === '--output') out.output = path.resolve(argv[++i]);
    else if (key === '--base-url') out.baseUrl = argv[++i];
    else if (key === '--selector-only') out.selectorOnly = true;
    else if (key === '--help') out.help = true;
    else throw new Error(`Unknown argument: ${key}`);
  }
  return out;
}

function safeName(value) { return String(value).replace(/[^a-z0-9._-]+/gi, '-').replace(/^-+|-+$/g, '') || 'page'; }
function short(value, max = 90) { return String(value || '').replace(/\s+/g, ' ').trim().slice(0, max); }

async function inspect(page) {
  return page.evaluate(() => {
    const root = document.documentElement;
    const shortText = (value, max = 90) => String(value || '').replace(/\s+/g, ' ').trim().slice(0, max);
    const visible = el => {
      if (!el.isConnected || el.closest('defs, symbol, clipPath, mask, pattern, marker')) return false;
      const style = getComputedStyle(el);
      if (style.display === 'none' || style.visibility === 'hidden' || Number(style.opacity) === 0) return false;
      const r = el.getBoundingClientRect();
      return r.width > 0 && r.height > 0;
    };
    const dupes = [];
    const idMap = new Map();
    for (const el of document.querySelectorAll('[id]')) idMap.set(el.id, (idMap.get(el.id) || 0) + 1);
    for (const [id, count] of idMap) if (count > 1) dupes.push({ id, count });
    const svgs = [];
    const collisions = [];
    const toRoot = (svg, el, box) => {
      const rootCTM = svg.getScreenCTM(); const elCTM = el.getScreenCTM();
      if (!rootCTM || !elCTM) return null;
      const matrix = rootCTM.inverse().multiply(elCTM);
      const pts = [[box.x, box.y], [box.x + box.width, box.y], [box.x, box.y + box.height], [box.x + box.width, box.y + box.height]]
        .map(([x, y]) => new DOMPoint(x, y).matrixTransform(matrix));
      const xs = pts.map(p => p.x), ys = pts.map(p => p.y);
      return { x: Math.min(...xs), y: Math.min(...ys), right: Math.max(...xs), bottom: Math.max(...ys) };
    };
    for (const [index, svg] of [...document.querySelectorAll('svg')].entries()) {
      if (!visible(svg)) continue;
      const rect = svg.getBoundingClientRect();
      const hostOverflow = rect.left < -1 || rect.right > innerWidth + 1;
      const vb = (svg.getAttribute('viewBox') || '').trim().split(/[ ,]+/).map(Number);
      const textRows = [];
      for (const text of svg.querySelectorAll('text')) {
        if (!visible(text)) continue;
        let box;
        try { box = text.getBBox(); } catch { continue; }
        if (!(box.width > 0 && box.height > 0)) continue;
        const normalized = toRoot(svg, text, box);
        if (!normalized) continue;
        const label = shortText(text.textContent) || '(empty)';
        if (vb.length === 4 && vb.every(Number.isFinite)) {
          const [vx, vy, vw, vh] = vb;
          if (normalized.x < vx - 1 || normalized.y < vy - 1 || normalized.right > vx + vw + 1 || normalized.bottom > vy + vh + 1) {
            textRows.push({ label, bounds: normalized });
          }
        }
        textRows.push({ label, bounds: normalized, _forCollision: true });
      }
      const drawable = textRows.filter(row => row._forCollision);
      for (let a = 0; a < drawable.length; a++) for (let b = a + 1; b < drawable.length; b++) {
        const xOverlap = Math.min(drawable[a].bounds.right, drawable[b].bounds.right) - Math.max(drawable[a].bounds.x, drawable[b].bounds.x);
        const yOverlap = Math.min(drawable[a].bounds.bottom, drawable[b].bounds.bottom) - Math.max(drawable[a].bounds.y, drawable[b].bounds.y);
        if (xOverlap > 1 && yOverlap > 1) collisions.push({ svg: svg.id || `svg-${index + 1}`, first: drawable[a].label, second: drawable[b].label, overlap: { x: +xOverlap.toFixed(1), y: +yOverlap.toFixed(1) } });
      }
      svgs.push({ id: svg.id || `svg-${index + 1}`, hostRect: { x: +rect.x.toFixed(1), right: +rect.right.toFixed(1), width: +rect.width.toFixed(1) }, hostHorizontalOverflow: hostOverflow,
        textOutsideViewBox: textRows.filter(row => !row._forCollision).map(({ label, bounds }) => ({ label, bounds })) });
    }
    const inspectEl = document.querySelector('[data-gate-inspect]');
    return {
      viewport: { width: innerWidth, height: innerHeight }, theme: root.dataset.theme === 'dark' ? 'dark' : 'light',
      documentOverflow: root.scrollWidth > innerWidth + 1 ? { clientWidth: innerWidth, scrollWidth: root.scrollWidth, excess: root.scrollWidth - innerWidth } : null,
      duplicateIds: dupes, svgs, svgTextCollisions: collisions,
      inspect: inspectEl ? { selector: '[data-gate-inspect]', text: short(inspectEl.textContent, 240), rect: (() => { const r = inspectEl.getBoundingClientRect(); return { x: +r.x.toFixed(1), y: +r.y.toFixed(1), width: +r.width.toFixed(1), height: +r.height.toFixed(1) }; })() } : null
    };
  });
}

async function main() {
  const options = args(process.argv.slice(2));
  if (options.help) {
    console.log('Usage: node gate.mjs [--manifest manifest.json] [--output DIR] [--base-url URL] [--selector-only]');
    return;
  }
  const manifest = options.manifest ? JSON.parse(await fs.readFile(options.manifest, 'utf8')) : { pages: [{ name: 'home', path: '/' }] };
  if (!Array.isArray(manifest.pages) || manifest.pages.length === 0) throw new Error('Manifest must contain a non-empty pages array.');
  await fs.mkdir(options.output, { recursive: true });
  const browser = await chromium.launch({ headless: true, executablePath: CHROME });
  const results = [];
  try {
    for (const entry of manifest.pages) {
      if (!entry.path) throw new Error('Each page requires path.');
      const pageUrl = new URL(entry.path, options.baseUrl).href;
      for (const viewport of VIEWPORTS) for (const theme of THEMES) {
        const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height }, colorScheme: theme });
        const seed = { ...(manifest.localStorage || {}), ...(entry.localStorage || {}), 'ordenacoes-theme': theme };
        await context.addInitScript(({ values, themeName }) => {
          try { for (const [key, value] of Object.entries(values)) localStorage.setItem(key, String(value)); } catch {}
          const root = document.documentElement;
          if (root) {
            if (themeName === 'dark') root.dataset.theme = 'dark';
            else delete root.dataset.theme;
          }
        }, { values: seed, themeName: theme });
        const page = await context.newPage();
        const jsErrors = [];
        page.on('pageerror', error => jsErrors.push({ kind: 'pageerror', message: error.message }));
        page.on('console', message => { if (message.type() === 'error') jsErrors.push({ kind: 'console-error', message: message.text() }); });
        const response = await page.goto(pageUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
        if (!response || response.status() >= 400) jsErrors.push({ kind: 'navigation', message: `HTTP ${response?.status() ?? 'no response'} for ${pageUrl}` });
        await page.evaluate(async themeName => {
          try {
            if (themeName === 'dark') localStorage.setItem('ordenacoes-theme', 'dark');
            else localStorage.setItem('ordenacoes-theme', 'light');
          } catch {}
          if (themeName === 'dark') document.documentElement.dataset.theme = 'dark';
          else delete document.documentElement.dataset.theme;
          if (document.fonts?.ready) await document.fonts.ready;
        }, theme);
        await page.waitForTimeout(100);
        const geometry = await inspect(page);
        const stem = `${safeName(entry.name || entry.path)}-${viewport.name}-${theme}`;
        const screenshot = options.selectorOnly ? null : path.join(options.output, `${stem}.png`);
        if (screenshot) await page.screenshot({ path: screenshot, fullPage: true });
        const crops = [];
        const selectors = [...(entry.selectors || [])];
        if (entry.artSelector) selectors.push(entry.artSelector);
        for (let i = 0; i < selectors.length; i++) {
          const selector = typeof selectors[i] === 'string' ? selectors[i] : selectors[i].selector;
          const label = typeof selectors[i] === 'string' ? selector : (selectors[i].name || selector);
          const locator = page.locator(selector).first();
          if (await locator.count()) {
            const crop = path.join(options.output, `${stem}-crop-${safeName(label)}.png`);
            await locator.screenshot({ path: crop });
            crops.push({ selector, screenshot: path.basename(crop) });
          } else crops.push({ selector, missing: true });
        }
        results.push({ page: entry.path, url: pageUrl, viewport, theme: geometry.theme, ...(screenshot ? { screenshot: path.basename(screenshot) } : {}), crops, geometry, jsErrors });
        await context.close();
      }
    }
  } finally { await browser.close(); }
  const report = { generatedAt: new Date().toISOString(), baseUrl: options.baseUrl, manifest: options.manifest ? path.basename(options.manifest) : '(default home page)', results };
  const reportPath = path.join(options.output, 'gate-report.json');
  await fs.writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`);
  console.log(`Captured ${results.length} page/theme/viewport states. Report: ${reportPath}`);
}

main().catch(error => { console.error(error.stack || error.message); process.exitCode = 1; });
