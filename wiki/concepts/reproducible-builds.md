---
title: 可重現建置
type: concept
sources: [reproducible-builds, tukaani-xz-backdoor]
updated: 2026-11-18
---
# 可重現建置（reproducible builds）

**一句話定義**：讓「原始碼 → 二進位檔」這條路可以被任何人獨立驗證：同樣的原始碼，誰來建置都得到一模一樣的結果。（來源：[Reproducible Builds](../sources/reproducible-builds.md)）

**生活比喻**：照著公開食譜做蛋糕，做出來跟店家賣的一模一樣，就能確定店家沒偷加東西。

## 重點

- 目的：確認軟體是真的、沒有被竄改；讓第三方能驗證。（來源：[Reproducible Builds](../sources/reproducible-builds.md)）
- 驗證方式：比對下載到的二進位檔是否與原始碼建出來的相符。（來源：[Reproducible Builds](../sources/reproducible-builds.md)）

## 限制：要驗證的「原始碼」本身也要可信

- xz 事件中，觸發後門的程式碼從未進入 Git repository，只出現在發布的 tarball。（來源：[XZ 說明頁](../sources/tukaani-xz-backdoor.md)）
- 也就是說，如果大家拿 tarball 當「原始碼」來重現建置，結果會完全一致，卻一樣含有後門。還必須比對「發布檔」與「Git 原始碼」是否一致。（應用推論：本 Wiki 歸納）

## 相關概念

[SLSA](slsa.md)・[軟體供應鏈攻擊](supply-chain-attack.md)
