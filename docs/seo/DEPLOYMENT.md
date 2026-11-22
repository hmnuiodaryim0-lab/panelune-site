# 部署与最终验收记录

日期：2026-11-22（Asia/Shanghai）。

已部署并完成匿名线上验收。搜索平台所有权与收录状态仍待用户在后台确认。

已完成：Python 10 项测试、首页 30 个语言／视口组合与 8 页 axe 检查通过；指南 30 个布局、10 页 axe 与无 JS 同主题语言导航通过。首页与指南单独测量移动端 Lighthouse 均为四项 100。指南 LCP 0.8s、TBT 50ms、CLS 0；首次并发测量为 Performance 91／TBT 390ms，保留该记录，不代表线上性能。

测试环境问题：首次指南检查将 axe 与禁用 JavaScript 的浏览器上下文混用，卡在 axe。10 秒限定对照实验显示禁用 JS 时超时，启用时返回 0 违规。已将 axe 检查放入独立启用 JS 的上下文；指南布局与语言导航仍在无 JS 上下文执行。没有为此修改产品 JS。

真实 Google 验证值已由用户提供并纳入生成配置。Google 账户内的验证与 Sitemap 提交尚未执行；Bing 同样待接入。

独立审查：可部署。唯一监测脚本 robots 空白处理问题已修复，新增回归测试从失败到通过；完整 10 项测试通过。App 前后 git binary diff 和 porcelain status 一致，未修改 App 工程。

## Git 与 Pages 回执

- 功能提交：`44112b2` — Add localized reading guides and phase-two SEO indexing preparation。
- 首次普通 push 被远端新提交拒绝，没有强推。
- 远端 `def57454075939ce9f966cc9f08844d33522b514` 新增 `google3106aad1a8a588fd.html`；本轮原样保留，并合并。该文件不是本轮自行生成的验证材料。
- 成功部署提交：`a63cb9bb6e6b26645ac2087077a1188ed804fec6`。
- GitHub Pages API：`status=built`，`error.message=null`，完成时间 `2026-11-22T13:21:26Z`（北京时间 21:21:26）。
- 本记录及 JSON 回执会作为后续文档提交保存，不更改生成页面。

## 线上验收

检查时间：`2026-11-22T13:21:55.995859+00:00`（北京时间 21:21:55）。

- 17／17 个 Sitemap canonical URL：HTTP 200、最终 URL 正确、canonical 正确、未发现 noindex，响应字节与本地生成文件一致。
- Sitemap 与本地完全一致，包含五个首页、十个指南、Privacy、Support；不包含 404、源码或 Google 验证文件。
- Googlebot／bingbot UA 访问英文导入指南：200、完整 HTML，与本地一致；这只是 UA 模拟，不代表真实爬虫已抓取。
- 根目录 robots：404；未将项目级 robots 当作域名级抓取控制。
- 不存在页面、`docs/seo/SEO-AUDIT.md`、`content/search-verification.json`、`scripts/build.py`：均返回 404。
- CSS、现有 JS、Google 验证文件与本地字节一致。
- 首页原始 HTML 含用户提供的准确 Google 验证 Meta Tag；Google/Bing 账户内验证、Sitemap 提交未执行。
- 原始 HTTP 回执：[live-check.json](live-check.json)、[live-extra.json](live-extra.json)。

## 新增页面

| 语言 | 导入指南 | 书库整理 |
|---|---|---|
| English | [Import](https://hmnuiodaryim0-lab.github.io/panelune-site/guides/import-books/) | [Library](https://hmnuiodaryim0-lab.github.io/panelune-site/guides/organize-library/) |
| 简体中文 | [导入](https://hmnuiodaryim0-lab.github.io/panelune-site/zh-Hans/guides/import-books/) | [整理](https://hmnuiodaryim0-lab.github.io/panelune-site/zh-Hans/guides/organize-library/) |
| 繁體中文 | [匯入](https://hmnuiodaryim0-lab.github.io/panelune-site/zh-Hant/guides/import-books/) | [整理](https://hmnuiodaryim0-lab.github.io/panelune-site/zh-Hant/guides/organize-library/) |
| 日本語 | [取り込み](https://hmnuiodaryim0-lab.github.io/panelune-site/ja/guides/import-books/) | [整理](https://hmnuiodaryim0-lab.github.io/panelune-site/ja/guides/organize-library/) |
| 한국어 | [가져오기](https://hmnuiodaryim0-lab.github.io/panelune-site/ko/guides/import-books/) | [정리](https://hmnuiodaryim0-lab.github.io/panelune-site/ko/guides/organize-library/) |

## 回滚

如需撤回本轮功能，先确认最新 main 没有后续依赖，再使用 `git revert 44112b2` 生成反向提交，运行测试并普通 push。不要 reset／force push，也不要撤销合并提交而误删远端原有的 Google 验证文件。本轮未执行回滚。

## Changed files

- `README.md`
- `content/en.json`
- `content/guides/en.json`
- `content/guides/ja.json`
- `content/guides/ko.json`
- `content/guides/zh-Hans.json`
- `content/guides/zh-Hant.json`
- `content/ja.json`
- `content/ko.json`
- `content/search-verification.json`
- `content/zh-Hans.json`
- `content/zh-Hant.json`
- `docs/seo/CONTENT-STRATEGY.md`
- `docs/seo/DEPLOYMENT.md`
- `docs/seo/IMPLEMENTATION-PLAN.md`
- `docs/seo/INDEXING-SETUP.md`
- `docs/seo/KEYWORD-RESEARCH.md`
- `docs/seo/SEO-AUDIT.md`
- `docs/seo/SEO-MONITORING.md`
- `guides/import-books/index.html`
- `guides/organize-library/index.html`
- `index.html`
- `ja/guides/import-books/index.html`
- `ja/guides/organize-library/index.html`
- `ja/index.html`
- `ko/guides/import-books/index.html`
- `ko/guides/organize-library/index.html`
- `ko/index.html`
- `privacy.html`
- `scripts/build.py`
- `scripts/check_live.py`
- `sitemap.xml`
- `styles.css`
- `support.html`
- `templates/support.html`
- `tests/guides-browser.cjs`
- `tests/test_live_signals.py`
- `tests/test_seo.py`
- `tests/test_site.py`
- `zh-Hans/guides/import-books/index.html`
- `zh-Hans/guides/organize-library/index.html`
- `zh-Hans/index.html`
- `zh-Hant/guides/import-books/index.html`
- `zh-Hant/guides/organize-library/index.html`
- `zh-Hant/index.html`
- `docs/seo/live-check.json`
- `docs/seo/live-extra.json`

Remote verification file preserved separately: `google3106aad1a8a588fd.html`.
