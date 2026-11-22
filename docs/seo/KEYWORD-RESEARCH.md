# 关键词与搜索意图研究

研究日期：2026-11-22（Asia/Shanghai）。公开网页搜索的定性样本，不是指定地区的 Google/Bing 排名监控，也不是付费关键词数据库。未读取任何个人搜索账户。

所有词的**搜索量未知**；没有 Keyword Difficulty、Panelune 排名、预计流量或转化率数据。优先级只由真实功能、当前发布状态、意图清晰度与内容可回答程度决定。竞品声称的格式、同步、AI 功能不代表 Panelune 支持。

## 方法与查询记录

agent-reach 的 Exa 后端两次返回网络握手失败，转用可用的公开网页搜索。实际查询包括：

- `offline manga reader cbz ipad local library`
- `iPad 自炊 漫画 ビューア CBZ EPUB 読み込み`
- `아이패드 만화책 뷰어 cbz epub 파일 가져오기`
- `iPad 漫畫 閱讀器 匯入 CBZ 離線`
- `iPad 本地漫画 阅读器 CBZ 导入 EPUB 小说`
- `manga reader iphone epub reader custom fonts one time purchase comic reader`
- `"manga reader iphone" "offline"`、`"epub reader" "custom fonts" iPhone`
- `"아이패드" "만화책 뷰어"`、`"private manga library"`
- `"manga library organizer" "iPad"`、`"one time purchase" "comic reader" ipad`
- `"cbz reader ipad"`、`"epub reader iphone"`
- `site:hmnuiodaryim0-lab.github.io/panelune-site Panelune`

不是每个候选词都逐字独立搜索：下表同语义词组由上述查询样本与原语言产品页面归纳。未观测到明确结果的精确短语标为待验证，不把语义推导写成真实查询量。站点查询没有返回可确认的 Panelune 官网结果；这不能证明未收录，更不能统计收录数量。

## 目标页

- H：对应语言首页，英文 `/`，其余 `/{locale}/`。
- I：`/{locale}/guides/import-books/`（英文去掉 `{locale}/`）。
- L：`/{locale}/guides/organize-library/`。
- S：英文 `/support.html#pro` 或 `#formats`。
- P1：本轮优先解决；P2：相关但作为辅助表达；暂缓：与未发布功能有关或意图歧义大。

## 英语市场

| 关键词 | 搜索意图 | Panelune 相关性与边界 | 竞争页面类型／样本 | 页面 | 优先级 | 搜索量 |
|---|---|---|---|---|---|---|
| manga reader iphone | 寻找可在 iPhone 使用的漫画 App，常混合在线书源需求 | iPhone 尚未发布，不能承诺立即可用 | App Store、阅读器官网；E1/E2 | H（仅预告） | 暂缓 | 未知 |
| offline manga reader | 在无网络时读漫画 | 适合已有本地副本；不提供漫画下载 | App Store 本地阅读器；E1 | H、I | P1 | 未知 |
| epub reader iphone | 寻找手机 EPUB 阅读器 | EPUB 相关，iPhone 设备条件尚不满足 | 产品官网、商店与比较页；E3 | H（仅预告） | 暂缓 | 未知 |
| cbz reader ipad | 用 iPad 打开已有 CBZ 漫画 | 对应现有 iPad 与 ZIP 图片档案读取 | App Store、格式教程；E4 | I、H | P1 | 未知 |
| local comic reader | 管理并阅读自己的文件 | 高相关；不同于在线内容服务 | App Store 本地文件阅读器；E2 | H、I | P1 | 未知 |
| private manga library | 保护私人收藏／也可能寻找实体漫画藏书 | 有 Private Library，但精确词意图分散 | 个人藏书文章、实体图书馆；E5 | L | 暂缓为独立目标 | 未知 |
| manga library organizer | 整理系列、卷和阅读进度 | 相关；精确短语的 App 意图仍需真实查询验证 | 检索样本稀疏；相邻词为阅读器、书库软件 | L | P2 | 未知 |
| epub reader custom fonts | 导入自定义字体或细调小说排版 | 1.2.0 字体改进尚未发布；不以旧版支持代替验证 | 开发者官网与商店；E3 | 暂不建页 | 暂缓 | 未知 |
| one time purchase comic reader | 比较买断与订阅 | Pro 一次购买解除系列上限，价格以当地 App 内为准 | 商店、阅读器比较页；E6 | L、S | P2 | 未知 |
| import cbz to ipad / transfer epub to ipad | 解决已有书籍如何加入 iPad 的问题 | 可具体解释 Wi-Fi 和链接文件夹 | 从本地阅读器样本归纳的操作型长尾；E1/E2 | I | P1，精确词待验证 | 未知 |

