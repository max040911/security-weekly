"""LLM Wiki 檢查（CLAUDE.md 第 8 節）。

用法：python scripts/lint_wiki.py
檢查 front matter、連結、目錄完整性、孤兒來源，以及「事實接地」：
concept / event 頁出現的 CVE 編號與版本號，必須能在它引用的 raw 原文中找到。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TYPES = {"source": "sources", "concept": "concepts", "event": "events", "meta": ""}
LINK_RE = re.compile(r"\]\(([^)\s]+?\.md)(#[^)]*)?\)")
FACT_RE = re.compile(r"CVE-\d{4}-\d{4,7}|(?<![\w.])\d+\.\d+(?:\.\d+)*(?:-(?:alpha|beta)\d+)?(?![\w.])")


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        v = v.strip()
        fm[k.strip()] = [s.strip() for s in v[1:-1].split(",") if s.strip()] if v.startswith("[") else v
    return fm, text[m.end():]


def main():
    errors = []
    pages = {p: p.read_text(encoding="utf-8") for p in WIKI.rglob("*.md") if "raw" not in p.parts}
    raws = {p.stem: p.read_text(encoding="utf-8") for p in (WIKI / "raw").glob("*.md")}
    source_raw = {}          # source slug -> raw text
    referenced_sources = set()

    for path, text in sorted(pages.items()):
        rel = path.relative_to(WIKI).as_posix()
        err = lambda m: errors.append(f"wiki/{rel}: {m}")
        fm, body = front_matter(text)
        if fm is None:
            err("缺少 YAML front matter")
            continue
        for key in ("title", "type", "updated"):
            if not fm.get(key):
                err(f"front matter 缺 {key}")
        t = fm.get("type")
        if t not in TYPES:
            err(f"type 不合法：{t}")
            continue
        if TYPES[t] and path.parent.name != TYPES[t]:
            err(f"type={t} 應放在 {TYPES[t]}/")
        if "{{" in text or "{%" in text:
            err("含有 Liquid 會吃掉的 {{ 或 {%")

        links = [m.group(1) for m in LINK_RE.finditer(body)]
        for l in links:
            if not l.startswith("http") and not (path.parent / l).resolve().exists():
                err(f"連結目標不存在：{l}")

        if t == "source":
            raw = re.search(r"\]\(\.\./raw/([\w-]+)\.md\)", body)
            if not raw or raw.group(1) not in raws:
                err("source 頁必須連到存在的 ../raw/<slug>.md")
            else:
                source_raw[path.stem] = raws[raw.group(1)]
        if t in ("concept", "event"):
            cited = {Path(l).stem for l in links if "/sources/" in f"/{l}" or l.startswith("../sources/")}
            referenced_sources |= cited
            if not cited:
                err("concept / event 頁至少要引用一個 sources/ 頁")
            declared = set(fm.get("sources") or [])
            if declared != cited:
                err(f"front matter sources {sorted(declared)} 與內文引用 {sorted(cited)} 不一致")

    # 事實接地：等所有 source 頁讀完再檢查
    for path, text in sorted(pages.items()):
        fm, body = front_matter(text)
        if not fm or fm.get("type") not in ("concept", "event"):
            continue
        cited = [s for s in (fm.get("sources") or []) if s in source_raw]
        corpus = "\n".join(source_raw[s] for s in cited)
        for fact in sorted(set(FACT_RE.findall(body))):
            if fact not in corpus:
                errors.append(f"wiki/{path.relative_to(WIKI).as_posix()}: 「{fact}」在引用的 raw 原文中找不到（來源：{cited}）")

    # 目錄完整、沒有孤兒來源
    index = pages.get(WIKI / "index.md", "")
    for path in pages:
        rel = path.relative_to(WIKI).as_posix()
        if rel != "index.md" and f"({rel})" not in index:
            errors.append(f"wiki/index.md: 沒有列出 {rel}")
    for slug in source_raw:
        if slug not in referenced_sources:
            errors.append(f"wiki/sources/{slug}.md: 沒有任何 concept / event 頁引用（孤兒來源）")

    if errors:
        print("\n".join(f"✗ {e}" for e in errors))
        print(f"\n{len(errors)} 個問題")
        return 1
    n = {t: sum(1 for p in pages if p.parent.name == d) for t, d in TYPES.items() if d}
    print(f"OK：{len(pages)} 頁（來源 {n['source']}、概念 {n['concept']}、事件 {n['event']}），raw {len(raws)} 份")
    return 0


if __name__ == "__main__":
    sys.exit(main())
