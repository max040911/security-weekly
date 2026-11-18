---
title: SBOM 軟體物料清單
type: concept
sources: [cisa-sbom, nvd-cves]
updated: 2026-11-18
---
# SBOM 軟體物料清單（Software Bill of Materials）

**一句話定義**：一份巢狀的清單，列出組成軟體的所有元件，就像食品包裝上的成分表。（來源：[CISA SBOM](../sources/cisa-sbom.md)）

**生活比喻**：食品有成分表，過敏的人一看就知道能不能吃。SBOM 讓你一看就知道「我的系統裡有沒有某個出事的元件」。

## 重點

- CISA 把 SBOM 視為軟體安全與供應鏈風險管理的關鍵基礎。（來源：[CISA SBOM](../sources/cisa-sbom.md)）
- 搭配 **VEX** 使用：VEX 說明某產品是否真的受某個已知漏洞影響，避免「有用到元件」就一律當成「有漏洞」。（來源：[CISA SBOM](../sources/cisa-sbom.md)）

## 對應事件

- [Log4Shell](../events/log4shell.md)：CVE-2021-44228 公開後，大家最先要回答的是「我們有沒有用到 Log4j？」（漏洞資訊見 [NVD](../sources/nvd-cves.md)）。有 SBOM 的組織可以直接查清單。（應用推論：本 Wiki 歸納）

## 相關概念

[軟體供應鏈攻擊](supply-chain-attack.md)・[SSDF](ssdf.md)