## 日本

| 关键词 | 搜索意图 | 功能相关性 | 竞争页面类型／样本 | 页面 | 优先级 | 搜索量 |
|---|---|---|---|---|---|---|
| iPad 自炊 漫画 ビューア | 阅读自有扫描漫画，而非寻找漫画平台 | 高；限定有使用权的本地书籍 | 日语阅读器官网、商店；J1/J2 | H、I | P1 | 未知 |
| CBZ 漫画リーダー | 打开漫画压缩档案 | 高；不扩展到 RAR CBR | 格式命名 App 商店页；J3 | I | P1 | 未知 |
| EPUB 小説 読み込み | 将已有小说文件加入阅读器 | 高；具体操作优先，不承诺竖排、注音等未核实功能 | 漫画／EPUB 综合阅读器；J2 | I | P1 | 未知 |
| 漫画 シリーズ 整理 | 整理系列与卷 | 高；语义长尾，精确需求待 Search Console 验证 | 产品功能说明；J1/J2 | L | P2 | 未知 |
| 漫画 ビューア 買い切り | 寻找不订阅的阅读器 | Pro 一次购买相关，不与竞品价格比较 | 开发者定价与商店页；J1 | L、S | P2 | 未知 |

日本文案使用“手持ちの本”“自炊漫画”“フォルダを連携”，不把英文 private library 机械译成主关键词。App 的实际日语菜单与 1.1.1 字符串目录交叉核对。

## 韩国

| 关键词 | 搜索意图 | 功能相关性 | 竞争页面类型／样本 | 页面 | 优先级 | 搜索量 |
|---|---|---|---|---|---|---|
| 아이패드 만화책 뷰어 | 选择 iPad 漫画文件阅读器 | 高；不是 웹툰 内容订阅平台 | 韩文 App Store、应用比较文章；K1/K2 | H | P1 | 未知 |
| CBZ 파일 가져오기 | 导入已有压缩漫画 | 高；提供文件与网络两条实际路径 | 文件型阅读器说明；K1 | I | P1 | 未知 |
| EPUB 소설 파일 | 打开已有 EPUB 小说 | 高；归纳型词组，精确需求待验证 | 多格式阅读器产品说明；K1 | I | P2 | 未知 |
| 만화책 보관함 정리 | 整理收藏与接续阅读 | 高；本地系列／卷 | 书架与系列功能说明；K1 | L | P2 | 未知 |
| 만화 뷰어 한 번 결제 | 买断付费偏好 | Pro 一次购买相关 | 商店内付费功能说明；K1 | L、S | P2 | 未知 |

韩国主文案使用“만화책 뷰어”“파일 가져오기”“이어 읽기”。不用宽泛的“무료 웹툰”吸引不匹配的在线内容流量。

## 繁體中文

| 關鍵詞 | 搜尋意圖 | 功能相關性 | 競爭頁面類型／樣本 | 頁面 | 優先級 | 搜尋量 |
|---|---|---|---|---|---|---|
| iPad 漫畫閱讀器 | 選擇閱讀自己的漫畫檔案的 App | 高；需說明自備書籍 | 台灣 App Store；T1 | H | P1 | 未知 |
| CBZ 匯入 iPad | 操作與格式問題 | 高；不誇大 CBR 相容性 | 本機檔案閱讀器說明；T1 | I | P1 | 未知 |
| 本機漫畫 離線閱讀 | 無網路閱讀收藏 | 高；區分本機副本與雲端來源 | 商店產品文案；T1 | H、I | P1 | 未知 |
| EPUB 小說 匯入 | 把自己的小說加入書庫 | 高；不承諾未核實的進階排版 | 多格式小說閱讀器；T2 | I | P2 | 未知 |
| 漫畫書庫 整理 | 系列分類與找書 | 高；精確詞組由功能語境歸納 | 本機閱讀器書庫說明；T1/T2 | L | P2 | 未知 |

