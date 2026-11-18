"""教學簡報檢查（CLAUDE.md 第 9 節，workflow 節點 N8）。

用法：python scripts/check_slides.py
- 每張投影片有 data-wiki，指到存在的 Wiki 頁，頁尾連結與 data-wiki 一致
- 數字接地：CVE、版本號、CVSS、日期、年份都能在引用的 Wiki 頁找到
- 教學結構：data-part 依固定順序出現且齊全；張數 12–18
- 不可有 <script> 或 inline style
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
PARTS = ["cover", "goals", "prereq", "case", "compare", "defense", "revisit", "quiz", "recap"]
FACT_RE = re.compile(
    r"CVE-\d{4}-\d{4,7}"
    r"|\d{4}-\d{2}-\d{2}"
    r"|(?<![\w.])\d+\.\d+(?:\.\d+)*(?:-(?:alpha|beta)\d+)?(?![\w.])"
    r"|(?<!\d)(?:19|20)\d{2}(?= ?年)"
)


class Deck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []          # dicts: part, wiki, refs, text
        self.bad = []
        self.depth = 0            # <section> nesting inside current slide
        self.in_ref = False       # 只計算 <p class="wiki-ref"> 內的依據連結

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "script":
            self.bad.append("含有 <script>")
        if "style" in a:
            self.bad.append(f"<{tag}> 使用 inline style")
        if tag == "section" and "slide" in a.get("class", "").split():
            self.slides.append({"part": a.get("data-part"), "wiki": (a.get("data-wiki") or "").split(),
                                "refs": [], "text": "", "id": a.get("id")})
            self.depth = 1
            return
        if tag == "section" and self.depth:
            self.depth += 1
        if tag == "p" and "wiki-ref" in a.get("class", "").split():
            self.in_ref = True
        if tag == "a" and self.in_ref and "/wiki/" in a.get("href", ""):
            self.slides[-1]["refs"].append(a["href"].split("/wiki/", 1)[1])

    def handle_endtag(self, tag):
        if tag == "p":
            self.in_ref = False
        if tag == "section" and self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if self.depth:
            self.slides[-1]["text"] += data


def check(path, errors):
    rel = path.relative_to(ROOT).as_posix()
    d = Deck()
    d.feed(path.read_text(encoding="utf-8"))
    errors += [f"{rel}: {b}" for b in d.bad]
    n = len(d.slides)
    if not 12 <= n <= 18:
        errors.append(f"{rel}: 投影片應 12–18 張，目前 {n} 張")

    order = []
    for i, s in enumerate(d.slides, 1):
        tag = f"{rel} 第 {i} 張（{s['id']}）"
        if s["part"] not in PARTS:
            errors.append(f"{tag}: data-part 不合法：{s['part']}")
            continue
        order.append(PARTS.index(s["part"]))
        if not s["wiki"]:
            errors.append(f"{tag}: 缺少 data-wiki")
            continue
        corpus = ""
        for w in s["wiki"]:
            f = WIKI / w
            if not f.exists():
                errors.append(f"{tag}: data-wiki 指到不存在的頁面 {w}")
            else:
                corpus += f.read_text(encoding="utf-8")
        refs = sorted(r.replace(".html", ".md") for r in s["refs"])
        if refs != sorted(s["wiki"]):
            errors.append(f"{tag}: 頁尾依據連結 {refs} 與 data-wiki {sorted(s['wiki'])} 不一致")
        text = re.sub(r"\s+", " ", s["text"])
        for fact in sorted(set(FACT_RE.findall(text))):
            if fact not in corpus:
                errors.append(f"{tag}: 「{fact}」在 {s['wiki']} 中找不到")

    check_outline(path, d.slides, errors)

    if order != sorted(order):
        errors.append(f"{rel}: 教學結構順序錯誤，應為 {' → '.join(PARTS)}")
    missing = [p for i, p in enumerate(PARTS) if i not in order]
    if missing:
        errors.append(f"{rel}: 缺少教學段落 {missing}")
    return n


def check_outline(path, slides, errors):
    """N5 大綱：每張投影片都要有大綱段落，依據頁一致，引用句逐字存在於依據頁。"""
    outline = path.with_suffix(".outline.md")
    rel = outline.relative_to(ROOT).as_posix()
    if not outline.exists():
        errors.append(f"{rel}: 缺少大綱檔（workflow N5）")
        return
    sections, cur = {}, None
    for line in outline.read_text(encoding="utf-8").splitlines():
        m = re.match(r"## (s\d+)\b", line)
        if m:
            cur = sections.setdefault(m.group(1), {"wiki": [], "quotes": []})
        elif cur is not None and line.startswith("- 依據："):
            cur["wiki"] = line.split("：", 1)[1].split()
        elif cur is not None and line.startswith("> "):
            cur["quotes"].append(line[2:].strip())
    for s in slides:
        sec = sections.get(s["id"])
        if not sec:
            errors.append(f"{rel}: 缺少 {s['id']} 的大綱")
            continue
        if sorted(sec["wiki"]) != sorted(s["wiki"]):
            errors.append(f"{rel} {s['id']}: 依據 {sec['wiki']} 與投影片 data-wiki {s['wiki']} 不一致")
        if not sec["quotes"]:
            errors.append(f"{rel} {s['id']}: 沒有引用任何 Wiki 原句")
        corpus = "".join((WIKI / w).read_text(encoding="utf-8") for w in sec["wiki"] if (WIKI / w).exists())
        for q in sec["quotes"]:
            if q not in corpus:
                errors.append(f"{rel} {s['id']}: 引用句不在依據頁中：「{q[:30]}」")


def main():
    errors = []
    decks = sorted((ROOT / "slides").glob("*.html"))
    if not decks:
        errors.append("slides/ 中沒有簡報")
    counts = {p.name: check(p, errors) for p in decks}
    if errors:
        print("\n".join(f"✗ {e}" for e in errors))
        print(f"\n{len(errors)} 個問題")
        return 1
    print("OK：" + "、".join(f"{k} {v} 張" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
