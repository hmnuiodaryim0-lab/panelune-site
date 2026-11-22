# Panelune SEO 第二阶段审计

研究／实施日期：2026-11-22（Asia/Shanghai）。基线：网站 `2249db6c72e394a52d904cd233e556a66ea56b57`，干净 main。部署：GitHub Pages legacy，main 分支根目录。App 功能依据只读的 `685569e`／`panelune-v1.1.1-pre-iphone-duo` 基线。

## 发现与证据

| 发现 | 证据 | 本轮处理 |
|---|---|---|
| 基础 SEO 已完成，不需要重做 | 五语言静态 HTML、独立 canonical、互惠 hreflang、7 URL Sitemap、JSON-LD、图片和响应式；原有 4 项测试通过 | 保留原结构与优化 |
| 首页标题未明确当前可用设备；功能宣传缺少操作型入口 | 基线五语言 soonTitle 为通用阅读器；除首页外只有 Privacy/Support | 标题明确 iPad，依据本地化搜索语境修描述；新增两组完整指南 |
| 旧版 Files 入口容易被理解为单文件导入 | 网站原文泛称 Files import；1.1.1 `LibraryRootView.swift` 只有 Link Folder 的文件夹选择器；独立 FilesImportView 属于当前开发中的版本 | 修正五语言首页与英文 Support，指南明确 1.1.1 具体步骤 |
| 未有搜索平台验证接入位置 | 基线未配置 Google/Bing 标签；无后台数据 | 可选配置、生成器安全转义；用户已提供真实 Google token，本轮纳入部署。Bing 保持空值 |
| 项目 robots 不能作为域名根规则 | 匿名线上首页 HTTP 200、10,485 字节完整 HTML；origin `/robots.txt` HTTP 404；项目文件位于 `/panelune-site/robots.txt` | 保留项目文件但不宣称其控制抓取；提供 Sitemap 直接提交路径与根规则复查 |
| 没有可衡量的搜索基线 | 未获得 Search Console/Bing Performance 或索引报告 | 建立 7/30/90 天记录模板，值标未知，发布 HTTP 回执与搜索成效分开 |

公开搜索的站点查询未返回可确认的官网结果，但这**不是未收录结论**。Google 明确指出 `site:` 结果不完整，不能据此计算收录量：[官方说明](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site?hl=en)。

## 已实施的增量

- 两组五语言指南，共 10 页；所有内容来自 JSON，由现有生成器维护。
- 每页真实静态正文、1 个 H1、明确步骤、页内目录、独立标题描述与 canonical、同主题互惠 hreflang（含 self 与英文 x-default）。
- 首页与 Support 导流；指南互链；英文法律／支持页面保留原 URL 并标明语言。
- Sitemap 从 7 增至 17 个实际 canonical URL；404 与源码路径不进入 Sitemap；不虚构 lastmod、priority 或 changefreq。
- 指南 JSON-LD 为 WebPage/BreadcrumbList；软件页面仍是已发布 iPad 1.1.1，没有评分、下载统计、FAQ 或 Duo 支持声明。
- `content/search-verification.json` 接收真实 Google/Bing meta content；默认空值不输出。本轮 Google 值来自用户提供的标签，Bing 为空；没有伪造文件或 token。
- 只读 `scripts/check_live.py` 与回归测试，未引入运行时依赖、分析代码、Cookie、外部字体或大图。

## 状态分类

1. **已完成且已验证**：源码基线审计、公开搜索采样、静态生成与本地自动检查。最终测试数值和部署回执见下方验证记录／`DEPLOYMENT.md`。
2. **已修改但尚未验证收录效果**：标题描述、新指南、站内链接和 Sitemap。无真实曝光或点击数据，不推算效果。
3. **需要用户手动验证**：Search Console 点击验证与 Sitemap 提交、Bing 添加属性／真实 token／验证和提交；必要的实机菜单抽查。
4. **以后依据真实数据优化**：实际查询与内容匹配、页面 CTR、Google 选择的 canonical、各市场曝光差异、第三个内容主题。

