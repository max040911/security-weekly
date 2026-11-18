---
title: SSDF 安全軟體開發框架
type: concept
sources: [nist-ssdf]
updated: 2026-11-18
---
# SSDF 安全軟體開發框架（Secure Software Development Framework）

**一句話定義**：NIST 提出的一組高層次安全開發實務，可以加進任何開發流程，讓發布的軟體漏洞更少。（來源：[NIST SSDF](../sources/nist-ssdf.md)）

**生活比喻**：不是某一道檢查關卡，而是整間工廠的品管制度：從員工訓練、原料保管、生產過程到出貨後的客訴處理都有規範。

## 四組實務

| 代號 | 名稱 | 一句話 |
|---|---|---|
| PO | 準備組織 | 人、流程、技術都準備好做安全開發 |
| PS | 保護軟體 | 所有元件不被竄改或未授權存取 |
| PW | 產出安全的軟體 | 讓發布的版本漏洞最少 |
| RV | 回應漏洞 | 處理發布後的漏洞，並避免再發生 |

（來源：[NIST SSDF](../sources/nist-ssdf.md)）

## 和其他防禦的關係（本 Wiki 歸納）

- [SBOM](sbom.md) 幫助 RV（出事時快速查影響範圍）。
- [SLSA](slsa.md) 與 [可重現建置](reproducible-builds.md) 屬於 PS（保護建置與發布不被竄改）。
