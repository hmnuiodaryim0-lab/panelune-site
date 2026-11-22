# Screenshot provenance and compression

Reviewed 2026-11-22. No screenshots were fabricated or generated for this website.

- iPad library: existing `assets/screenshots/01-home.png`, matching the original demo books used by the app screenshot fixtures.
- iPhone: `~/Desktop/Panelune-iPhone-1.2.0-Screenshots/`, four scenes for each of five languages. `REPORT.txt`, `verification.json`, `Panelary/App/ScreenshotSupport.swift`, and `Scripts/capture_iphone_screenshots.py` document fictional/original covers, original comic art and original localized novel text. All 20 selected iPhone scenes were visually reviewed in a contact sheet. No user book content or private user data was selected.
- Wi-Fi screenshots contain the existing demonstration local address, not a live user's endpoint.
- Favicons and social image are resized copies of the existing AppIcon-1024.png.
- No App source, simulator or Xcode build was changed/run for the website task.

WebP quality 86, Lanczos resize: iPad 1600×1200, iPhone 804×1748. Original aspect ratios preserved, no UI alterations, crops or synthetic frames. Images include dimensions, translated alt text, async decoding and lazy loading.

| Website file | Original bytes | WebP bytes |
| --- | ---: | ---: |
| `assets/screenshots/ipad-library.webp` | 2159252 | 139872 |
| `assets/screenshots/en-library.webp` | 473620 | 49664 |
| `assets/screenshots/en-manga.webp` | 238087 | 14764 |
| `assets/screenshots/en-novel.webp` | 495691 | 135192 |
| `assets/screenshots/en-import.webp` | 145494 | 28220 |
| `assets/screenshots/zh-Hans-library.webp` | 470280 | 48596 |
| `assets/screenshots/zh-Hans-manga.webp` | 235614 | 14802 |
| `assets/screenshots/zh-Hans-novel.webp` | 625596 | 140232 |
| `assets/screenshots/zh-Hans-import.webp` | 135309 | 25326 |
| `assets/screenshots/zh-Hant-library.webp` | 470407 | 48730 |
| `assets/screenshots/zh-Hant-manga.webp` | 235614 | 14802 |
| `assets/screenshots/zh-Hant-novel.webp` | 651077 | 163710 |
| `assets/screenshots/zh-Hant-import.webp` | 140692 | 26060 |
| `assets/screenshots/ja-library.webp` | 476008 | 48546 |
| `assets/screenshots/ja-manga.webp` | 235614 | 14802 |
| `assets/screenshots/ja-novel.webp` | 706746 | 136014 |
| `assets/screenshots/ja-import.webp` | 154018 | 27122 |
| `assets/screenshots/ko-library.webp` | 450528 | 44484 |
| `assets/screenshots/ko-manga.webp` | 235614 | 14802 |
| `assets/screenshots/ko-novel.webp` | 513932 | 115122 |
| `assets/screenshots/ko-import.webp` | 134656 | 23566 |

Total: 9,383,849 → 1,274,428 bytes (86.4% smaller). Each language loads only its four iPhone shots plus the shared iPad shot.

Responsive small variants add 756,168 bytes across all languages: iPad 800×600 and iPhone 536×1165. `srcset`/`sizes` let the browser load only one size per image. Total committed WebP derivatives: 2,030,596 bytes; a page does not load both sizes or all languages.
