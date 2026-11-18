---
title: 來源｜SLSA v1.0 安全等級
type: source
updated: 2026-11-18
---
# 來源｜SLSA v1.0 安全等級

- raw：[slsa-levels](../raw/slsa-levels.md)
- 原始網址：<https://slsa.dev/spec/v1.0/levels>
- 發布者：SLSA 專案（OpenSSF）
- 授權：CC BY 4.0

## 重點摘要

1. SLSA 的 Build 軌道分四級：L0 到 L3。
2. Build L0「No guarantees」：沒有任何要求。
3. Build L1「Provenance exists」：有一份**來源證明（provenance）**說明成品是怎麼建置出來的；可防止發布流程的失誤，但容易被繞過或偽造。
4. Build L2「Hosted build platform」：由託管的建置平台產生**有簽章的**來源證明；可防止建置完成後的竄改。
5. Build L3「Hardened builds」：在強化過的建置平台上建置；可防止**建置過程中**的竄改，包括內部人員與被盜憑證。

## 與其他來源的衝突

無。
