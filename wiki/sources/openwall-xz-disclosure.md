---
title: 來源｜xz 後門原始揭露郵件（來源卡）
type: source
updated: 2026-11-18
---
# 來源｜xz 後門原始揭露郵件（來源卡）

- raw：[openwall-xz-disclosure](../raw/openwall-xz-disclosure.md)（來源卡，未轉載全文）
- 原始網址：<https://www.openwall.com/lists/oss-security/2024/03/29/4>
- 作者：Andres Freund，2024-03-29

## 重點摘要

1. 發現契機：在 Debian sid 上注意到 ssh 登入很吃 CPU，以及 valgrind 錯誤。
2. 量測：被拒絕的 ssh 登入約 0.30 秒 → 有後門時約 0.81 秒。
3. 受影響的上游版本：5.6.0 與 5.6.1。
4. 能碰到 sshd 是因為多個發行版替 OpenSSH 加上 systemd 通知支援，因而連結到 liblzma。

## 與其他來源的衝突

無。
