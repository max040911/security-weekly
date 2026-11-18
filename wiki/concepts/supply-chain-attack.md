---
title: 軟體供應鏈攻擊
type: concept
sources: [cisa-aa20-352a, nvd-cves, tukaani-xz-backdoor]
updated: 2026-11-18
---
# 軟體供應鏈攻擊（software supply chain attack）

**一句話定義**：不直接攻擊目標，而是污染目標所信任、所依賴的上游軟體或其發布流程，讓惡意程式跟著正常更新一起進來。（本 Wiki 歸納）

**生活比喻**：餐廳很注意廚房衛生，但沒人檢查供應商送來的醬料。醬料工廠一旦被動手腳，所有用這款醬料的餐廳一起中毒。

## 重點

- 被利用的不是程式漏洞本身，而是**信任**：使用者信任簽章、信任官方發布檔、信任熱門套件。
- SolarWinds 事件中，惡意 DLL 用的是 SolarWinds 合法的程式碼簽章憑證，所以看起來完全正常。（來源：[CISA AA20-352A](../sources/cisa-aa20-352a.md)）
- xz 事件中，惡意程式碼藏在上游 tarball 與偽裝成測試檔的檔案裡。（來源：[NVD](../sources/nvd-cves.md)）
- xz 的惡意 tarball 由取得發布權限的維護者帳號 Jia Tan 製作並簽署。（來源：[XZ 說明頁](../sources/tukaani-xz-backdoor.md)）

## 三種常見入口（本 Wiki 歸納）

| 入口 | 例子 |
|---|---|
| 建置 / 發布流程被入侵 | [SolarWinds](../events/solarwinds.md) |
| 維護者身分被滲透 | [XZ 後門](../events/xz-backdoor.md) |
| 被廣泛依賴的元件本身有漏洞 | [Log4Shell](../events/log4shell.md) |

Log4Shell 嚴格說是漏洞而非蓄意植入，但它展示了「一個被到處依賴的元件出事，下游全部受影響」的同一種結構。

## 相關概念

[SBOM](sbom.md)・[SLSA](slsa.md)・[可重現建置](reproducible-builds.md)・[SSDF](ssdf.md)
