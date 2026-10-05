// Figure and viewport probe. Findings are measured in browser screen coordinates
// after fonts and lazy content settle, at the requested viewport widths.
import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';

const DEFAULT_PLAYWRIGHT = '/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright';
const DEFAULT_CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const DEFAULT_BASE = 'http://127.0.0.1:8790/';

function usage() {
  return 'Usage: node breakscan.mjs SITE_ROOT OUTPUT.csv [--width N] [--base-url URL] [--chrome PATH] [--playwright PATH]\nEnv: BREAKSCAN_BASE_URL, BREAKSCAN_CHROME/CHROME_PATH, BREAKSCAN_PLAYWRIGHT/PLAYWRIGHT_PATH; defaults use localhost:8790 and today\'s Chrome/Playwright paths.';
}

function parseArgs(argv) {
  const positional = [];
  const options = {
    widths: [],
    baseUrl: process.env.BREAKSCAN_BASE_URL || DEFAULT_BASE,
    chromePath: process.env.BREAKSCAN_CHROME || process.env.CHROME_PATH || DEFAULT_CHROME,
    playwrightPath: process.env.BREAKSCAN_PLAYWRIGHT || process.env.PLAYWRIGHT_PATH || DEFAULT_PLAYWRIGHT
  };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    const value = name => {
      const next = argv[++i];
      if (!next || next.startsWith('--')) throw new Error(`${name} needs a value`);
      return next;
    };
    if (arg === '--width') options.widths.push(Number(value(arg)));
    else if (arg.startsWith('--width=')) options.widths.push(Number(arg.slice(8)));
    else if (arg === '--base-url') options.baseUrl = value(arg);
    else if (arg === '--chrome') options.chromePath = value(arg);
    else if (arg === '--playwright') options.playwrightPath = value(arg);
    else if (arg === '--help' || arg === '-h') { console.log(usage()); process.exit(0); }
    else if (arg.startsWith('--')) throw new Error(`Unknown option: ${arg}`);
    else positional.push(arg);
  }
  if (positional.length !== 2) throw new Error(usage());
  if (!options.widths.length) options.widths = [1280, 375];
  if (options.widths.some(w => !Number.isInteger(w) || w < 200 || w > 10000)) throw new Error('--width must be an integer from 200 to 10000');
  options.widths = [...new Set(options.widths)];
  return { siteRoot: path.resolve(positional[0]), outFile: path.resolve(positional[1]), ...options };
}

let opts;
try { opts = parseArgs(process.argv.slice(2)); }
catch (error) { console.error(error.message); process.exit(2); }

const require = createRequire(import.meta.url);
let chromium;
try { chromium = require(opts.playwrightPath).chromium; }
catch (error) {
  console.error(`Cannot load Playwright from ${opts.playwrightPath}: ${error.message}`);
  process.exit(2);
}

function csv(value) {
  return `"${String(value ?? '').replaceAll('"', '""')}"`;
}
const CSV_HEADER = ['course', 'page', 'width', 'step', 'step_index', 'panel', 'svg', 'caption', 'issue', 'label', 'detail'];
async function writeCsv(rows, target) {
  const lines = [CSV_HEADER.map(csv).join(',')];
  for (const row of rows) lines.push([
    row.course, row.page, row.width, row.step, row.stepIndex, row.panel, row.svg,
    row.caption, row.kind, row.label, row.detail
  ].map(csv).join(','));
  await fs.mkdir(path.dirname(target), { recursive: true });
  await fs.writeFile(target, `${lines.join('\n')}\n`);
}

async function listPages(siteRoot) {
  const coursesRoot = path.join(siteRoot, 'courses');
  const courses = await fs.readdir(coursesRoot, { withFileTypes: true });
  const pages = [];
  for (const course of courses.filter(entry => entry.isDirectory() && !entry.name.startsWith('.')).sort((a, b) => a.name.localeCompare(b.name))) {
    const dir = path.join(coursesRoot, course.name);
    for (const file of (await fs.readdir(dir)).filter(name => /^(aula|unidade|suplemento|revisao)[^.]*\.html$/.test(name) && !name.includes('original')).sort()) {
      pages.push({ course: course.name, page: file, route: `courses/${course.name}/${file}` });
    }
  }
  try {
    await fs.access(path.join(siteRoot, 'specimen', 'figuras.html'));
    pages.push({ course: 'specimen', page: 'figuras.html', route: 'specimen/figuras.html' });
  } catch { /* Specimen is optional in older site snapshots. */ }
  return pages;
}

