"""資安週報結構檢查：驗證 CLAUDE.md 第 3、4、6 節的規則。

用法：python scripts/check_site.py
全部通過時印出 OK 並回傳 0；否則列出問題並回傳 1。只用標準函式庫。
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISSUES = ROOT / "issues"
NAME_RE = re.compile(r"^(\d{3})-[a-z0-9]+(?:-[a-z0-9]+)*\.html$")
REQUIRED_IDS = ["tldr", "deep-dive", "briefs", "glossary"]
DEEP_DIVE_H3 = ["先備概念", "事件經過", "技術機制", "防禦與啟示"]


class Page(HTMLParser):
    """收集檢查需要的結構資訊。"""

    def __init__(self):
        super().__init__()
        self.ids, self.hrefs, self.ext_links = [], [], []
        self.section = None
        self.tldr_items, self.h3_deep, self.briefs, self.dl_items = [], [], 0, 0
        self.brief_sources = []          # 每則短訊的外部連結數
        self.has_inline_style = False
        self.has_issue_nav = False
        self.has_header = False
        self._capture = None
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "style" in a or tag == "style":
            self.has_inline_style = True
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "section" and a.get("id") in REQUIRED_IDS:
            self.section = a["id"]
        cls = a.get("class", "").split()
        if tag == "header" and "issue-header" in cls:
            self.has_header = True
        if tag == "nav" and "issue-nav" in cls:
            self.has_issue_nav = True
        if tag == "article" and "brief" in cls:
            self.briefs += 1
            self.brief_sources.append(0)
        if tag == "a" and "href" in a:
            href = a["href"]
            self.hrefs.append(href)
            if href.startswith("http"):
                self.ext_links.append(a)
                if self.section == "briefs" and self.brief_sources:
                    self.brief_sources[-1] += 1
        if tag == "dt" and self.section == "glossary":
            self.dl_items += 1
        if (tag == "li" and self.section == "tldr") or (tag == "h3" and self.section == "deep-dive"):
            self._capture, self._buf = tag, ""

    def handle_data(self, data):
        if self._capture:
            self._buf += data

    def handle_endtag(self, tag):
        if tag == self._capture:
            text = self._buf.strip()
            (self.tldr_items if tag == "li" else self.h3_deep).append(text)
            self._capture = None
        if tag == "section":
            self.section = None


def parse(path):
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))
    return p


def check_issue(path, errors):
    rel = path.relative_to(ROOT).as_posix()
    p = parse(path)
    err = lambda msg: errors.append(f"{rel}: {msg}")

    if not p.has_header:
        err('缺少 <header class="issue-header">')
    for i in REQUIRED_IDS:
        if i not in p.ids:
            err(f"缺少 #{i} 區塊")
    if len(p.tldr_items) != 3:
        err(f"#tldr 應剛好 3 句，目前 {len(p.tldr_items)} 句")
    for s in p.tldr_items:
        if len(s) > 40:
            err(f"#tldr 句子超過 40 字（{len(s)} 字）：{s[:20]}…")
    if p.h3_deep != DEEP_DIVE_H3:
        err(f"#deep-dive 的 h3 應為 {DEEP_DIVE_H3}，目前 {p.h3_deep}")
    if not 3 <= p.briefs <= 5:
        err(f"#briefs 應有 3–5 則，目前 {p.briefs} 則")
    for n, c in enumerate(p.brief_sources, 1):
        if c == 0:
            err(f"第 {n} 則短訊沒有來源連結")
    if not 3 <= p.dl_items <= 6:
        err(f"#glossary 應有 3–6 個詞條，目前 {p.dl_items} 個")
    if not p.has_issue_nav:
        err('缺少 <nav class="issue-nav">')
    if "{{" in path.read_text(encoding="utf-8"):
        err("仍有未替換的 {{...}} 佔位符")
    return p


def main():
    errors = []
    files = sorted(f for f in ISSUES.glob("*.html"))
    numbers = []
    for f in files:
        m = NAME_RE.match(f.name)
        if not m:
            errors.append(f"issues/{f.name}: 檔名不符 NNN-slug.html")
            continue
        numbers.append(int(m.group(1)))
    if numbers != list(range(1, len(numbers) + 1)):
        errors.append(f"期號應從 001 連續遞增，目前為 {numbers}")

    pages = {f.name: check_issue(f, errors) for f in files}

    # 上下期連結
    names = [f.name for f in files]
    for i, name in enumerate(names):
        hrefs = pages[name].hrefs
        if i > 0 and names[i - 1] not in hrefs:
            errors.append(f"issues/{name}: 缺少連到上一期 {names[i - 1]} 的連結")
        if i < len(names) - 1 and names[i + 1] not in hrefs:
            errors.append(f"issues/{name}: 缺少連到下一期 {names[i + 1]} 的連結")

    # 首頁：列出所有期數、新到舊
    index = parse(ROOT / "index.html")
    listed = [h.split("/")[-1] for h in index.hrefs if h.startswith("issues/")]
    if listed != list(reversed(names)):
        errors.append(f"index.html 期數列表應為新到舊 {list(reversed(names))}，目前 {listed}")

    # 全站：無 inline style、外部連結屬性、相對連結存在
    for f in [ROOT / "index.html", ROOT / "about.html", *files]:
        p = pages.get(f.name) if f.parent == ISSUES else parse(f)
        rel = f.relative_to(ROOT).as_posix()
        if p.has_inline_style:
            errors.append(f"{rel}: 不可使用 inline style 或 <style>")
        for a in p.ext_links:
            if a.get("target") != "_blank" or "noopener" not in a.get("rel", ""):
                errors.append(f"{rel}: 外部連結缺 target/rel：{a['href']}")
        for h in p.hrefs:
            if h.startswith(("http", "#", "mailto:")):
                continue
            if not (f.parent / h.split("#")[0]).resolve().exists():
                errors.append(f"{rel}: 連結目標不存在：{h}")

    if errors:
        print("\n".join(f"✗ {e}" for e in errors))
        return 1
    print(f"OK：{len(files)} 期全部符合規則")
    return 0


if __name__ == "__main__":
    sys.exit(main())
