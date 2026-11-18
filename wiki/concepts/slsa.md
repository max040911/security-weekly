---
title: SLSA 與來源證明
type: concept
sources: [slsa-levels, cisa-aa20-352a]
updated: 2026-11-18
---
# SLSA 與來源證明（provenance）

**一句話定義**：SLSA 是一套分級框架，用「來源證明」說明一個軟體成品是在哪裡、用什麼方式建置出來的，等級越高越難偽造或竄改。（來源：[SLSA](../sources/slsa-levels.md)）

**生活比喻**：產銷履歷。L1 是農夫自己手寫的履歷；L2 是由公正的檢驗所出具並蓋章；L3 是檢驗所本身也有嚴格門禁，連內部人員都很難動手腳。

## Build 等級

| 等級 | 名稱 | 要求 | 防什麼 |
|---|---|---|---|
| L0 | No guarantees | 無 | — |
| L1 | Provenance exists | 有來源證明 | 發布流程的失誤（但容易偽造） |
| L2 | Hosted build platform | 託管平台產生有簽章的來源證明 | 建置**完成後**的竄改 |
| L3 | Hardened builds | 強化過的建置平台 | 建置**過程中**的竄改，含內部人員、被盜憑證 |

（來源：[SLSA](../sources/slsa-levels.md)）

## 對應事件

- [SolarWinds](../events/solarwinds.md) 的惡意程式在 SolarWinds 的軟體生命週期中被加入，再經合法憑證簽章（來源：[CISA AA20-352A](../sources/cisa-aa20-352a.md)）。這正是 L3「建置過程中被竄改」要防的情境；只有簽章不夠，還要能證明建置過程本身可信。（應用推論：本 Wiki 歸納）

## 相關概念

[可重現建置](reproducible-builds.md)・[軟體供應鏈攻擊](supply-chain-attack.md)
