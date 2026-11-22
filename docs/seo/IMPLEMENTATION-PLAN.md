# SEO phase 2 implementation plan — 2026-11-22

> Execution: superpowers:executing-plans, inline implementation and final independent review.

Goal: make published Panelune iPad functionality discoverable through useful localized documentation and prepare measurable indexing.
Architecture: keep the standard-library Python generator, source JSON and committed static HTML; add two guide families, no runtime dependency.
Spec: user's SEO phase 2 request supplied 2026-11-22.

Constraints: do not modify Panelary; iphoneReleaseStatus = coming-soon; published schema = iPad 1.1.1; no invented functionality, ranking, traffic, verification tokens, analytics or forced push. Ordinary main push and deployment verification explicitly authorized.

Decision: work in an isolated temporary copy of the clean site checkout, then install reviewed changes in the requested checkout. This avoids writes to the App and keeps target mutations reviewable.
Decision: publish import and library guides in all five languages. Defer the advanced EPUB guide until release-specific settings can be documented without confusing 1.1.1 and 1.2.0.

Review focus: nested project paths; same-topic reciprocal hreflang; links without JavaScript; pending release vs actual baseline functionality; real verification tokens only, safely escaped.

- [x] Record live/source audit and real search samples, including volume-unknown labels.
- [x] Add failing tests in tests/test_seo.py: 17 sitemap URLs, per-topic alternates, heading/metadata/schema, crawl graph, blank/escaped verification configuration.
- [x] Extend scripts/build.py with localized guide rendering, topic-specific head alternates, homepage cards and optional verification tags. Source content/guides/*.json and content/search-verification.json.
- [x] Correct baseline import language in content/{locale}.json and templates/support.html; keep release configuration unchanged.
- [x] Add dependency-free live audit script, docs/seo reports and 7/30/90-day checks.
- [x] Generate; run full unittest suite, browser/axe checks across locales and viewports, mobile Lighthouse; visually inspect guides.
- [x] Independent final review; fix substantive issues and rerun relevant/full checks.
- [ ] Install reviewed files, commit, ordinary push main; wait for Pages and verify served HTML, sitemap, links and excluded source paths. Record receipts and remaining manual verification.

Execution decisions: user explicitly requested direct implementation and ordinary main push, so no redundant approval gates were added. Independent review found robots whitespace normalization; treated as monitoring correctness and fixed with a failing-then-passing test. No deferred code findings remain. Account verification and indexing require authorized account data and remain manual. App binary behavior was source-checked against 1.1.1, not represented as a new device test.
