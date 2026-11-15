# 資安週報

每週一則深講、幾則短訊的資安週報靜態網站，給懂一點程式、但還不是資安專家的讀者。

這個專案的重點不是單一網頁，而是一套**讓 AI 可以照著規則持續新增期數**的設定：

| 檔案 | 作用 |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | 專案規則：目的、結構、命名、每期固定區塊、寫作規則、新增流程 |
| [`AGENTS.md`](AGENTS.md) | 給 Codex 等工具，指向 `CLAUDE.md` |
| [`templates/issue.html`](templates/issue.html) | 新期數模板，所有區塊以 `{{...}}` 佔位 |
| [`scripts/check_site.py`](scripts/check_site.py) | 把規則變成可執行的檢查，AI 完成後必跑 |

## 本機預覽

```bash
python -m http.server 8765
```

開啟 <http://localhost:8765>。

## 新增一期

對 AI 說「新增一期，主題是 ○○」，它會依 `CLAUDE.md` 第 6 節：
複製模板 → 填內容 → 更新上一期的「下一期」連結 → 更新首頁 → 跑檢查腳本。

```bash
python scripts/check_site.py
```

## 發布

GitHub Pages：Settings → Pages → Source 選 `Deploy from a branch`，Branch 選 `main`、資料夾 `/ (root)`。
