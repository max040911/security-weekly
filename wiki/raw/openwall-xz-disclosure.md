# RAW（來源卡）: xz backdoor 原始揭露郵件

- url: https://www.openwall.com/lists/oss-security/2024/03/29/4
- author: Andres Freund
- date: 2024-03-29
- fetched: 2026-11-18
- license: 郵件論壇文章，未標示授權 → 只存來源卡
- 本檔為原始資料，ingest 後不得修改。

---

## 短引述

> "The upstream xz repository and the xz tarballs have been backdoored."

## 事實摘錄（依原文）

- Symptom first noticed on Debian sid: ssh logins taking a lot of CPU, plus valgrind errors.
- Measured delay of a rejected ssh login: about 0.30 seconds before, about 0.81 seconds with the backdoor.
- Affected upstream releases: 5.6.0 and 5.6.1.
- Reaches sshd because several distributions patch OpenSSH to support systemd notification, which links liblzma.
