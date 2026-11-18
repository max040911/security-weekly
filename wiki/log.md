---
title: 操作紀錄
type: meta
updated: 2026-11-18
---
# 操作紀錄（log）

依時間追加，不修改舊紀錄。格式：`## [日期] 操作｜摘要`。

## [2026-11-18] discuss｜先討論、後生成

和使用者討論 Wiki 範圍後，才開始生成。決定：

- **主題**：接續資安週報（第 1 期 XZ、第 2 期 Log4Shell），以「軟體供應鏈安全」為主題，Wiki 作為週報的知識庫。
- **讀者**：完全不熟資安的人，簡報約 15 頁、入門程度。
- **位置**：放在既有的 `security-weekly` repo（`wiki/`、`slides/`），用 GitHub Pages 的 github.io 網址瀏覽。
- **頁面類型**：source / concept / event 三種，加上 index、log、workflow。
- **來源原則**：優先政府機關與官方公告；授權不允許轉載的只存來源卡。

## [2026-11-18] fetch｜取得 9 份來源

- 用腳本把 7 份可轉載的頁面存進 `raw/`；2 份（tukaani、openwall）只存來源卡。
- **錯誤 1**：Python `urllib` 下載 CISA 網頁得到 HTTP 403，一份都沒存到。改用 `curl` 後成功。
- **錯誤 2（來源衝突）**：Apache 安全公告寫 CVE-2021-44228 系列中的 CVE-2021-44832 修補於 2.17.0；NVD 寫 through 2.17.0 受影響、修補於 2.17.1。網頁摘要工具兩次都回報 2.17.0，直到用 curl 取原文、再用 NVD API 對照才確認是**來源本身不一致**，不是摘要錯誤。

## [2026-11-18] ingest｜9 份來源 → 9 個 source 頁、5 個 concept 頁、3 個 event 頁

- 衝突處理：依 CLAUDE.md 第 8 節，在 Apache、NVD 兩個 source 頁都寫明衝突，event 頁 [Log4Shell](events/log4shell.md) 加警示框並說明採用 NVD。
- 推論與事實分開：「三種入口」「SBOM 可對應 Log4Shell」等屬於本 Wiki 歸納，頁面上明確標註。

## [2026-11-18] lint｜N4 Wiki 檢查

- `lint_wiki.py` 第一次執行即 `OK`：20 頁、raw 9 份。
- 因為第一次就通過，另外做**反向測試**：故意在 SolarWinds 頁加入假的版本號 `2020.2.9` 和 `CVE-2020-99999`，lint 正確抓出 2 個「在 raw 原文中找不到」，還原後恢復 `OK`。
- 第一次就通過的原因：N2 交叉核對時，已經先把 Log4j 版本衝突處理掉了。

## [2026-11-18] generate｜N5–N9 第一次產生簡報（workflow v1）

- N5 大綱：16 張，依「封面 → 學習目標 → 先備概念 ×3 → 案例 ×3 → 比較 → 防禦 ×4 → 回到案例 → 小測驗 → 回顧」排列。N6 無缺口。
- N8 第一次執行：**1 個錯誤**。s16 的頁尾依據連結被算成 `['index.md', 'index.md']`。原因是**檢查腳本的 bug**：投影片內文的 Wiki 連結也被當成依據連結。修正為只計算 `<p class="wiki-ref">` 內的連結。
- 人工檢查（N9 前逐張對照 Wiki）：發現 **2 句 Wiki 沒有的敘述**，N8 沒抓到，因為它只檢查數字：
  1. s8「Log4j2 是 Java 世界**最常用**的日誌函式庫」：Wiki 沒有「最常用」的依據 → 改成「Java 的日誌函式庫」。
  2. s9「下游怎麼中招：**發行版打包新版**」：Wiki 沒直接寫 → 改成「取得含後門的發布檔」。
- N8 第二次執行：`OK`。

## [2026-11-18] revise｜workflow v1 → v2：檢查往前移到 N5

- 問題：N7（生成簡報）最常出錯，而且錯的是**不含數字的敘述**，N8 的數字接地檢查抓不到。
- 修改：N5 必須產出 `slides/supply-chain-101.outline.md`，每張投影片**逐字引用** Wiki 原句；`check_slides.py` 新增「引用句必須存在於依據頁」的檢查；CLAUDE.md 第 9 節同步更新。
- 依 v2 從 N5 重跑：大綱 16 段、引用 44 句，N8 `OK`。
- 反向測試：把大綱 s6 的「2020 年 3 月」改成「2019 年 3 月」，N8 正確抓出「引用句不在依據頁中」，還原後 `OK`。

## [2026-11-18] check｜N9 視覺檢查

- 截圖工具在視窗隱藏時逾時，改用 JavaScript 量測每張投影片高度與水平溢出。
- 375×812（手機）、1280×800：沒有橫向捲動，每張都在一個畫面內。
- **1366×680**（筆電扣掉瀏覽器工具列）：s8（Log4Shell，含程式碼區塊）高 687px，**超出 7px** → 回 N7 調整投影片上下留白（56/40px → 44/28px），重測三種尺寸全部通過。

## [2026-11-18] deploy｜N10 部署失敗 → 修正

- push 後 GitHub Pages 建置**失敗**（Build with Jekyll failure），github.io 上的 Wiki 與簡報都是 404。
- 原因：CLAUDE.md 第 8 節「禁止 Liquid 字元」那條規則，文字本身就含有 Liquid 的標籤開頭（左大括號加百分號），Jekyll 把它當成 Liquid 標籤而報錯。lint 只檢查 `wiki/` 內的頁面，沒涵蓋根目錄文件。
- 修正：新增 `_config.yml`，讓 Jekyll 不處理 CLAUDE.md、AGENTS.md、scripts、templates。
- workflow 新增 **N10 部署檢查**：push 後查 GitHub Actions 的 pages build 結果，並實際打開 github.io 網址確認狀態碼 200。
- 寫這筆紀錄時，第一版直接引用了那兩個字元，`lint_wiki.py` 立刻擋下（「含有 Liquid 會吃掉的字元」）。改寫成文字描述後通過，等於同一個錯誤在 N4 被提前攔住。
