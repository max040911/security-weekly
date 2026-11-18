---
title: SolarWinds Orion 供應鏈入侵
type: event
sources: [cisa-aa20-352a]
updated: 2026-11-18
---
# SolarWinds Orion 供應鏈入侵（2020）

**一句話摘要**：攻擊者把後門放進 SolarWinds Orion 的正式更新，並用 SolarWinds 自己的合法憑證簽章，讓客戶以為是正常更新而安裝。（來源：[CISA AA20-352A](../sources/cisa-aa20-352a.md)）

## 時間線

- 至少 2020 年 3 月：入侵活動開始。
- 2020-12-13：CISA 發布緊急指令 ED 21-01，要求聯邦機關中斷受影響設備。
- 2020-12-17：CISA 發布警示 AA20-352A（之後多次修訂）。

（來源：[CISA AA20-352A](../sources/cisa-aa20-352a.md)）

## 機制

1. 惡意版本的 `solarwinds.orion.core.businesslayer.dll` 被放進 SolarWinds 的軟體生命週期。
2. 這個檔案由 SolarWinds 合法的程式碼簽章憑證簽署。
3. 安裝後連到 `avsvmcloud[.]com` 的子網域，流量偽裝成正常的 SolarWinds 通訊。
4. 攻擊者用 DNS 回應挑選目標，再送出新的指令伺服器位址。

（來源：[CISA AA20-352A](../sources/cisa-aa20-352a.md)）

## 受影響範圍

- 受影響版本包含 Orion Platform 2019.4 HF5 到 2020.2 HF1 之間的數個版本；建議重建到至少 2020.2.1 HF2。（來源：[CISA AA20-352A](../sources/cisa-aa20-352a.md)）
- 後門被稱為 SUNBURST。

## 相關概念

[軟體供應鏈攻擊](../concepts/supply-chain-attack.md)・[SLSA](../concepts/slsa.md)
