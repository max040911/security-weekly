---
title: 來源｜CISA AA20-352A：SolarWinds 事件警示
type: source
updated: 2026-11-18
---
# 來源｜CISA AA20-352A：SolarWinds 事件警示

- raw：[cisa-aa20-352a](../raw/cisa-aa20-352a.md)
- 原始網址：<https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a>
- 發布者：美國 CISA；初版 2020-12-17，最後修訂 2021-04-15
- 授權：美國政府著作（公有領域）

## 重點摘要

1. APT 攻擊者入侵美國政府機關、關鍵基礎設施與民間組織，最早可追溯到「至少 2020 年 3 月」。
2. 其中一個入侵途徑是 SolarWinds Orion 的**軟體供應鏈入侵**。
3. 攻擊者把惡意版本的 `solarwinds.orion.core.businesslayer.dll` 放進 SolarWinds 的軟體生命週期，**並用 SolarWinds 合法的程式碼簽章憑證簽署**。
4. 安裝後會連到 `avsvmcloud[.]com` 的子網域，通訊格式偽裝成正常 SolarWinds 流量，再依 DNS 回應取得後續指令伺服器。
5. 受影響版本列於附錄，例如 Orion Platform 2019.4 HF5、2020.2、2020.2 HF1；建議重建到至少 2020.2.1 HF2。
6. 2020-12-13 CISA 發布緊急指令 ED 21-01，要求聯邦機關中斷受影響設備。
7. 文件也指出攻擊者還有其他初始入侵途徑（如密碼噴灑），不是所有受害者都經由 Orion。
8. 後門惡意程式被命名為 SUNBURST（見文中 MAR 報告標題）。

## 與其他來源的衝突

無。