使用“檔案、匯入、連結資料夾、本機、儲存”，並保留實際 App 選單用語；不直接套用簡中“文件、導入”。市場是繁體使用者，並非宣稱已做台港兩地獨立排名研究。

## 简体中文

| 关键词 | 搜索意图 | 功能相关性 | 竞争页面类型／样本 | 页面 | 优先级 | 搜索量 |
|---|---|---|---|---|---|---|
| iPad 本地漫画阅读器 | 选择阅读自有文件的 App | 高 | 中文商店、本地阅读器官网；C1/C2 | H | P1 | 未知 |
| CBZ 漫画 导入 | 文件怎么加入书库 | 高；具体路径可验证 | 多格式阅读器说明；C1 | I | P1 | 未知 |
| EPUB 小说 导入 iPad | 导入已有小说 | 高；保留完整 EPUB | 小说／漫画综合阅读器；C3 | I | P1 | 未知 |
| Wi-Fi 传书 iPad | 电脑向设备传文件 | 高；同一局域网，无云同步 | 阅读器导入说明；C2 | I | P1 | 未知 |
| 漫画书库 系列 整理 | 修正分组与卷号 | 高；语义长尾，待真实查询验证 | 阅读器书架功能页；C1/C2 | L | P2 | 未知 |

简中页面主要服务使用这些表达的用户；不据此宣称 github.io 在中国大陆网络中稳定可达，也不把 Google/Bing 策略等同于完整的中国大陆搜索策略。本轮没有获得大陆多运营商可用性或其他搜索引擎后台数据。

## 来源（均于 2026-11-22 检索）

以下为搜索实际返回的页面样本；这里只提炼页面类型、语言与意图，不复制竞品的宣传内容。

- E1：[Longbox — Apple US](https://apps.apple.com/us/app/longbox-comic-reader/id6794874811?platform=ipad)
- E2：[ComicToons — Apple US](https://apps.apple.com/us/app/comictoons-manga-comic-reader/id6809746021)
- E3：[justRead 开发者官网](https://justread.app/en/)
- E4：[Splash — Apple US](https://apps.apple.com/us/app/splash-smart-comics-reader/id6757821463?platform=ipad)
- E5：[Private Manga Library 个人藏书文章](https://note.com/shimox/n/n28a241d7c6c3?hl=en)
- E6：[ComicReader — Apple](https://apps.apple.com/de/app/comicreader-comic-book-reader/id1597314495?platform=watch)
- J1：[Emaki 开发者官网](https://www.piktoo.com/emaki-ios/)
- J2：[Hiraku — Apple JP](https://apps.apple.com/jp/app/id6805065363)
- J3：[CBZ 漫画リーダー — Apple JP](https://apps.apple.com/jp/app/id6789862403)
- K1：[만화숨 — Apple KR](https://apps.apple.com/kr/app/id6825267435)
- K2：[마나뷰어 — Apple KR](https://apps.apple.com/kr/app/id1544720860)
- T1：[漫閱 — Apple TW](https://apps.apple.com/tw/app/id6753895889)
- T2：[青頁小說閱讀器 — Apple TW](https://apps.apple.com/tw/app/id6767811417)
- C1：[Inkveil — Apple CN](https://apps.apple.com/cn/app/id6767468474)
- C2：[漫阅开发者网站](https://allluckly.cn/apps/manyue/)
- C3：[ReadMe — Apple CN](https://apps.apple.com/cn/app/id1438616606)

## 数据到位后的取舍

在 Search Console 按国家、设备、页面、查询查看实际曝光。优先处理已经有相关曝光但页面回答不充分的查询；出现下载书源、云同步、RAR/DRM 等不匹配意图时澄清边界，不制造对应功能页。iPhone 和自定义字体相关词须等待独立的正式发布核验。
