import os
import re

# ---------------- CONFIG ----------------
BASE_DIR = "/home/mcclusky/dsa-abhyaas/dsa-abhyaas"
PROBLEMS_DIR = BASE_DIR + "/DSA/problems"
MASTER_FILE = BASE_DIR + "/DSA/DSA_MASTER_LIST.md"
# ----------------------------------------



def parse_frontmatter(md_text: str) -> dict:
    """
    Extract YAML frontmatter from markdown.
    Works for simple key: value pairs.
    """
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", md_text, flags=re.DOTALL)
    if not m:
        return fm

    body = m.group(1).strip().splitlines()
    for line in body:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def find_problem_notes(folder: str):
    notes = []
    for root, _, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(".md"):
                notes.append(os.path.join(root, f))
    return notes


def md_link(text: str, url: str) -> str:
    return f"[{text}]({url})"


def build_markdown_table(headers, rows):
    # Markdown table
    table = []
    table.append("| " + " | ".join(headers) + " |")
    table.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        table.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(table)


def main():
    if not os.path.isdir(PROBLEMS_DIR):
        raise SystemExit(f"❌ Problems folder not found: {PROBLEMS_DIR}")

    notes = find_problem_notes(PROBLEMS_DIR)

    data = []
    for path in notes:
        try:
            with open(path, "r", encoding="utf-8") as fp:
                text = fp.read()
        except Exception:
            continue

        fm = parse_frontmatter(text)

        problem = fm.get("problem", "").strip()
        link = fm.get("link", "").strip()
        status = fm.get("status", "").strip()
        approach = fm.get("approach", "").strip()
        level = fm.get("level", "").strip()


        # keep only valid notes
        if not problem or not link:
            continue

        data.append({
            "problem": problem,
            "link": link,
            "status": status if status else "Pending",
            "approach": approach if approach else "-",
            "level": level if level else "-",
            "solution": solution_link
        })

    # Sort by problem name (stable + clean)
    data.sort(key=lambda x: x["problem"].lower())

    # ---------------- TABLE 1 (Quick View) ----------------
    quick_rows = []
    for i, p in enumerate(data, start=1):
        quick_rows.append([
            i,
            p["problem"],  # NOT clickable
            md_link("Open", p["link"]),  # platform link
            p["status"]
        ])

    quick_table = build_markdown_table(
        ["S No.", "Problem Name", "Platform Link", "Status"],
        quick_rows
    )

    # ---------------- TABLE 2 (Approach View) ----------------
    # Sort by approach, then problem
    data2 = sorted(data, key=lambda x: (x["approach"].lower(), x["problem"].lower()))

    detail_rows = []
    for i, p in enumerate(data2, start=1):
        detail_rows.append([
            i,
            p["problem"],                 # NOT clickable
            md_link("Open", p["link"]),   # platform link
            p["approach"],
            p["level"],
            p["solution"]                 # clickable obsidian note link
        ])

    detail_table = build_markdown_table(
        ["S No.", "Problem Name", "Platform Link", "Approach", "Level", "Solution"],
        detail_rows
    )

    # Write master file
    content = f"""# DSA MASTER LIST

## Table 1: Quick View
{quick_table}

---

## Table 2: Approach View
{detail_table}
"""

    with open(MASTER_FILE, "w", encoding="utf-8") as fp:
        fp.write(content)

    print(f"✅ Updated: {MASTER_FILE}")
    print(f"✅ Total problems: {len(data)}")


if __name__ == "__main__":
    main()