// Runs inside Chromium. SVG text boxes and stroke samples are converted to CSS
// screen pixels first, so transforms and separate <g> groups share coordinates.
function probe({ width, step, stepIndex, focusPanelId = '', skipPanelIds = [] }) {
  const findings = [];
  const visible = el => {
    const rootSvg = el.closest?.('svg');
    for (let node = el; node && node !== document.documentElement; node = node.parentElement) {
      const style = getComputedStyle(node);
      if (style.display === 'none' || style.visibility === 'hidden' || Number(style.opacity) <= 0.001) return false;
      // The stage may be aria-hidden while its art is still visible. Ignore
      // explicit aria-hidden marks inside SVG content, not that outer wrapper.
      if ((node === rootSvg || node.namespaceURI === 'http://www.w3.org/2000/svg') && node.getAttribute('aria-hidden') === 'true') return false;
    }
    return true;
  };
  const describe = el => `${el.tagName.toLowerCase()}${el.id ? `#${el.id}` : ''}${el.classList ? [...el.classList].slice(0, 3).map(name => `.${name}`).join('') : ''}`;
  const rectOf = box => ({ left: box.left, right: box.right, top: box.top, bottom: box.bottom, width: box.width, height: box.height });
  const transformRect = (box, matrix) => {
    const points = [
      new DOMPoint(box.x, box.y), new DOMPoint(box.x + box.width, box.y),
      new DOMPoint(box.x, box.y + box.height), new DOMPoint(box.x + box.width, box.y + box.height)
    ].map(point => point.matrixTransform(matrix));
    const xs = points.map(point => point.x), ys = points.map(point => point.y);
    return { left: Math.min(...xs), right: Math.max(...xs), top: Math.min(...ys), bottom: Math.max(...ys) };
  };
  const add = (svg, kind, detail, label = '') => findings.push({
    width, step: step || '', stepIndex: stepIndex ?? '', panel: svg?.id || '', svg: svg ? describe(svg) : '',
    caption: svg ? ((svg.closest('figure')?.querySelector('figcaption')?.textContent || svg.getAttribute('aria-label') || '').trim().slice(0, 100)) : '',
    kind, label, detail
  });

  const rootSvgs = [...document.querySelectorAll('body svg')]
    .filter(svg => !svg.parentElement?.closest('svg') && svg.getBoundingClientRect().width > 40 && visible(svg)
      && (!focusPanelId || svg.id === focusPanelId) && !skipPanelIds.includes(svg.id));
  for (const svg of rootSvgs) {
    const texts = [...svg.querySelectorAll('text')].filter(text => text.textContent.trim() && visible(text)).map(text => {
      const box = rectOf(text.getBoundingClientRect());
      return box.width > 0 && box.height > 0 ? { text, box, value: text.textContent.trim().replace(/\s+/g, ' ').slice(0, 70) } : null;
    }).filter(Boolean);

    // Text × text overlap in rendered screen space, including nested transforms.
    for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
      const a = texts[i].box, b = texts[j].box;
      const overlapX = Math.min(a.right, b.right) - Math.max(a.left, b.left);
      const overlapY = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
      const gapX = Math.max(a.left - b.right, b.left - a.right, 0);
      const sameLine = overlapY > Math.min(a.height, b.height) * 0.55;
      const tightLabelValue = sameLine && gapX < 2.1 && (
        (/^[\p{Lu}\p{N} ·/&–.-]+$/u.test(texts[i].value) && /^\p{Ll}/u.test(texts[j].value))
        || (/^[\p{Lu}\p{N} ·/&–.-]+$/u.test(texts[j].value) && /^\p{Ll}/u.test(texts[i].value))
      );
      if ((overlapX > 0.5 && overlapY > 2) || (sameLine && gapX < 0.5) || tightLabelValue) {
        const detail = overlapX > 0 ? `text boxes overlap ${overlapX.toFixed(1)}×${overlapY.toFixed(1)}px`
          : tightLabelValue ? `label/value boxes leave only ${gapX.toFixed(1)}px gap` : 'text boxes touch with under 0.5px separation';
        add(svg, 'CLASH', detail, `${texts[i].value} × ${texts[j].value}`);
      }
    }

    // Compare rendered text boxes with the actual root viewBox and clipping parents.
    const viewBox = svg.viewBox?.baseVal;
    let viewClip = rectOf(svg.getBoundingClientRect());
    if (viewBox && viewBox.width > 0 && viewBox.height > 0) {
      try { viewClip = transformRect(viewBox, svg.getScreenCTM()); } catch { /* Use SVG viewport bounds. */ }
    }
    for (const item of texts) {
      const b = item.box;
      let side = '', excess = 0;
      const edgeMargin = 1.5;
      if (b.left < viewClip.left + edgeMargin) { side = 'left'; excess = viewClip.left - b.left; }
      else if (b.right > viewClip.right - edgeMargin) { side = 'right'; excess = b.right - viewClip.right; }
      else if (b.top < viewClip.top + edgeMargin) { side = 'top'; excess = viewClip.top - b.top; }
      else if (b.bottom > viewClip.bottom - edgeMargin) { side = 'bottom'; excess = b.bottom - viewClip.bottom; }
      if (side) {
        const detail = excess > 0 ? `text box extends ${excess.toFixed(1)}px past viewBox ${side}` : `text box is within ${(-excess).toFixed(1)}px of viewBox ${side} edge (clipping margin < ${edgeMargin}px)`;
        add(svg, 'CLIP', detail, item.value);
      }

      for (let parent = item.text.parentElement; parent; parent = parent.parentElement) {
        const style = getComputedStyle(parent);
        const clipsX = /hidden|clip|scroll|auto/.test(style.overflowX);
        const clipsY = /hidden|clip|scroll|auto/.test(style.overflowY);
        const clipsPath = style.clipPath && style.clipPath !== 'none';
        if ((clipsX || clipsY || clipsPath) && parent !== svg) {
          const clipBox = rectOf(parent.getBoundingClientRect());
          let clipSide = '', clippedBy = 0;
          if ((clipsX || clipsPath) && b.left < clipBox.left - 1) { clipSide = 'left'; clippedBy = clipBox.left - b.left; }
          else if ((clipsX || clipsPath) && b.right > clipBox.right + 1) { clipSide = 'right'; clippedBy = b.right - clipBox.right; }
          else if ((clipsY || clipsPath) && b.top < clipBox.top - 1) { clipSide = 'top'; clippedBy = clipBox.top - b.top; }
          else if ((clipsY || clipsPath) && b.bottom > clipBox.bottom + 1) { clipSide = 'bottom'; clippedBy = b.bottom - clipBox.bottom; }
          if (clipSide) add(svg, 'CLIP', `text box extends ${clippedBy.toFixed(1)}px past clipping parent ${describe(parent)} ${clipSide}`, item.value);
        }
        if (parent === svg) break;
      }
    }

    const strokes = [...svg.querySelectorAll('line, path, polyline')].filter(el => {
      if (!visible(el)) return false;
      const style = getComputedStyle(el);
      return style.stroke !== 'none' && Number.parseFloat(style.strokeWidth) > 0.5 && Number.parseFloat(style.strokeOpacity || '1') > 0.001;
    });
    const markers = [...svg.querySelectorAll('circle, ellipse')].filter(el => {
      if (!visible(el)) return false;
      const style = getComputedStyle(el);
      const box = el.getBoundingClientRect();
      return style.fill !== 'none' && Number.parseFloat(style.fillOpacity || '1') > 0.001 && box.width <= 20 && box.height <= 20;
    });
    for (const el of svg.querySelectorAll('.draw, .grow')) {
      if (!visible(el) || !el.getTotalLength) continue;
      const dash = Number.parseFloat(getComputedStyle(el).strokeDasharray);
      let length;
      try { length = el.getTotalLength(); } catch { continue; }
      if (dash && length > dash + 2) add(svg, 'SHORT', `path length ${length.toFixed(0)} > dash ${dash.toFixed(0)}`);
    }
    for (const { box, value } of texts) {
      const inner = { left: box.left + 1, right: box.right - 1, top: box.top + box.height * 0.25, bottom: box.top + box.height * 0.75 };
      for (const el of strokes) {
        let length;
        try { length = el.getTotalLength(); } catch { continue; }
        if (!length || length > 6000) continue;
        const matrix = el.getScreenCTM();
        if (!matrix) continue;
        let hit = false;
        const stride = Math.max(0.8, Math.min(3, length / 600));
        for (let d = 0; d <= length; d += stride) {
          const point = el.getPointAtLength(d).matrixTransform(matrix);
          if (point.x > inner.left && point.x < inner.right && point.y > inner.top && point.y < inner.bottom) { hit = true; break; }
        }
        if (hit) { add(svg, 'CROSS', 'visible stroke runs through label box', value); break; }
      }
      for (const marker of markers) {
        const mark = rectOf(marker.getBoundingClientRect());
        const overlapX = Math.min(mark.right, box.right) - Math.max(mark.left, box.left);
        const overlapY = Math.min(mark.bottom, box.bottom) - Math.max(mark.top, box.top);
        if (overlapX > 2 && overlapY > 2) { add(svg, 'CROSS', 'filled marker overlaps label box', value); break; }
      }
    }
  }

  // Page scroll width plus an individual table, figure, or panel exceeding its column.
  const candidates = [...document.querySelectorAll('table, figure, svg, img, video, canvas, pre')].filter(visible);
  const elemOverflow = [];
  for (const el of candidates) {
    const box = rectOf(el.getBoundingClientRect()), parent = el.parentElement;
    let parentExcess = 0;
    if (parent) {
      const pr = parent.getBoundingClientRect(), left = pr.left + parent.clientLeft, right = left + parent.clientWidth;
      parentExcess = Math.max(left - box.left, box.right - right, 0);
    }
    const ownScroll = el.scrollWidth > el.clientWidth + 2;
    if (parentExcess > 1 || ownScroll) elemOverflow.push({ el, box, parentExcess, ownScroll });
  }
  const scrollWidth = Math.max(document.documentElement.scrollWidth, document.body?.scrollWidth || 0);
  const pageOverflows = scrollWidth > window.innerWidth;
  let reported = elemOverflow;
  if (pageOverflows) {
    const crossing = elemOverflow.filter(item => item.box.left < -1 || item.box.right > window.innerWidth + 1);
    reported = crossing.length ? crossing : elemOverflow;
    if (!reported.length) {
      const all = [...document.querySelectorAll('body *')].filter(el => visible(el) && !['SCRIPT', 'STYLE'].includes(el.tagName));
      const edge = all.filter(el => { const r = el.getBoundingClientRect(); return r.left < -1 || r.right > window.innerWidth + 1 || el.scrollWidth > el.clientWidth + 1; });
      const edgeSet = new Set(edge);
      const leaves = edge.filter(el => ![...el.children].some(child => edgeSet.has(child))).slice(0, 4);
      reported = leaves.map(el => ({ el, box: rectOf(el.getBoundingClientRect()), parentExcess: 0, ownScroll: el.scrollWidth > el.clientWidth + 1 }));
    }
  }
  const uniqueReported = new Map();
  for (const item of reported) uniqueReported.set(describe(item.el), item);
  for (const item of uniqueReported.values()) {
    const note = item.parentExcess > 1 ? `exceeds parent column by ${item.parentExcess.toFixed(1)}px` : item.ownScroll ? `scrollWidth ${item.el.scrollWidth}px > clientWidth ${item.el.clientWidth}px` : 'extends beyond viewport edge';
    const pageNote = pageOverflows ? `; document scrollWidth ${scrollWidth}px > innerWidth ${window.innerWidth}px` : '';
    add(null, 'OVERFLOW', `${describe(item.el)} ${note}${pageNote}`);
  }
  return findings;
}

