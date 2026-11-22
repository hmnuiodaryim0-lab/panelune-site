# Google / Bing 接入准备

核查日期：2026-11-22。状态：**已接入用户提供的真实 Google 验证标签，待部署及用户点击验证；Bing 未配置，未提交 Sitemap，未获得后台数据。** 没有访问 Google/Bing 账户，没有添加 Analytics、Clarity、广告或 Cookie 追踪。

网站属性：`https://hmnuiodaryim0-lab.github.io/panelune-site/`

Sitemap：`https://hmnuiodaryim0-lab.github.io/panelune-site/sitemap.xml`

## Google Search Console：推荐 URL-prefix + HTML tag

本轮用户已提供 Google meta 标签并配置，部署后直接从第 5 步继续；请先确认创建的属性与下列 URL 完全一致。

1. 用户自行登录 [Search Console](https://search.google.com/search-console/)，添加 **URL-prefix** 属性，完整填入上面的网站地址，包括 HTTPS 与 `/panelune-site/`。
2. 选择 HTML tag 验证，复制平台提供的真实 `google-site-verification` 标签。无需提供密码、Cookie 或登录令牌。
3. 将标签的 **content 属性值** 填入 `content/search-verification.json` 的 `google` 字符串。不要把整个标签放入 JSON 值。`bing` 可保持空字符串。
4. 运行 `python3 scripts/build.py`、`python3 -m unittest discover -s tests -v`。提交并普通 push；部署完成后检查首页原始 HTML 的 `<head>` 中出现准确标签。生成器会转义属性值并在页面中保留标签；空值不输出。
5. 回到 Search Console 点击验证。平台确认成功才算完成；部署标签不等于验证成功。后续不要删除标签。
6. 在该属性的 Sitemaps 提交 `sitemap.xml` 或完整 Sitemap 地址，检查平台是否成功读取。依次检查首页及两篇英文指南，并抽查四种其他语言指南；使用 URL Inspection 的实时测试，按需请求编入索引。
7. 保存提交时间、Sitemap 处理状态、URL Inspection 的索引状态与 Google 选择的 canonical。不要反复对同一批 URL 请求索引。

[Google 所有权验证文档](https://support.google.com/webmasters/answer/9008080?hl=en)说明 HTML 标签适用于 URL-prefix，且应位于公开首页的 head。这里可控制项目目录 HTML，不能控制 `github.io` 的 DNS，因此不使用 Domain property 的 DNS 验证。

### 如果选择 HTML 文件

只使用平台为当前属性提供的原始文件名和完整内容。确认验证界面要求的 URL 位于 `/panelune-site/` 内，才将文件放到仓库根目录；保留原样，匿名访问应返回 200。若平台要求域名根目录的文件，这个项目仓库无法发布到那里，应改用 meta 标签。不要自行编造文件名或把 HTML 内容用模板替代。本轮没有生成或上传任何验证文件。

## Bing Webmaster Tools

1. 用户自行进入 [Bing Webmaster Tools](https://www.bing.com/webmasters/)，添加同一完整项目地址。
2. 已完成 Google 验证时，可自行选择从 Search Console 导入。只有用户授权该连接后才进行，且不要把“可以导入”写成“已导入”。
3. 或选择 meta tag 验证，将平台提供的 `msvalidate.01` 标签的 content 值填入同一 JSON 的 `bing` 字段，按上述构建、测试、部署步骤发布，然后在 Bing 中验证。
4. 在 Sitemaps 提交完整 Sitemap URL；用 URL Inspection 检查代表页面、抓取状态与索引问题，保存回执。
5. 如果门户只接受更大范围属性或要求根目录文件，先检查门户提供的 meta 验证是否可用于该项目地址；不假定拥有账户站点根目录或 DNS。无法完成时保留“待用户验证”，不要尝试访问其他账户。

官方依据：[Add and Verify site](https://www2.bing.com/webmasters/help/add-and-verify-site-12184f8b)、[从 Search Console 导入](https://blogs.bing.com/webmaster/2019/9/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools/)。实际门户可用选项以用户自己的界面为准。

## IndexNow 评估

技术上适用 GitHub Pages 静态项目：官方协议允许在子目录放 UTF-8 密钥文件并显式传入 `keyLocation`。项目根下的文件只覆盖 `/panelune-site/` 及其子路径，不能提交其他项目或整个 github.io 域名。

本轮**不实现、不提交**。网站目前仅 17 个 canonical 页面、更新频率低，优先完成站点验证与 Sitemap，避免新增无实际数据支撑的提交机制。Search Console 缺失不是 IndexNow 技术阻碍；这是维护成本与更新频率的选择。

将来需要时：生成协议允许的随机密钥（8—128 字符；可用 32 位十六进制），将仅含该密钥的 UTF-8 文本部署在项目根；匿名核验文件和页面可访问后，POST 到官方端点，使用 `host=hmnuiodaryim0-lab.github.io`、该项目内的 `keyLocation` 和由真实内容差异得到的 `urlList`。只提交实际新增、更新或删除 URL，保存真实响应码；200 表示收到，202 表示等待密钥验证，均不等于收录或排名。不要把 IndexNow 当成 Google 所有权验证或 Google 提交接口。

来源：[IndexNow 正式协议](https://www.indexnow.org/documentation)。本轮没有密钥文件、提交请求或伪造成功记录。

## GitHub Pages 边界

- `/panelune-site/robots.txt` 不是根目录机器人协议文件。2026-11-22 匿名请求 `https://hmnuiodaryim0-lab.github.io/robots.txt` 返回 404；当时未见该文件的阻止规则。后续若账户根站点新增规则，应再次核查。
- URL-prefix 可以细分项目范围；无需为本轮强行购买或迁移域名。子路径本身不阻止抓取，但目录拼接、根级 robots、验证文件作用范围必须处理正确。
- 自定义域名是将来品牌稳定性与站点控制权的独立决策；不承诺换域名就提高排名。本轮不更改域名、App Store 地址或其他项目。
