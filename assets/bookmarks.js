/* CUFRGS · caderno: chapter bookmarks kept in this browser. */
(function () {
  'use strict';
  var path = normalizePath(location.pathname);
  if (!path || /\/index\.html$/i.test(location.pathname) || !/^\/courses\//.test(path)) return;
  if (!/\.html$/i.test(path) || !/^\/courses\/[a-z0-9-]+\/(?:aula-[a-z0-9][a-z0-9-]*|unidade-[a-z0-9][a-z0-9-]*|suplemento-[a-z0-9][a-z0-9-]*|revisao(?:-[a-z0-9][a-z0-9-]*)?)\.html$/i.test(path)) return;

  var KEY = 'ordenacoes-bm';
  var BLOCK = 'p,li,td,th,blockquote,figcaption,dd,dt,h2,h3,h4';
  var SKIP = 'nav,button,select,input,textarea,summary,svg,script,style,label,[contenteditable],.topbar,.label,.kicker,.titleblock,.endnav,.course-nav,.stage,.deck-wrap,.deck-tools,.art-tools,.art-key,.heading-anchor,.chapter-nav,.chapter-pagination,.skip-link,.site-return,.num,.tag,.cu-pop,.cu-hlbar';
  var pageHeadings = Array.prototype.slice.call(document.querySelectorAll('h2'));
  if (!pageHeadings.length) return;

  function normalizePath(value) {
    if (typeof value !== 'string' || value.length > 300) return '';
    var p = value.split(/[?#]/)[0].replace(/\\/g, '/');
    if (p.charAt(0) !== '/') p = '/' + p;
    p = p.replace(/\/index\.html$/i, '/');
    return p;
  }
  function safeText(value, max) {
    return String(value || '').replace(/\s+/g, ' ').trim().slice(0, max);
  }
  function safeMark(item) {
    return !!item && typeof item === 'object' && normalizePath(item.path) === path &&
      /^\/courses\/[a-z0-9-]+\/[a-z0-9][a-z0-9._-]*\.html$/i.test(item.path) &&
      typeof item.chapterId === 'string' && item.chapterId.length > 0 && item.chapterId.length <= 120 &&
      typeof item.chapterTitle === 'string' && item.chapterTitle.length <= 240 &&
      typeof item.course === 'string' && item.course.length <= 160 &&
      typeof item.lessonTitle === 'string' && item.lessonTitle.length <= 240 &&
      typeof item.created === 'string' && item.created.length <= 40;
  }
  function readMarks() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw || raw.length > 200000) return [];
      var parsed = JSON.parse(raw);
      if (!Array.isArray(parsed)) return [];
      return parsed.filter(safeMark).map(function (m) {
        return { path: m.path, course: m.course, lessonTitle: m.lessonTitle, chapterId: m.chapterId,
          chapterTitle: m.chapterTitle, created: m.created };
      });
    } catch (e) { return []; }
  }
  var marks = readMarks();
  // the <title> ends with the course name; the h1's innerText keeps the space where a split span breaks the line
  var titleParts = String(document.title || '').split(' · ');
  var course = safeText(titleParts.length > 1 ? titleParts[titleParts.length - 1] : '', 160);
  var lessonTitle = safeText(document.querySelector('h1') && String(document.querySelector('h1').innerText || document.querySelector('h1').textContent).replace(/\s+/g, ' '), 240) || safeText(document.title, 240);

  var css = document.createElement('style');
  css.textContent =
    '.cu-bm-toggle{display:inline-grid;place-items:center;vertical-align:middle;width:40px;height:40px;margin-left:.4em;padding:0;border:0;background:transparent;color:var(--ink-2);cursor:pointer;touch-action:manipulation}' +
    '.cu-bm-toggle svg{display:block;width:21px;height:25px;overflow:visible}' +
    '.cu-bm-toggle .cu-bm-paper{fill:var(--paper-2);stroke:currentColor;stroke-width:1.6;stroke-linejoin:miter}' +
    '.cu-bm-toggle .cu-bm-fold{fill:none;stroke:currentColor;stroke-width:1.4;stroke-linejoin:miter}' +
    '.cu-bm-toggle[aria-pressed="true"]{color:var(--conc)}.cu-bm-toggle[aria-pressed="true"] .cu-bm-paper{fill:var(--conc-wash);stroke:var(--conc)}' +
    '.cu-bm-toggle:hover,.cu-bm-toggle:focus-visible{color:var(--conc)}.cu-bm-toggle:focus-visible{outline:2px solid var(--dif);outline-offset:2px}' +
    '.chapter h2,.reading-sheet h2{position:relative}' +
    '.cu-bm-margin{position:fixed;z-index:8;top:112px;left:8px;display:none;pointer-events:none;color:var(--conc)}' +
    '.cu-bm-margin svg{display:block;width:22px;height:27px;filter:drop-shadow(1px 1px 0 var(--paper))}' +
    '.cu-bm-margin .cu-bm-paper{fill:var(--conc-wash);stroke:var(--conc);stroke-width:1.6;stroke-linejoin:miter}' +
    '.cu-bm-margin .cu-bm-fold{fill:none;stroke:var(--conc);stroke-width:1.4;stroke-linejoin:miter}' +
    '.cu-bm-margin.is-visible{display:block}' +
    '@media(max-width:600px) and (orientation:portrait){.cu-bm-toggle{width:36px;height:36px;margin-left:.25em}.cu-bm-margin{display:none!important}}' +
    '@media(prefers-reduced-motion:reduce){.cu-bm-toggle,.cu-bm-margin{scroll-behavior:auto;animation:none!important;transition:none!important}}' +
    '@media print{.cu-bm-toggle,.cu-bm-margin{display:none!important}}';
  document.head.appendChild(css);

  function ribbonSvg() {
    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 20 25'); svg.setAttribute('aria-hidden', 'true');
    var paper = document.createElementNS(svg.namespaceURI, 'path');
    paper.setAttribute('class', 'cu-bm-paper'); paper.setAttribute('d', 'M4 2.5h12v20l-6-4-6 4z');
    var fold = document.createElementNS(svg.namespaceURI, 'path');
    fold.setAttribute('class', 'cu-bm-fold'); fold.setAttribute('d', 'M4.8 3.3h10.4v17.7L10 17.6l-5.2 3.4z');
    svg.appendChild(paper); svg.appendChild(fold); return svg;
  }
  function slug(text) {
    var value = safeText(text, 180).toLocaleLowerCase('pt-BR');
    try { value = value.normalize('NFD').replace(/[\u0300-\u036f]/g, ''); } catch (e) {}
    return value.replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 72) || 'capitulo';
  }
  var used = Object.create(null);
  Array.prototype.forEach.call(document.querySelectorAll('[id]'), function (el) { used[el.id] = true; });
  pageHeadings.forEach(function (h) {
    if (!h.id) {
      var base = slug(h.textContent), id = base, n = 2;
      while (used[id] || document.getElementById(id)) id = base + '-' + n++;
      h.id = id; used[id] = true;
    }
  });

  function isMarked(id) { return marks.some(function (m) { return m.path === path && m.chapterId === id; }); }
  function syncButton(button, heading) {
    var active = isMarked(heading.id);
    button.setAttribute('aria-pressed', String(active));
    button.setAttribute('aria-label', active ? 'Desmarcar capítulo: ' + safeText(heading.textContent, 180) : 'Marcar capítulo: ' + safeText(heading.textContent, 180));
    button.title = active ? 'Desmarcar capítulo' : 'Marcar capítulo';
  }
  function persist(next) {
    try {
      if (next.length) localStorage.setItem(KEY, JSON.stringify(next));
      else localStorage.removeItem(KEY);
      return true;
    } catch (e) { return false; }
  }
  var sections = [];
  pageHeadings.forEach(function (heading) {
    var chapterTitle = safeText(heading.textContent, 240);
    var button = document.createElement('button');
    button.type = 'button'; button.className = 'cu-bm-toggle'; button.setAttribute('data-bookmark-toggle', ''); button.appendChild(ribbonSvg());
    syncButton(button, heading); heading.appendChild(button);
    var section = heading.closest('section') || heading.parentElement;
    sections.push({ heading: heading, section: section, button: button });
    button.addEventListener('click', function () {
      var found = isMarked(heading.id), next = marks.filter(function (m) { return !(m.path === path && m.chapterId === heading.id); });
      if (!found) {
        next.push({ path: path, course: course || path.split('/')[2], lessonTitle: lessonTitle,
          chapterId: heading.id, chapterTitle: chapterTitle, created: new Date().toISOString() });
      }
      if (!persist(next)) return;
      marks = next; syncButton(button, heading); updateMargin();
    });
  });

  var margin = document.createElement('span');
  margin.className = 'cu-bm-margin'; margin.setAttribute('aria-hidden', 'true'); margin.appendChild(ribbonSvg());
  document.body.appendChild(margin);
  function updateMargin() {
    var candidates = sections.filter(function (item) {
      if (!isMarked(item.heading.id)) return false;
      var rect = item.section.getBoundingClientRect();
      return rect.top < window.innerHeight * .58 && rect.bottom > 80;
    }).sort(function (a, b) { return b.heading.getBoundingClientRect().top - a.heading.getBoundingClientRect().top; });
    if (!candidates.length || window.innerWidth <= 600) { margin.classList.remove('is-visible'); return; }
    var rect = candidates[0].heading.getBoundingClientRect();
    margin.style.left = Math.max(8, rect.left - 46) + 'px';
    margin.classList.add('is-visible');
  }
  window.addEventListener('scroll', updateMargin, { passive: true });
  window.addEventListener('resize', updateMargin);
  updateMargin();

  function deepLinkHighlight() {
    var match = /^#hl=(.+)$/.exec(location.hash || '');
    if (!match) return;
    var id; try { id = decodeURIComponent(match[1]); } catch (e) { return; }
    if (!id || id.length > 160) return;
    var highlightKey = 'ordenacoes-hl:' + path;
    var highlight = null;
    try {
      var raw = localStorage.getItem(highlightKey);
      if (!raw || raw.length > 2000000) return;
      var list = JSON.parse(raw);
      if (!Array.isArray(list)) return;
      highlight = list.find(function (h) { return h && h.id === id && Number.isFinite(h.s) && Number.isFinite(h.e) && typeof h.q === 'string' && h.q.length <= 10000; });
    } catch (e) { return; }
    if (!highlight) return;

    var attempts = 0;
    function locate() {
      attempts++;
      var existing = document.querySelectorAll('mark.cu-hl[data-h]');
      var painted = Array.prototype.filter.call(existing, function (el) { return el.getAttribute('data-h') === id; });
      if (painted.length) {
        painted.forEach(function (el) { el.classList.add('cu-hl-return'); });
        var target = painted[0]; target.scrollIntoView({ block: 'center', behavior: reducedMotion() ? 'auto' : 'smooth' });
        window.setTimeout(function () { painted.forEach(function (el) { el.classList.remove('cu-hl-return'); }); }, 1500);
        return;
      }
      var idx = textIndex();
      var start = Math.max(0, Math.floor(highlight.s));
      if (idx.text.slice(start, start + highlight.q.length) !== highlight.q) {
        var found = idx.text.indexOf(highlight.q); if (found < 0) { if (attempts < 30) window.setTimeout(locate, 100); return; }
        start = found;
      }
      var point = offsetPoint(idx.nodes, start);
      if (point) {
        var range = document.createRange(); range.setStart(point.node, point.offset); range.collapse(true);
        var rect = range.getBoundingClientRect();
        if (rect.height || rect.top || rect.left) {
          window.scrollTo({ top: window.pageYOffset + rect.top - Math.min(180, window.innerHeight * .28), behavior: reducedMotion() ? 'auto' : 'smooth' });
          var parent = point.node.parentElement;
          if (parent) { parent.classList.add('cu-hl-return'); window.setTimeout(function () { parent.classList.remove('cu-hl-return'); }, 1500); }
          return;
        }
      }
      if (attempts < 30) window.setTimeout(locate, 100);
    }
    function textIndex() {
      var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, { acceptNode: function (node) {
        return node.nodeValue && node.parentElement && node.parentElement.closest(BLOCK) && !node.parentElement.closest(SKIP) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }});
      var nodes = [], parts = [], pos = 0, node;
      while ((node = walker.nextNode())) { nodes.push({ node: node, start: pos }); parts.push(node.nodeValue); pos += node.nodeValue.length; }
      return { nodes: nodes, text: parts.join('') };
    }
    function offsetPoint(nodes, offset) {
      for (var i = 0; i < nodes.length; i++) {
        var len = nodes[i].node.nodeValue.length;
        if (offset <= nodes[i].start + len) return { node: nodes[i].node, offset: Math.max(0, offset - nodes[i].start) };
      }
      return null;
    }
    function reducedMotion() { return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches; }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', locate, { once: true }); else locate();
  }
  var returnStyle = document.createElement('style');
  returnStyle.textContent = '.cu-hl-return{outline:2px solid var(--conc)!important;outline-offset:3px!important;transition:outline-color .2s}@media(prefers-reduced-motion:reduce){.cu-hl-return{transition:none}}';
  document.head.appendChild(returnStyle);
  deepLinkHighlight();
})();
