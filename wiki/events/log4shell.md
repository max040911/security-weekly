---
title: Log4Shell
type: event
sources: [nvd-cves, apache-log4j-security]
updated: 2026-11-18
---
# Log4Shell（CVE-2021-44228）

**一句話摘要**：Java 日誌函式庫 Log4j2 會解析日誌內容中的 JNDI lookup，能控制日誌內容的攻擊者可以讓伺服器從 LDAP 伺服器載入並執行任意程式碼。（來源：[NVD](../sources/nvd-cves.md)、[Apache 公告](../sources/apache-log4j-security.md)）

## 時間線

- 2021-12-10：NVD 發布 CVE-2021-44228，CVSS 10.0。（來源：[NVD](../sources/nvd-cves.md)）
- 修補一：2.15.0 起此行為預設關閉。
- 修補二：2.15.0 在部分非預設設定下仍不完整（CVE-2021-45046），2.16.0 起完全移除此功能。
- 2021-12-28：NVD 發布 CVE-2021-44832（需能改設定檔），2.0-beta7 through 2.17.0 受影響，修補於 2.17.1。（來源：[NVD](../sources/nvd-cves.md)）

> ⚠️ **來源衝突**：[Apache 公告](../sources/apache-log4j-security.md) 目前寫 CVE-2021-44832 修補於 2.17.0，與 NVD 不同。本 Wiki 採用 NVD 的 2.17.1，理由見 Apache 來源頁。

## 機制

1. 程式把使用者輸入寫進日誌，例如登入失敗的帳號名稱。
2. 受影響的 Log4j2（2.0-beta9 起）會解析其中的 JNDI lookup。
3. JNDI 連到攻擊者控制的 LDAP 伺服器，載入並執行任意程式碼。

（來源：[NVD](../sources/nvd-cves.md)、[Apache 公告](../sources/apache-log4j-security.md)）

## 防禦

- Java 8 以上升級到 2.17.1 以上，可涵蓋本頁列出的所有相關 CVE。（來源：[NVD](../sources/nvd-cves.md)）

## 相關概念

[軟體供應鏈攻擊](../concepts/supply-chain-attack.md)・[SBOM](../concepts/sbom.md)
