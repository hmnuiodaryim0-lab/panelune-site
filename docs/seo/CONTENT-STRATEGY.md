# 内容策略与已实施页面

日期：2026-11-22。目标是回答已有书籍如何加入和管理，而不是增加重复的产品宣传页。

## 本轮选择

1. **本地书籍导入**：给出 Wi-Fi Transfer 与 Files Link Folder 两条 1.1.1 可用路径，解释存储区别、完整 EPUB、CBZ/ZIP 与 CBR 边界，补充连接、格式、空间、系列上限排查及离线准备。
2. **漫画书库管理**：解释 Series/Volumes，提供编辑、移动、合并、Continue Reading 和 Private Library 操作，区分关联条目与已导入副本的删除后果。

每篇有实际步骤、问题排查或边界说明，而非重复首页。首页提供两篇指南卡片；指南有页内目录、同主题五语言导航、另一篇指南与英文 Support/Privacy 链接。没有只列关键词的中转页。

## 为什么暂缓 EPUB 高级阅读指南

已发布 App 基线为 `Panelary` 提交 `685569e`（1.1.1 pre-iPhone）。当前工作目录含待发布的 EPUB、字体与阅读位置实现。为避免把 1.2.0 的控件写成旧版操作，不发布依赖这些控件的第三篇指南；导入 EPUB 的实际流程已包含在第一篇。正式上架后应核实实际版本和操作，再独立撰写字体、目录、恢复位置及漫画／小说模式差异，不以竞争产品行为代替证据。

## 生成与维护

- 内容：`content/guides/{en,zh-Hans,zh-Hant,ja,ko}.json`。
- 生成：`scripts/build.py`；共两组、每组五种完整语言版本。
- 英文路径：`guides/import-books/`、`guides/organize-library/`。
- 其他语言：`{locale}/guides/{slug}/`。
- 修改 JSON 后运行构建与完整测试。生成 HTML 入库，不手工同步十份 HTML。
- 每页独立 canonical；hreflang 指向同主题译文并互相回链，x-default 指英文同主题。未给仅英文的隐私／支持页伪造译文。
- 使用 `WebPage` 与 `BreadcrumbList`，不添加 FAQ 富结果、评分、下载量或未经证实的作者权威信号。
- 全部内容是静态 HTML；指南不加载 JS、远程字体、图片或第三方脚本。

## 事实核对与版本保护

只读核对 App 基线：

| 事实 | 1.1.1 证据（均为 `git show 685569e:<path>`） |
|---|---|
| Files 使用文件夹入口，支持漫画／小说、重新扫描和重新连接 | `Panelary/Views/LibraryRootView.swift` 的 LinkFolderView，约 286—378 行 |
| Wi-Fi 本地地址、保持前台、传输状态、开始与停止 | `Panelary/Views/WiFiTransferView.swift`；`Panelary/Services/WiFiTransferServer.swift` 的上传页 |
| 系列／单卷编辑、移动、合并与已读标记 | `Panelary/Views/LibraryManagementViews.swift`、`LibraryBatchViews.swift` |
| Continue Reading | `Panelary/Views/LibraryRootView.swift`、`SeriesDetailView.swift` |
| 私密入口与设备认证 | `Panelary/Views/SettingsView.swift`、`Panelary/Services/PrivateLibrarySecurity.swift` |
| 关联原文件 vs 导入副本、删除确认 | `Panelary/Services/LibraryStore.swift`、`Panelary/Views/LibraryManagementViews.swift` |
| 免费 3 系列、一次购买 Pro | `Panelary/Services/LibraryRules.swift`、`ProStore.swift` |
| ZIP 实现，不夸大 RAR CBR 支持 | `Panelary/Services/ComicArchive.swift` |
| 日／韩／中文真实菜单名 | `Panelary/Resources/Localizable.xcstrings` |

本轮没有运行 App、修改 App 工程或重新做设备实机验收。操作说明依据已发布版本的源码基线；若商店包与该基线存在差异，应依据实机反馈修订。不是从待发布界面截图推断旧版步骤。

`content/site.json` 保持原样，`iphoneReleaseStatus=coming-soon`；软件 JSON-LD 保留 iPadOS、iPad、1.1.1。每篇指南明确 1.1.1 适用范围与当前 iPhone 预告。现有首页和 Support 的泛泛“Files import”已改为明确的文件夹入口。

## 以后如何增补

7—30 天先检查页面是否可抓取、用户是否找到操作入口。收到 Search Console 查询或真实支持问题后，改进现有段落。90 天再决定是否需要第三个主题。只有独立需求、足够真实步骤、能维护的完整语言内容才新增页面；不按关键词排列组合批量建页。App Store 跳转已有真实链接，本轮不加追踪参数或统计服务，无法据此计算下载转化。
