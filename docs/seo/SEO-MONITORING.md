# SEO 监测机制

基准日期：2026-11-22，Asia/Shanghai。使用搜索引擎自有站长工具和无追踪的技术检查；没有安装访问统计、Cookie、Clarity 或定时自动提交任务。

## 当前可观测与不可观测

可以观察：HTTP 状态、真实 HTML、canonical、语言互链、站内链接、Sitemap、部署差异、本地性能与无障碍。

尚不可观察：Google/Bing 已收录页数、曝光、点击、CTR、查询、平均排名、自然流量带来的 App Store 点击或下载。这些值目前均为 **未知**，不能写成 0。HTTP 200、Sitemap 部署、Lighthouse 100 都不代表已收录。

## 每次发布的检查

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
node --check site.js
python3 scripts/check_live.py --output /tmp/panelune-live-check.json
```

前三步在提交前执行，最后一步在 Pages 部署成功后执行。线上脚本匿名访问 Sitemap 中每个 canonical URL，核对 200、最终 URL、canonical、noindex、与本地生成文件字节一致；检查 Sitemap、根 robots、代表页面的 Googlebot/Bingbot UA 响应及私有源码路径 404。UA 测试只是模拟请求头，不代表搜索引擎真的来抓取。脚本不登录、不提交 URL、不改网站。

若失败，先看错误与 Pages 发布 SHA，区分 CDN 缓存和真实错误，不自动重试大量索引提交。根 robots 变化须单独阅读规则，确认没有阻挡 `/panelune-site/`。保留 JSON 回执作为该次 HTTP 检查证据。

需要布局验收时复用临时开发工具，不在网站添加依赖：

```sh
NODE_PATH=/path/to/dev/node_modules SITE_URL=http://127.0.0.1:8766/panelune-site/ node tests/browser.cjs
NODE_PATH=/path/to/dev/node_modules SITE_URL=http://127.0.0.1:8766/panelune-site/ node tests/guides-browser.cjs
```

本地服务器应将网站挂载在真实子路径 `/panelune-site/`。Lighthouse 使用固定移动端参数与相同环境对比；单次实验室结果不能替代真实用户 Core Web Vitals。

## 7 / 30 / 90 天安排

若部署日期变化，相应顺延；以下以 2026-11-22 为第 0 天。

| 时间 | 操作 | 应保留的证据 | 如何处理 |
|---|---|---|---|
| 7 天：2026-11-29 | 完成 Google/Bing 验证与 Sitemap 提交；URL Inspection 抽查首页及 10 篇指南；运行线上检查 | 所有权状态、Sitemap 读取结果、检查日期、被选择的 canonical、抓取与索引原因 | 未发现 URL 则核对内部链接和 Sitemap；阻止抓取则修真实规则；尚未索引先记录状态，不改发布承诺 |
| 30 天：2026-12-22 | 导出 Google Performance 和 Pages；查看 Bing Search Performance/Site Explorer；按语言页面、国家、设备分组 | 查询、页面、曝光、点击、CTR、平均排名、索引状态；各平台分开 | 有曝光但匹配差：改对应标题或段落；有相关查询但回答不足：补现有指南；不能因为没数据就堆关键词 |
| 90 天：2027-02-20 | 比较相同长度窗口，评估指南和首页的不同作用；复查格式与发布版本 | 最近 28 天与此前 28 天的导出、内容修改日期、实际支持反馈 | 证据支持再新增主题；iPhone 实际上架后独立更新发布状态与相应指南；不以平均排名单一值判断成功 |

## 记录表模板

每次导出另存本地文件或获授权的内部位置；不要将包含敏感查询的原始账户导出自动提交到公共仓库。

| 检查日 | 平台 | 时间窗口 | 页面／语言 | 国家 | 设备 | 索引状态／原因 | 曝光 | 点击 | CTR | 平均排名 | 来源文件 | 下一步 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-22 | Google | 尚无数据 | 全站 | 未知 | 未知 | 未知 | 未知 | 未知 | 未知 | 未知 | 尚未接入 | 用户验证属性 |
| 2026-11-22 | Bing | 尚无数据 | 全站 | 未知 | 未知 | 未知 | 未知 | 未知 | 未知 | 未知 | 尚未接入 | 用户验证属性 |

CTR 按同一窗口的总点击／总曝光计算，不直接平均不同页面的 CTR。平均排名来自平台报告，不能从公开抽样结果猜测。Search Console 可能隐藏低量查询，因此查询行总和不一定等于总数；报告保留平台口径与时间窗口。

## 触发修复的条件

- 关键页面从 200 变为 4xx/5xx，或出现 noindex、错误 canonical：优先修技术问题。
- hreflang 指向错误主题、语言互链缺失、Sitemap URL 无效：阻止发布并修生成器。
- 索引报告中的重复页／Google 另选 canonical：比较实际内容与 URL，按证据处理，不强行删除译文。
- 同一个相关问题反复出现在查询或支持反馈中：扩展对应指南；不制造多个同义页面互相争夺同一意图。
- App Store 中实际可下载版本变化：按单独发布流程核实后再更新配置；本轮始终保持 coming-soon。

本方案不预测或保证排名。技术通过只是可发现、可理解的前提，搜索展示效果需要真实后台数据和时间验证。

来源：[Search Console 性能报告](https://support.google.com/webmasters/answer/7576553)、[URL Inspection](https://support.google.com/webmasters/answer/9012289)、[Google Sitemap 文档](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)。
