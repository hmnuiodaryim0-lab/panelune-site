# Panelune 1.2.0 website launch plan

Goal: update the existing static GitHub Pages site for a pending iPhone release without changing the App or design stack.
Architecture: plain HTML/CSS, small progressively enhanced language navigation, Python standard-library generator. One content/site.json release switch generates all five static homepages and the English support page. English privacy stays English.
Spec: user's Panelune 1.2.0 website brief, 2026-11-22.

Constraints: preserve legal URLs, original design, main-root Pages deployment; one commit with requested message; no App edits/builds; no Duo claims; only reviewed original demo screenshots; no uniform regional price.

- [x] Record clean HEAD/remote/Pages config; verify source behavior and screenshot provenance.
- [x] Add single release configuration, five translations, static metadata and real reciprocal language URLs; verify both release states and no-JS output.
- [x] Compress existing real UI, extend responsive gallery, update English support and narrowly clarify privacy.
- [x] Check links, image loading, small-phone/tablet/desktop layouts, language/scroll/history, keyboard/no-JS, accessibility and Lighthouse; independent final review.
- [ ] Review exact diff and asset inventory, copy reviewed files to the original clean repo, commit once, push main without force, verify Pages commit and live URLs.

Review focus: stale metadata after release change; relative links from nested languages; text reflow/scroll after switching; no-JS discoverability; upcoming features accidentally described as already shipped.

Decisions: original repository stays the deployment checkout; temporary staging and QA artifacts live under /tmp. Generated HTML is committed so existing branch-based Pages needs no new build service. App Store primary button preserves the requested region-neutral ID URL, with a verified US listing in Support because the current local storefront redirects the neutral URL to its homepage.
