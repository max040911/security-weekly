---
title: 軟體供應鏈安全 LLM Wiki
type: meta
updated: 2026-11-18
---
# 軟體供應鏈安全 LLM Wiki

資安週報的知識庫。週報與[教學簡報](../slides/supply-chain-101.html)的事實都從這裡來，這裡的事實都能追到 `raw/` 原始資料。
規則見 repo 根目錄的 `CLAUDE.md` 第 8 節。

- [操作紀錄 log](log.md)：討論、ingest、lint、生成的完整紀錄
- [流程圖 workflow](workflow.md)：Wiki → 簡報的 loop / graph 設計

## 概念

| 頁面 | 一句話 |
|---|---|
| [軟體供應鏈攻擊](concepts/supply-chain-attack.md) | 污染上游，讓惡意程式跟著正常更新進來 |
| [SBOM](concepts/sbom.md) | 軟體的成分表，出事時查「有沒有用到」 |
| [SLSA](concepts/slsa.md) | 用分級的來源證明，證明成品怎麼建置出來 |
| [可重現建置](concepts/reproducible-builds.md) | 任何人都能驗證二進位檔與原始碼相符 |
| [SSDF](concepts/ssdf.md) | NIST 的安全開發實務，分 PO / PS / PW / RV 四組 |

## 事件

| 頁面 | 年份 | 入口 |
|---|---|---|
| [SolarWinds](events/solarwinds.md) | 2020 | 建置 / 發布流程被入侵 |
| [Log4Shell](events/log4shell.md) | 2021 | 被廣泛依賴的元件有漏洞 |
| [XZ 後門](events/xz-backdoor.md) | 2024 | 維護者身分被滲透 |

## 來源（9 份）

| 來源頁 | 類型 |
|---|---|
| [CISA AA20-352A](sources/cisa-aa20-352a.md) | 政府警示（全文） |
| [NVD 漏洞條目](sources/nvd-cves.md) | 漏洞資料庫（全文） |
| [Apache Log4j 安全公告](sources/apache-log4j-security.md) | 官方公告（全文） |
| [CISA SBOM](sources/cisa-sbom.md) | 政府專頁（全文） |
| [SLSA 等級](sources/slsa-levels.md) | 規範（全文） |
| [NIST SSDF](sources/nist-ssdf.md) | 政府框架（全文） |
| [Reproducible Builds](sources/reproducible-builds.md) | 專案首頁（全文） |
| [XZ 說明頁](sources/tukaani-xz-backdoor.md) | 原維護者說明（來源卡） |
| [xz 揭露郵件](sources/openwall-xz-disclosure.md) | 原始揭露（來源卡） |
