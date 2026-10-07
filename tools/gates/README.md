# Staging capture and geometry gate

`gate.mjs` captures a staging site without editing it. It writes full-page screenshots for every manifest page at desktop (1280×960) and phone (390×844), in light and dark themes. It also writes optional selector crops and `gate-report.json`.

The default target is `http://127.0.0.1:8767/`. With no manifest, the runner captures `/`. Pass a manifest path and output directory as needed:

```sh
node \
  tools/gates/gate.mjs \
  --manifest /absolute/path/to/gate-manifest.json \
  --output /absolute/path/to/captures \
  --base-url http://127.0.0.1:8767/
```

The runner uses the bundled Playwright module and `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`. It waits for `document.fonts.ready` before measurement and capture.

## Manifest

```json
{
  "localStorage": { "demo-mode": "bookmarks" },
  "pages": [
    {
      "name": "home",
      "path": "/",
      "selectors": ["header", { "name": "home-art", "selector": ".home-art" }]
    },
    {
      "name": "course-index",
      "path": "/courses/sample/index.html",
      "localStorage": { "demo-mode": "bookmark-seed" },
      "artSelector": "main svg"
    }
  ]
}
```

`pages` is required when a manifest is supplied. Each `path` resolves against `--base-url`; `name` controls screenshot filenames. Optional `localStorage` entries seed browser storage before page scripts run. Page-level values override global values. The runner sets `ordenacoes-theme` and `document.documentElement.dataset.theme` for each light/dark pass, matching the site theme convention. `selectors` may be selector strings or `{ "name", "selector" }` objects; `artSelector` is a shorthand for one selected art crop. Missing selectors are listed in the JSON report.

## Report fields

Each state records the actual theme and viewport, screenshot paths, inspect target, uncaught page errors and console errors, document horizontal overflow (only when it exceeds the viewport by more than 1 CSS px), duplicate IDs, visible SVG host rectangles that overflow horizontally, visible SVG text outside its `viewBox`, and overlapping visible SVG text bounds. Text bounds are converted through SVG screen matrices into the outer SVG coordinate system so nested SVG transforms are included. Hidden content, zero-size text, and definitions such as `defs`, `symbol`, and `clipPath` do not count.

To make a later bookmarks/demo state easy to locate in the report, mark its visible host with `data-gate-inspect`; its text and rectangle are recorded as `geometry.inspect`. The gate reports measurements and captures evidence; review the images and decide which findings need a repair.
