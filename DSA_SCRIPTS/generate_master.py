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
    table = []
    table.append("| " + " | ".join(headers) + " |")
    table.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        table.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(table)


def get_primary_approach(approach_text: str) -> str:
    """
    For sorting:
    - "Binary Search, Two Pointer" -> "Binary Search"
    - "Two Pointer" -> "Two Pointer"
    """
    if not approach_text:
        return "-"
    parts = [p.strip() for p in approach_text.split(",") if p.strip()]
    return parts[0] if parts else "-"


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

        prereq = fm.get("prerequisite", "").strip()
        video = fm.get("video", "").strip()

        # Must have at least problem + platform link
        if not problem or not link:
            continue

        # ✅ Solution link -> opens your Obsidian note (works on GitHub too)
        relative_note_path = os.path.relpath(path, os.path.join(BASE_DIR, "DSA"))
        relative_note_path = relative_note_path.replace("\\", "/")
        solution_link = md_link("View", f"./{relative_note_path}")

        # ✅ optional links
        prereq_link = md_link("Open", prereq) if prereq else "-"
        video_link = md_link("Watch", video) if video else "-"

        approach_text = approach if approach else "-"
        primary_approach = get_primary_approach(approach_text)

        data.append({
            "problem": problem,
            "link": link,
            "status": status if status else "PENDING",
            "approach": approach_text,
            "primary_approach": primary_approach,   # used only for sorting
            "level": level if level else "-",
            "prerequisite": prereq_link,
            "video": video_link,
            "solution": solution_link,
        })

    # ---------------- TABLE 1: Quick View ----------------
    # Sort by problem name
    data.sort(key=lambda x: x["problem"].lower())

    quick_rows = []
    for i, p in enumerate(data, start=1):
        quick_rows.append([
            i,
            p["problem"],                 # NOT clickable
            md_link("Open", p["link"]),   # platform link
            p["status"]
        ])

    quick_table = build_markdown_table(
        ["S No.", "Problem Name", "Platform Link", "Status"],
        quick_rows
    )

    # ---------------- TABLE 2: Detailed View ----------------
    # Sort by FIRST approach only (clean ordering), then problem name
    data2 = sorted(data, key=lambda x: (x["primary_approach"].lower(), x["problem"].lower()))

    detail_rows = []
    for i, p in enumerate(data2, start=1):
        detail_rows.append([
            i,
            p["problem"],                 # NOT clickable
            md_link("Open", p["link"]),   # platform link
            p["approach"],                # full approach text (supports multi)
            p["level"],
            p["prerequisite"],
            p["video"],
            p["solution"]
        ])

    detail_table = build_markdown_table(
        ["S No.", "Problem Name", "Platform Link", "Approach", "Level", "Pre-requisite", "Video Solution", "Solution"],
        detail_rows
    )

    # Write master file
    content = f"""# DSA MASTER LIST

## Table 1: Quick View
{quick_table}

---

## Table 2: Detailed View
{detail_table}
"""

    with open(MASTER_FILE, "w", encoding="utf-8") as fp:
        fp.write(content)

    print(f"✅ Updated: {MASTER_FILE}")
    print(f"✅ Total problems: {len(data)}")


if __name__ == "__main__":
    main()
