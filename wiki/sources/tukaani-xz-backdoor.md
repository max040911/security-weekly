---
title: 來源｜XZ 原維護者說明頁（來源卡）
type: source
updated: 2026-11-18
---
# 來源｜XZ 原維護者說明頁（來源卡）

- raw：[tukaani-xz-backdoor](../raw/tukaani-xz-backdoor.md)（來源卡，未轉載全文）
- 原始網址：<https://tukaani.org/xz-backdoor/>
- 作者：Lasse Collin

## 重點摘要

1. 5.6.0 與 5.6.1 的發布 tarball 含有後門，由 Jia Tan 製作並簽署。
2. Jia Tan 能控制的只有 GitHub 上的項目（含 xz.tukaani.org 子網域）。
3. 2024-04-09 Git repository 在 GitHub 上恢復；2024-05-29 發布乾淨的新版本。
4. 惡意檔案仍在 Git 歷史中，但沒有觸發碼就無害，而觸發碼從未進入 Git repository。

## 與其他來源的衝突

- [NVD](nvd-cves.md) 只寫「從 5.6.0 開始」，本來源明確列出 5.6.0 與 5.6.1，兩者不矛盾。
