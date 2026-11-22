# Launch readiness validation — 2026-11-22

Baseline: clean `main`, HEAD `8e319cc0fd640a5b4fec07e26147f0ff9f42dbac`.
Remote: `https://github.com/hmnuiodaryim0-lab/panelune-site.git`.
GitHub Pages: branch build (`legacy`), `main`, root `/`, HTTPS enabled.

## Product and release evidence

- Apple's US lookup API returned Panelune 1.1.1 and iPad-only supported devices.
- `content/site.json` remains `coming-soon`. No schema claims iPhone availability;
  the published schema reports version 1.1.1 and iPad. No fabricated rating, review,
  download count, offer price or Duo feature is emitted.
- Read-only source checks: device-owner authentication for Private Library, local
  TCP Wi-Fi server, StoreKit purchase/restoration, free Series limit of 3 allowing
  additions to existing Series, no collected/tracking data in the app manifest.
- ComicArchive reads ZIP structures. Support therefore explicitly distinguishes
  CBZ/ZIP from RAR-based CBR rather than advertising unverified support.
- Privacy stays English; existing clauses were preserved, with a narrow sourced
  explanation of Private Library and updated date. Original legal URLs retained.
- Support retains the existing email and restoration route, adds Files import,
  device/release availability, local network guidance, offline/linked-provider caveat,
  copyright guidance, regional pricing and the verified US Store link fallback.
- Panelary working-tree status and binary diff match the start-of-task snapshots.
  No App edits, Xcode builds or simulator operations performed.

## Verification

- `python3 -m unittest discover -s tests -v`: 4 tests pass, including both release
  states for five languages, deterministic generated output, local links, anchors,
  image attributes, canonical/hreflang and truthful structured data.
- `node --check site.js`: passes.
- Headless Chrome via `tests/browser.cjs`: 30 language/viewport combinations pass
  (five languages × 320, 375, 390, 768, 1024, 1440 px). No horizontal overflow,
  image decoding failures, page exceptions or failed local resource responses.
- Browser language changes preserve the current section/offset and update language,
  title, social metadata, canonical and schema. No-JS language links work.
- Independent read-only review found one history-position defect. Reproduced with
  #pro offset 158.71875 → 5828.71875 px after Back/Forward; corrected using per-entry
  position storage. Regression offset difference is now 0. Native fragment history
  is also covered and passes.
- Axe WCAG 2 A/AA and WCAG 2.1 AA checks: no violations on the five homepages,
  Privacy, Support or 404. Original Pro eyebrow contrast was corrected using the
  existing darker blue, preserving the palette.
- Final local Lighthouse (mobile simulation, Chrome): Performance 100,
  Accessibility 100, Best Practices 100, SEO 100. LCP 0.8 s, TBT 10 ms, CLS 0.
  These are local lab measurements, not claims about real-world network performance.
- All five mobile hero layouts and desktop/full-page gallery were visually inspected.
- Original demo screenshot provenance and all 20 selected iPhone scenes were reviewed.
  See assets.md for compression details. No runtime third-party dependencies added.

## Hosting boundaries

The project includes a discoverable sitemap and non-blocking robots.txt. A robots.txt
under `/panelune-site/` cannot control the origin; origin-root rules belong to the
GitHub account site. Real five-language static pages have reciprocal hreflang;
English Privacy/Support have canonical metadata but no invented language alternates.

The App Store neutral ID URL can redirect by storefront. In this environment it
redirected to the CN store homepage, so Support also offers Apple's verified US
product URL. This website cannot change Apple distribution settings.

Commit/push/deployment IDs and live URL verification are reported in the delivery
message after publishing; they are not fabricated in this pre-deployment record.
