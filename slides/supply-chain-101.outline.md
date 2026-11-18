---
title: 簡報大綱：軟體供應鏈安全入門
type: outline
updated: 2026-11-18
---
# 簡報大綱：軟體供應鏈安全入門

workflow 節點 N5 的產出。每張投影片列出依據的 Wiki 頁，以及**逐字引用**的 Wiki 原句（`>` 開頭）。
`scripts/check_slides.py` 會檢查：每張投影片都有大綱、依據頁與 `data-wiki` 一致、每句引用都真的存在於依據頁。
投影片只能改寫這裡引用的內容，不可新增引用以外的事實。

## s1 封面
- 依據：index.md
> 資安週報的知識庫。

## s2 學習目標
- 依據：index.md
> 污染上游，讓惡意程式跟著正常更新進來
> NIST 的安全開發實務，分 PO / PS / PW / RV 四組

## s3 先備概念｜什麼是軟體供應鏈
- 依據：concepts/supply-chain-attack.md
> 不直接攻擊目標，而是污染目標所信任、所依賴的上游軟體或其發布流程，讓惡意程式跟著正常更新一起進來。
> 醬料工廠一旦被動手腳，所有用這款醬料的餐廳一起中毒。

## s4 先備概念｜被攻破的是信任
- 依據：concepts/supply-chain-attack.md
> 使用者信任簽章、信任官方發布檔、信任熱門套件。

## s5 先備概念｜三種入口
- 依據：concepts/supply-chain-attack.md
> 建置 / 發布流程被入侵
> 維護者身分被滲透
> 被廣泛依賴的元件本身有漏洞

## s6 案例｜SolarWinds
- 依據：events/solarwinds.md
> 這個檔案由 SolarWinds 合法的程式碼簽章憑證簽署。
> 至少 2020 年 3 月：入侵活動開始。
> 2020-12-13：CISA 發布緊急指令 ED 21-01，要求聯邦機關中斷受影響設備。
> 安裝後連到 `avsvmcloud[.]com` 的子網域，流量偽裝成正常的 SolarWinds 通訊。

## s7 案例｜XZ 後門
- 依據：events/xz-backdoor.md
> 在 5.6.0 與 5.6.1 的發布 tarball 中植入後門
> 2024-03-29：NVD 發布 CVE-2024-3094，CVSS 10.0。
> 觸發碼從未進入 Git repository。
> 從一個**偽裝成測試檔**的檔案取出預先編好的目的檔
> 多個發行版替 OpenSSH 加上 systemd 通知支援，使 sshd 連結到 liblzma，後門因此能影響 sshd。
> 被拒絕的 ssh 登入從約 0.30 秒變成約 0.81 秒

## s8 案例｜Log4Shell
- 依據：events/log4shell.md
> Java 日誌函式庫 Log4j2 會解析日誌內容中的 JNDI lookup
> 受影響的 Log4j2（2.0-beta9 起）會解析其中的 JNDI lookup。
> JNDI 連到攻擊者控制的 LDAP 伺服器，載入並執行任意程式碼。
> 2021-12-10：NVD 發布 CVE-2021-44228，CVSS 10.0。
> Java 8 以上升級到 2.17.1 以上，可涵蓋本頁列出的所有相關 CVE。

## s9 比較
- 依據：events/solarwinds.md events/xz-backdoor.md events/log4shell.md
> 讓客戶以為是正常更新而安裝
> 觸發碼從未進入 Git repository。
> 程式把使用者輸入寫進日誌

## s10 防禦｜SBOM
- 依據：concepts/sbom.md
> 一份巢狀的清單，列出組成軟體的所有元件
> VEX 說明某產品是否真的受某個已知漏洞影響

## s11 防禦｜SLSA
- 依據：concepts/slsa.md
> L1 是農夫自己手寫的履歷；L2 是由公正的檢驗所出具並蓋章；L3 是檢驗所本身也有嚴格門禁
> 含內部人員、被盜憑證

## s12 防禦｜可重現建置
- 依據：concepts/reproducible-builds.md
> 同樣的原始碼，誰來建置都得到一模一樣的結果。
> 還必須比對「發布檔」與「Git 原始碼」是否一致。

## s13 防禦｜SSDF
- 依據：concepts/ssdf.md
> 人、流程、技術都準備好做安全開發
> 處理發布後的漏洞，並避免再發生

## s14 回到案例
- 依據：concepts/slsa.md concepts/reproducible-builds.md concepts/sbom.md events/log4shell.md
> 這正是 L3「建置過程中被竄改」要防的情境
> 結果會完全一致，卻一樣含有後門
> 有 SBOM 的組織可以直接查清單
> Java 8 以上升級到 2.17.1 以上

## s15 小測驗
- 依據：events/solarwinds.md concepts/sbom.md concepts/reproducible-builds.md
> 這個檔案由 SolarWinds 合法的程式碼簽章憑證簽署。
> 大家最先要回答的是「我們有沒有用到 Log4j？」
> 結果會完全一致，卻一樣含有後門

## s16 重點回顧
- 依據：index.md
> 污染上游，讓惡意程式跟著正常更新進來
> NIST 的安全開發實務，分 PO / PS / PW / RV 四組
