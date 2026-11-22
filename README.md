# Panelune website

Plain HTML/CSS on GitHub Pages, published from the root of `main`.
No framework, runtime packages, external fonts, analytics, or new hosting service.

## Edit and generate

`content/site.json` is the single source of truth for release availability:

```json
"iphoneReleaseStatus": "coming-soon"
```

Five complete homepages are generated from `content/{en,zh-Hans,zh-Hant,ja,ko}.json`.
English is `/`; other languages use their own directories. Each page has its own
canonical URL and reciprocal hreflang entries. Links work without JavaScript;
`site.js` enhances language switching to preserve the visible section and offset.
Privacy and Support remain at their original English URLs. Edit their source in
`templates/`; do not edit generated HTML directly.

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
```

Generated HTML is committed, so branch-based GitHub Pages does not need to run Python.
Keep `content/`, `templates/`, `scripts/`, `tests/`, and `docs/` excluded from Jekyll
publication using `_config.yml`.

## Release 1.2.0

Only after Apple approval **and actual App Store availability**:

1. Change `iphoneReleaseStatus` to `available` in `content/site.json`.
2. Run the build and tests above.
3. Review the diff: all five hero headings, badges, release notes, screenshot labels,
   reading-improvement notes, page/social titles, JSON-LD devices/version and Support
   availability update together.
4. Commit, push `main` without force, and verify the Pages build and live site.

Do not hand-edit state in individual HTML pages. Review Apple's current listing before
switching: approval with manual release pending does not mean the app is downloadable.

The primary download URL is the requested region-neutral App Store ID link. During
2026-11-22 verification it redirected to the CN storefront homepage on the local network;
Apple's US catalog verified Panelune 1.1.1. Support includes the verified US product URL
as a fallback. Storefront availability is controlled by Apple/the app's distribution settings.

## Assets and checks

See `docs/assets.md` for screenshot provenance and compression, `docs/launch-plan.md`
for scope. The gallery uses actual app screenshots with original demonstration books.
The existing three PNG files remain in Git for preservation, but are no longer loaded by
the homepage. Website image derivatives have no location/EXIF metadata.

`robots.txt` is included at the project path. Robots rules are only authoritative at an
origin's root (`https://hmnuiodaryim0-lab.github.io/robots.txt`); a project site cannot
control that origin file. No blocking robots directives are added. `sitemap.xml` contains
only the seven real, indexable pages; the custom 404 is `noindex`.

Optional browser regression suite (development only): install `playwright` and
`@axe-core/playwright` in a temporary directory, use an installed Chrome, start a local
HTTP server with the site mounted at `/panelune-site/`, then run:

```sh
NODE_PATH=/path/to/temporary/node_modules node tests/browser.cjs
```

`SITE_URL` overrides the preview URL; `QA_OUTPUT` chooses an external directory for
screenshots and JSON results. Covers 30 viewport/language pairs, local links/anchors,
image decoding, axe accessibility, no-JS links, metadata, language position, and history.
