---
title: XZ Utils 後門
type: event
sources: [nvd-cves, tukaani-xz-backdoor, openwall-xz-disclosure]
updated: 2026-11-18
---
# XZ Utils 後門（CVE-2024-3094）

**一句話摘要**：取得 xz 發布權限的維護者帳號，在 5.6.0 與 5.6.1 的發布 tarball 中植入後門，可能影響透過 liblzma 連到的 sshd。（來源：[XZ 說明頁](../sources/tukaani-xz-backdoor.md)、[NVD](../sources/nvd-cves.md)）

## 時間線

- 2024-03-29：Andres Freund 在 oss-security 郵件論壇揭露。（來源：[揭露郵件](../sources/openwall-xz-disclosure.md)）
- 2024-03-29：NVD 發布 CVE-2024-3094，CVSS 10.0。（來源：[NVD](../sources/nvd-cves.md)）
- 2024-04-09：XZ 的 Git repository 在 GitHub 恢復。
- 2024-05-29：發布乾淨的新版本。（來源：[XZ 說明頁](../sources/tukaani-xz-backdoor.md)）

## 怎麼被發現的

在 Debian sid 上注意到 ssh 登入異常吃 CPU；量測後，被拒絕的 ssh 登入從約 0.30 秒變成約 0.81 秒。（來源：[揭露郵件](../sources/openwall-xz-disclosure.md)）

## 機制

1. 惡意程式碼只在**上游發布的 tarball** 中，觸發碼從未進入 Git repository。（來源：[XZ 說明頁](../sources/tukaani-xz-backdoor.md)）
2. 建置 liblzma 時，從一個**偽裝成測試檔**的檔案取出預先編好的目的檔，修改 liblzma 的特定函式。（來源：[NVD](../sources/nvd-cves.md)）
3. 多個發行版替 OpenSSH 加上 systemd 通知支援，使 sshd 連結到 liblzma，後門因此能影響 sshd。（來源：[揭露郵件](../sources/openwall-xz-disclosure.md)）

## 相關概念

[軟體供應鏈攻擊](../concepts/supply-chain-attack.md)・[可重現建置](../concepts/reproducible-builds.md)
