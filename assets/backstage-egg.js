/* Backstage: an Easter egg on the home page's paper. Nothing announces it.
   The drafting grid is pinned to the window on desktop (120 px squares of 5×5 cells of 24 px).
   In the square at column 2, row 3, four cells answer a click with a brief flash. Clicked clockwise
   from the top left, each within 2 s of the last, they mark the corners of a cut: the knife runs
   along the square's left, top and right edges, and the sheet falls away from the reader, hinged
   at its bottom, showing the other side of the paper (the other theme) and the way backstage.
   Desktop and landscape only; reduced motion fades instead of folding. Chairman's idea, 07/10. */
(function () {
  var mq = window.matchMedia('(min-width: 1100px) and (hover: hover) and (pointer: fine) and (orientation: landscape)');
  var MAJOR = 120, CELL = 24, SQ = { x: 120, y: 240 };           // column 2, row 3 of the pinned grid
  var CORNERS = [[1, 1], [2, 1], [2, 2], [1, 2]];                 // TL, TR, BR, BL inside the square
  var TINT = ['var(--dif)', 'var(--conc)', '#e8c547', 'var(--ink)'];
  var WINDOW_MS = 2000, step = 0, last = 0, open = false, layer = null;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  var css = document.createElement('style');
  css.textContent =
    '.bs-flash{position:fixed;width:' + CELL + 'px;height:' + CELL + 'px;pointer-events:none;z-index:60;opacity:0;animation:bs-flash .75s ease-out forwards}' +
    '@keyframes bs-flash{0%{opacity:0;transform:scale(.6)}18%{opacity:.9;transform:scale(1)}100%{opacity:0;transform:scale(1.15)}}' +
    '.bs-stage{position:fixed;left:' + SQ.x + 'px;top:' + SQ.y + 'px;width:' + MAJOR + 'px;height:' + MAJOR + 'px;z-index:55;perspective:520px}' +
    '.bs-under{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:6px;box-shadow:inset 0 0 18px rgba(0,0,0,.45);opacity:0;transition:opacity .25s ease .2s}' +
    '.bs-stage.on .bs-under{opacity:1}' +
    '.bs-under a{font:600 12px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;text-decoration:none;padding:7px 9px;border:1.5px solid currentColor}' +
    '.bs-under a:focus-visible{outline:2px solid var(--conc);outline-offset:3px}' +
    '.bs-under small{font:400 9px/1.3 var(--mono);letter-spacing:.08em;text-transform:uppercase;opacity:.65}' +
    '.bs-flap{position:absolute;inset:0;transform-origin:50% 100%;background-color:var(--paper);background-image:linear-gradient(var(--grid-major) 1px,transparent 1px),linear-gradient(90deg,var(--grid-major) 1px,transparent 1px),linear-gradient(var(--grid) .5px,transparent .5px),linear-gradient(90deg,var(--grid) .5px,transparent .5px);background-size:120px 120px,120px 120px,24px 24px,24px 24px;background-position:0 0;backface-visibility:hidden;transition:transform .9s cubic-bezier(.55,.05,.75,.45),filter .9s;will-change:transform}' +
    '.bs-stage.on .bs-flap{transform:rotateX(86deg);filter:brightness(.72);pointer-events:none}' +
    '.bs-stage.lift .bs-flap{transition:transform .55s cubic-bezier(.2,.7,.3,1),filter .55s}' +
    '.bs-cut{position:absolute;inset:-1px;overflow:visible;pointer-events:none}' +
    '.bs-cut path{fill:none;stroke:var(--ink);stroke-width:1.6;stroke-dasharray:360;stroke-dashoffset:360;animation:bs-cut .45s ease-in forwards}' +
    '@keyframes bs-cut{to{stroke-dashoffset:0}}' +
    '@media (prefers-reduced-motion: reduce){.bs-flap{transition:opacity .3s}.bs-stage.on .bs-flap{transform:none;opacity:0}.bs-cut path{animation:none;stroke-dashoffset:0}}';
  document.head.appendChild(css);

  // the other side of the paper is the other theme
  function otherSide() {
    var dark = document.documentElement.dataset.theme === 'dark';   // the site goes dark only through its own toggle
    return dark
      ? { bg: '#efe9da', ink: '#1d2530', grid: '#d8d2c0', major: '#c9c1aa' }
      : { bg: '#15181d', ink: '#e5e3da', grid: '#1a1e25', major: '#252a32' };
  }

  function flash(i) {
    var d = document.createElement('div');
    d.className = 'bs-flash';
    d.style.left = (SQ.x + CORNERS[i][0] * CELL) + 'px';
    d.style.top = (SQ.y + CORNERS[i][1] * CELL) + 'px';
    d.style.background = TINT[i];
    d.style.boxShadow = '0 0 14px 3px ' + TINT[i];
    document.body.appendChild(d);
    setTimeout(function () { d.remove(); }, 800);
  }

  function reveal() {
    open = true;
    var s = otherSide();
    layer = document.createElement('div');
    layer.className = 'bs-stage';
    layer.innerHTML =
      '<div class="bs-under" style="background:' + s.bg + ';color:' + s.ink + ';background-image:linear-gradient(' + s.major + ' 1px,transparent 1px),linear-gradient(90deg,' + s.major + ' 1px,transparent 1px),linear-gradient(' + s.grid + ' .5px,transparent .5px),linear-gradient(90deg,' + s.grid + ' .5px,transparent .5px);background-size:120px 120px,120px 120px,24px 24px,24px 24px">' +
      '<a href="backstage/" style="color:' + s.ink + '">Backstage&nbsp;→</a><small>behind the paper</small></div>' +
      '<div class="bs-flap" style="background-position:-' + SQ.x + 'px -' + SQ.y + 'px"></div>' +
      '<svg class="bs-cut" viewBox="0 0 ' + MAJOR + ' ' + MAJOR + '" width="' + (MAJOR + 2) + '" height="' + (MAJOR + 2) + '" aria-hidden="true"><path d="M1 ' + (MAJOR + 1) + ' V1 H' + (MAJOR + 1) + ' V' + (MAJOR + 1) + '"/></svg>';
    document.body.appendChild(layer);
    var cut = layer.querySelector('.bs-cut');
    setTimeout(function () {
      layer.classList.add('on');
      setTimeout(function () { if (cut) cut.style.opacity = '0'; }, reduce.matches ? 50 : 700);
    }, reduce.matches ? 0 : 480);
  }

  function close() {
    if (!layer) return;
    var l = layer; layer = null; open = false;
    l.classList.add('lift'); l.classList.remove('on');
    setTimeout(function () { l.remove(); }, 650);
  }

  function onPaper(t) {
    return !t.closest('a,button,input,label,summary,details,nav,header,footer,h1,h2,h3,p,li,svg,figure,.prancha,.patch-bento,.about,.hist-card');
  }

  // the egg exists only where all four cells are open paper (window ≥ ~1,500 px: the course cards sit right of column 2)
  function allClear() {
    return CORNERS.every(function (c) {
      var el = document.elementFromPoint(SQ.x + c[0] * CELL + CELL / 2, SQ.y + c[1] * CELL + CELL / 2);
      return el && (el.classList.contains('bs-flash') || onPaper(el));
    });
  }

  document.addEventListener('click', function (e) {
    if (!mq.matches) return;
    if (open) { if (!layer.contains(e.target)) close(); return; }
    if (!onPaper(e.target) || !allClear()) return;
    var cx = Math.floor((e.clientX - SQ.x) / CELL), cy = Math.floor((e.clientY - SQ.y) / CELL);
    var i = -1;
    for (var k = 0; k < 4; k++) if (CORNERS[k][0] === cx && CORNERS[k][1] === cy) i = k;
    var now = Date.now();
    if (i < 0) { step = 0; return; }
    flash(i);
    if (now - last > WINDOW_MS) step = 0;
    last = now;
    if (i === step) { step++; } else { step = (i === 0) ? 1 : 0; }
    if (step === 4) { step = 0; setTimeout(function () { CORNERS.forEach(function (_, j) { flash(j); }); reveal(); }, 260); }
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && open) close(); });
})();
