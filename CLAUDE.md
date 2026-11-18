# 資安週報網站 — 專案規則

給 AI（Claude Code、Codex 等）與協作者閱讀。新增或修改任何內容前，先讀完本檔。

## 1. 專案目的

每週一期的**資安週報**靜態網站，讀者是「懂一點程式、但不是資安專業」的大學生。
每期由**一則深講**（由淺入深講透一個事件）加上**幾則短訊**組成。
目標是讓讀者看完一期，能用自己的話說出：發生什麼事、為什麼會發生、我該怎麼防。

## 2. 技術限制

- 純 HTML + CSS，**不使用框架、建置工具或 JavaScript**（目前沒有任何 JS，非必要不要加）。
- 所有頁面共用 `assets/style.css`，**不在 HTML 內寫 `<style>` 或 inline style**。
- 不引用外部字型、CDN 或追蹤碼；網站要能直接用 GitHub Pages 從根目錄發布。
- 所有連結使用相對路徑（期數頁回首頁用 `../index.html`）。

## 3. 檔案結構

```
.
├── CLAUDE.md              # 本檔：專案規則（唯一權威）
├── AGENTS.md              # 指向本檔，給 Codex 等工具
├── README.md              # 給人看的專案介紹
├── index.html             # 首頁：期數列表（新到舊）
├── about.html             # 關於本站與寫作原則
├── assets/style.css       # 全站樣式表（簡報另加 assets/slides.css）
├── templates/issue.html   # 新期數的模板（複製它，不要從零寫）
├── issues/
│   ├── 001-xz-backdoor.html
│   └── 002-log4shell.html
├── wiki/                  # LLM Wiki：週報的知識庫（第 8 節）
│   ├── index.md           # 所有頁面目錄
│   ├── log.md             # 操作紀錄（討論、ingest、lint、查詢）
│   ├── workflow.md        # 知識庫 → 簡報的流程圖與檢查點
│   ├── raw/               # 原始資料，ingest 後不可修改
│   ├── sources/           # 每份原始資料一頁摘要
│   ├── concepts/          # 概念頁
│   └── events/            # 事件頁
├── slides/                # 由 Wiki 產生的教學簡報與大綱（第 9 節）
└── scripts/
    ├── check_site.py      # 週報結構檢查
    ├── lint_wiki.py       # Wiki 檢查
    └── check_slides.py    # 簡報檢查
```

### 命名規則

- 期數檔：`issues/NNN-slug.html`
  - `NNN`：三位數期號，從 `001` 遞增，不跳號、不重用。
  - `slug`：深講主題的英文小寫短名，用 `-` 連接，例如 `xz-backdoor`。
- 圖片（若需要）：`assets/img/NNN-描述.png`，寬度不超過 1600px，必須有 `alt`。

## 4. 一期週報的固定結構

每期頁面**必須**依序包含以下區塊，`id` 不可更改（檢查腳本會驗證）：

| 順序 | 元素 / id | 內容規則 |
|---|---|---|
| 1 | `<header class="issue-header">` | 期號（`第 N 期`）、出刊日期 `<time datetime="YYYY-MM-DD">`、標題、1–3 個標籤 |
| 2 | `#tldr` 本期三句話 | 剛好 3 個 `<li>`，每句不超過 40 字 |
| 3 | `#deep-dive` 深講 | 依序四個 `<h3>`：**先備概念 → 事件經過 → 技術機制 → 防禦與啟示** |
| 4 | `#briefs` 短訊 | 3–5 則 `<article class="brief">`，每則含日期、標題、1–2 句說明、**來源連結** |
| 5 | `#glossary` 名詞小卡 | 3–6 個 `<dl>` 詞條，解釋深講中出現的術語 |
| 6 | `<nav class="issue-nav">` | 上一期 / 回首頁 / 下一期；沒有就用 `<span class="disabled">` |

### 深講寫法（由淺入深）

1. **先備概念**：用生活比喻講清楚讀者需要的背景，不假設讀者懂術語。
2. **事件經過**：時間線，用 `<ol class="timeline">`，每項以 `<time>` 開頭。
3. **技術機制**：講到「為什麼這樣能攻擊成功」。可放程式碼，用 `<pre><code>`；
   惡意 payload 只能示意，**不放可直接利用的完整 exploit**。
4. **防禦與啟示**：分「立即可做」與「長期該想」兩層，用 `<ul>`。

## 5. 內容與寫作規則

- 語言：繁體中文，台灣用語；術語第一次出現時附英文原文，例如「供應鏈攻擊（supply chain attack）」。
- **事實必須可查證**：日期、版本號、CVE 編號要能從來源核對；不確定就不寫，不要編造。
- 短訊每則至少一個來源，優先順序：官方公告 / 原始揭露 > 政府機關（CISA、NVD、TWCERT）> 主流資安媒體。
- 外部連結一律加 `target="_blank" rel="noopener"`。
- 不寫攻擊教學、不針對特定個人、不公開未修補漏洞的利用細節。
- 語氣：清楚、冷靜，不渲染恐慌；避免「史上最強」這類形容。

## 6. 新增一期的標準流程

