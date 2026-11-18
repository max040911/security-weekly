---
title: 來源｜Apache Log4j 官方安全公告
type: source
updated: 2026-11-18
---
# 來源｜Apache Log4j 官方安全公告

- raw：[apache-log4j-security](../raw/apache-log4j-security.md)
- 原始網址：<https://logging.apache.org/log4j/2.x/security.html>
- 發布者：Apache Logging Services
- 授權：Apache License 2.0

## 重點摘要

1. CVE-2021-44228（Log4Shell）：CVSS 10.0。能控制日誌訊息或參數的攻擊者，可以執行從 LDAP 伺服器載入的任意程式碼。
2. CVE-2021-44228 修補版本：2.3.1（Java 6）、2.12.2（Java 7）、2.15.0（Java 8 以上）。
3. CVE-2021-45046：CVSS 9.0。2.15.0 的修補在某些非預設設定下不完整；Java 8 以上修補版為 2.16.0。
4. CVE-2021-45105：CVSS 5.9，自我參照的 lookup 造成無限遞迴、阻斷服務；Java 8 以上修補版為 2.17.0。
5. CVE-2021-44832：CVSS 6.6，需要能寫入日誌設定檔的攻擊者，透過 JDBC Appender 的 JNDI 資料來源執行程式碼。

## 與其他來源的衝突

- **CVE-2021-44832 的修補版本**：本頁寫受影響範圍到 `2.17.0)`（不含 2.17.0）、修補版為 **2.17.0**；
  [NVD](nvd-cves.md) 寫 2.0-beta7 **through 2.17.0** 受影響、修補於 **2.17.1**。
  兩者不一致。本 Wiki 採用 NVD 的說法（2.17.1），理由：NVD 條目發布於 2021-12-28，內容與當時的修補版本一致；本頁是之後整理的彙總頁，區間寫法較可能是整理時的錯誤。發現於 2026-11-18 ingest。