## 技术边界

- GitHub Pages 子路径本身可以承载完整可抓取 HTML；它不赋予本项目对 origin robots 或 github.io DNS 的控制权。使用 URL-prefix HTML tag 验证更贴合当前权限范围。
- 未迁移域名，不认为自定义域名必然提升排名。中国大陆不同网络下的 github.io 可用性未做实测，不从本次访问推出全市场可用性。
- `/index.html` 与目录 URL 由 Pages 同时提供时，以目录 canonical 为准，不虚称服务器已做重定向。
- JSON-LD 验证包括解析、类型、版本、设备和 URL 合同；没有声称 Google Rich Results Test 通过或保证富结果资格。
- 相同主题的五语言内容是完整本地化页面；法律与 Support 只有英文，不伪造其他版本。
- 图片未增加、原图片 alt 与尺寸/lazy loading 回归检查保留。没有真实用户 CrUX 数据。
- IndexNow 已评估但未启用，原因与未来 keyLocation 范围见接入清单；没有提交回执可报告。

## 本地验证记录

- 新增测试先失败于缺失指南、互链、Sitemap 与验证标签输出，再实现通过。
- 10 项 Python unittest 通过：完整生成一致性、全站本地链接／锚点、5 语言与两个发布分支、17 URL Sitemap、同主题语言互链、验证标签空值与转义、当前发布状态、robots 指令规范化。
- 首页浏览器：30 个语言／视口组合通过，8 页 axe 无违规，语言切换／历史／无 JS 导航通过。
- 首页移动端 Lighthouse：Performance 100、Accessibility 100、Best Practices 100、SEO 100；LCP 0.8s，TBT 60ms，CLS 0。仅本地实验室测量，非线上真实用户分数。
- 指南浏览器：30 个语言／视口组合通过，10 页 axe 无违规；无 JS 语言导航保留同主题。
- 指南单独复测移动端 Lighthouse 四项 100；LCP 0.8s，TBT 50ms，CLS 0。首次与浏览器批测并行时性能 91、TBT 390ms，报告显示 0 个脚本和不可归因长任务；停止并发测试后以相同参数复测，没有修改页面来追分。
- 独立审查通过；修复监测脚本带空格 robots 指令的漏报，并以失败到通过的回归测试验证。
- 最终线上验证记录到 `DEPLOYMENT.md`。

## 文件与维护入口

- [关键词研究](KEYWORD-RESEARCH.md)：查询记录、30 个候选词、来源、搜索量未知、五语言策略。
- [内容策略](CONTENT-STRATEGY.md)：已发布功能证据、两主题选择与维护方法。
- [接入清单](INDEXING-SETUP.md)：Google/Bing 与 IndexNow 条件。
- [监测方案](SEO-MONITORING.md)：7/30/90 天步骤、无数据边界、复查命令。
- `scripts/build.py`、`scripts/check_live.py`、`content/guides/*.json`、`content/search-verification.json`。
- 五语言首页 JSON、`templates/support.html`、`styles.css`、生成后的主页／指南／Support／Sitemap。
- `tests/test_seo.py`、扩展 `tests/test_site.py`、`tests/guides-browser.cjs`。

来源：[Google robots 规则范围](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt)、[多语言版本](https://developers.google.com/search/docs/specialty/international/localized-versions)、[Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)。

App Store 外链：本次本机网络中 region-neutral 和显式 US 地址均返回 200 后落到 CN Today 首页，不能当作详情页可访问的证据。公开网页读取后端可读取 [US 产品详情](https://apps.apple.com/us/app/panelune/id6807220447)，仍为 iPad 1.1.1。保留真实 App ID 和原链接，不改变商店分发设置；用户可从目标市场设备抽查区域重定向。