1. 確認下一個期號 `NNN`（看 `issues/` 中最大的號碼 +1）。
2. 複製 `templates/issue.html` 為 `issues/NNN-slug.html`，替換所有 `{{...}}` 佔位符。
3. 更新**上一期**頁面的 `issue-nav`：把「下一期」由 `disabled` 改成連到新頁。
4. 在 `index.html` 的 `<ol class="issue-list">` **最上方**新增一張卡片（格式照既有卡片）。
5. 執行 `python scripts/check_site.py`，必須顯示 `OK` 才算完成。
6. 用瀏覽器開啟新頁面，確認手機寬度（375px）下沒有橫向捲動。

## 7. AI 修改時的規則

- 修改既有期數時，只改被要求的部分，不順手重寫其他段落。
- 新增樣式前，先確認 `style.css` 中沒有可重用的 class；新 class 加在對應區段並寫註解。
- 顏色只使用 `:root` 中定義的 CSS 變數，不寫死色碼；深色模式須同步處理。
- 不刪除既有期數；內容有誤時在該期加 `<p class="erratum">` 更正說明。
- 結構規則（第 4 節）若需要改，先更新本檔與 `scripts/check_site.py`，再改頁面，三者保持一致。

## 8. LLM Wiki（`wiki/`）

Wiki 是週報與簡報的**唯一知識來源**：週報與簡報裡的事實，都要先存在於 Wiki；Wiki 裡的事實，都要能追到 `raw/`。
三層結構：`raw/`（原始資料，人或腳本放入，AI 不改）→ Wiki 頁面（AI 維護）→ 本節規則（schema）。

### 頁面類型與格式

每個 Wiki 頁面開頭都有 YAML front matter（GitHub Pages 會用它產生標題）：

```yaml
---
title: 頁面標題
type: source | concept | event | meta
sources: [raw 檔名或 source 頁 slug, ...]   # meta 頁可省略
updated: YYYY-MM-DD
---
```

| 類型 | 位置 | 必要內容 |
|---|---|---|
| source | `sources/<slug>.md` | `raw:` 連結到 `../raw/<slug>.md`、原始網址、授權、**重點摘要**（5–10 點）、與其他來源的衝突 |
| concept | `concepts/<slug>.md` | 一句話定義、生活比喻、重點、和哪些事件有關、來源 |
| event | `events/<slug>.md` | 一句話摘要、時間線、機制、受影響範圍、相關概念、來源 |
| meta | `index.md`、`log.md`、`workflow.md` | — |

- 頁面之間用**相對路徑的標準 Markdown 連結**（`[SBOM](../concepts/sbom.md)`），不用 `[[wikilink]]`，GitHub Pages 才會轉成可點的 `.html`。
- concept / event 頁的每個事實段落後面標來源：`（來源：[NVD](../sources/nvd-cves.md)）`。
- `raw/` 只放授權允許轉載的全文（公有領域、CC、Apache 等）；其他來源只放「來源卡」：網址、作者、日期、少於 15 字的短引述。
- 內文不可出現 `{{` 或 `{%`（GitHub Pages 的 Liquid 會吃掉）。

### 三種操作

1. **Ingest**（新增來源）：放入 `raw/` → 寫 `sources/<slug>.md` → 更新受影響的 concept / event 頁 → 更新 `index.md` → 在 `log.md` 追加一筆。
2. **Query**（查詢）：先讀 `index.md` 找頁面，再讀頁面回答；好的答案可以寫回成新頁。
3. **Lint**（檢查）：`python scripts/lint_wiki.py`，必須顯示 `OK`。

### 來源衝突

兩個來源說法不同時，**不可以挑一個默默採用**：在兩邊的 source 頁「衝突」段落都寫明，並在 concept / event 頁註明採用哪個、為什麼。

## 9. 教學簡報（`slides/`）

- 檔名 `slides/<slug>.html`，單一 HTML 檔，樣式寫在 `assets/slides.css`。**不用 JavaScript**：用 CSS scroll-snap 換頁，小測驗答案用 `<details>`。
- 每張投影片是 `<section class="slide" data-wiki="concepts/sbom.md events/xz-backdoor.md">`，`data-wiki` 列出這頁依據的 Wiki 頁（相對於 `wiki/`），頁尾顯示可點的依據連結。
- **簡報不可出現 Wiki 沒有的事實**：CVE 編號、版本號、CVSS 分數、日期，都必須能在 `data-wiki` 指到的頁面中找到原文。
- 教學結構固定：封面 → 學習目標 → 先備概念 → 案例 → 比較 → 防禦方法 → 回到案例 → 小測驗 → 重點回顧。張數 12–18。
- **先寫大綱再寫簡報**：`slides/<slug>.outline.md`，每張投影片一段 `## sN`，列出 `- 依據：` 與逐字引用的 Wiki 原句（`> ` 開頭）。投影片只能改寫大綱引用的內容；需要新事實時，先補進 Wiki，再更新大綱。
- 完成後執行 `python scripts/check_slides.py`，必須 `OK`；再用 375px 寬度目視檢查。

### 產生簡報的流程

依 `wiki/workflow.md` 的流程圖執行：每個節點的檢查失敗，就回到圖上標示的節點重做，不跳過。