const pages = await listPages(opts.siteRoot);
let browser;
try { browser = await chromium.launch({ executablePath: opts.chromePath, headless: true }); }
catch (error) {
  const rows = opts.widths.map(width => ({ course: '', page: '<browser>', width, step: '', stepIndex: '', panel: '', svg: '', caption: '', kind: 'ERROR', label: '', detail: `browser launch failed: ${String(error?.message || error).replace(/\s+/g, ' ').slice(0, 200)}` }));
  await writeCsv(rows, opts.outFile);
  console.error(`Browser launch failed; ERROR row written to ${opts.outFile}`);
  process.exit(1);
}
const context = await browser.newContext({ viewport: { width: opts.widths[0], height: 900 } });
const page = await context.newPage();
const results = [];
const baseUrl = opts.baseUrl.endsWith('/') ? opts.baseUrl : `${opts.baseUrl}/`;

for (const width of opts.widths) {
  await page.setViewportSize({ width, height: 900 });
  for (const item of pages) {
    let currentStep = '';
    try {
      const response = await page.goto(new URL(item.route, baseUrl).href, { waitUntil: 'load', timeout: 30000 });
      if (response && !response.ok()) throw new Error(`HTTP ${response.status()} for ${item.route}`);
      const readiness = await page.evaluate(async () => {
        const fonts = await Promise.race([
          document.fonts.ready.then(() => 'ready'),
          new Promise(resolve => setTimeout(() => resolve('timeout'), 15000))
        ]);
        if (fonts !== 'ready') return { error: 'document.fonts.ready timed out' };
        const imgs = [...document.images];
        imgs.forEach(img => { if (img.loading === 'lazy') img.loading = 'eager'; });
        window.scrollTo(0, document.documentElement.scrollHeight);
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
        const imageResult = await Promise.race([
          Promise.all(imgs.filter(img => img.currentSrc || img.src).map(async img => {
            try { await img.decode(); return ''; } catch { return img.currentSrc || img.src; }
          })).then(failed => failed.find(Boolean) || ''),
          new Promise(resolve => setTimeout(() => resolve('timeout'), 15000))
        ]);
        window.scrollTo(0, 0);
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
        return imageResult === 'timeout' ? { error: 'lazy image readiness timed out' }
          : imageResult ? { error: `lazy image failed to load: ${imageResult}` } : { ready: true };
      });
      if (readiness.error) throw new Error(readiness.error);

      const steps = await page.evaluate(() => [...document.querySelectorAll('.step[data-panel]')].map((step, index) => ({
        index: index + 1,
        panel: (step.getAttribute('data-panel') || '').trim().split(/[\s,]+/)[0],
        title: (step.querySelector('h3')?.textContent || step.querySelector('.label')?.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 80)
      })));
      for (const step of steps) {
        currentStep = `step ${step.index}${step.title ? ` · ${step.title}` : ''}`;
        const activation = await page.evaluate(async ({ panelId }) => {
          const target = document.getElementById(panelId);
          if (!target) return { missing: panelId };
          const scope = target.closest('.scrolly') || target.closest('.stage') || target.parentElement;
          if (scope) for (const panel of scope.querySelectorAll('svg.panel')) panel.classList.toggle('on', panel === target);
          target.classList.add('on');
          await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
          return { ready: true };
        }, { panelId: step.panel });
        if (activation.missing) {
          results.push({ course: item.course, page: item.page, width, step: currentStep, stepIndex: step.index, panel: step.panel, svg: '', caption: '', kind: 'ERROR', label: '', detail: `data-panel target #${activation.missing} not found` });
          continue;
        }
        for (const finding of await page.evaluate(probe, { width, step: currentStep, stepIndex: step.index, focusPanelId: step.panel })) results.push({ course: item.course, page: item.page, ...finding });
      }
      currentStep = steps.length ? 'initial/static' : '';
      const steppedPanels = steps.map(step => step.panel);
      for (const finding of await page.evaluate(probe, { width, step: currentStep, stepIndex: '', skipPanelIds: steppedPanels })) results.push({ course: item.course, page: item.page, ...finding });
    } catch (error) {
      results.push({ course: item.course, page: item.page, width, step: currentStep, stepIndex: '', panel: '', svg: '', caption: '', kind: 'ERROR', label: '', detail: String(error?.message || error).replace(/\s+/g, ' ').slice(0, 240) });
    }
  }
}

await browser.close();
const uniqueResults = new Map();
for (const finding of results) {
  const stepKey = ['OVERFLOW', 'ERROR'].includes(finding.kind) ? '' : `${finding.stepIndex}:${finding.step}`;
  const key = [finding.course, finding.page, finding.width, stepKey, finding.panel, finding.kind, finding.label, finding.detail].join('\u0000');
  if (!uniqueResults.has(key)) uniqueResults.set(key, finding);
}
const findings = [...uniqueResults.values()];
await writeCsv(findings, opts.outFile);
for (const width of opts.widths) console.log(`${width}px: ${findings.filter(result => result.width === width).length} findings`);
console.log(`CSV: ${opts.outFile}`);
if (findings.length) process.exitCode = 1;
