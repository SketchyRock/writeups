#!/usr/bin/env python3
"""Rebuild the index table in README.md and index.json from each document's front matter.

Run from anywhere:  python3 scripts/build_index.py
Add --check to validate front matter without writing anything.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- index:start -->", "<!-- index:end -->"
REQUIRED = ["title", "type", "category", "event", "tags"]
CATEGORIES = [
    ("ctf", "Capture the flag"),
    ("cyber-defense", "Cyber defense"),
    ("competitive-programming", "Competitive programming"),
    ("makeathon", "Makeathons"),
    ("conference", "Conferences"),
]
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def parse_value(raw):
    raw = raw.split("  #")[0].strip()
    if raw.startswith('"'):
        return json.loads(raw)
    if raw.startswith("["):
        try:
            return json.loads(raw)
        except ValueError:
            return [x.strip() for x in raw.strip("[]").split(",") if x.strip()]
    return raw


def read_doc(path):
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("no front matter")
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            meta[k.strip()] = parse_value(v)
    meta["path"] = path.relative_to(ROOT).as_posix()
    meta["has_breadcrumb"] = "[← All write-ups](../README.md)" in text
    return meta


def pretty_date(meta):
    d, e = meta.get("date", ""), meta.get("end_date", "")
    parts = d.split("-")
    if len(parts) < 2:
        return d
    label = f"{MONTHS[int(parts[1]) - 1]} {parts[0]}"
    return label


def sort_key(meta):
    return meta.get("date", ""), meta["title"]


def main():
    check = "--check" in sys.argv
    docs, problems = [], []
    for path in sorted(ROOT.glob("20*/*.md")):
        try:
            meta = read_doc(path)
        except ValueError as err:
            problems.append(f"{path.name}: {err}")
            continue
        for field in REQUIRED:
            if not meta.get(field):
                problems.append(f"{path.name}: missing '{field}'")
        if not meta["has_breadcrumb"]:
            problems.append(f"{path.name}: missing '[← All write-ups](../README.md)' under the H1")
        docs.append(meta)

    if problems:
        print("Problems:\n  " + "\n  ".join(problems))
        if check:
            sys.exit(1)

    out = []
    retros = [d for d in docs if d["type"] == "retrospective"]
    for cat, heading in CATEGORIES:
        rows = sorted((d for d in retros if d["category"] == cat), key=sort_key, reverse=True)
        if not rows:
            continue
        out += [f"### {heading}", "", "| Event | Date | Result |", "|---|---|---|"]
        for d in rows:
            out.append(f"| [{d['title']}]({d['path']}) | {pretty_date(d)} | {d.get('result', '')} |")
        out.append("")
    refs = sorted((d for d in docs if d["type"] != "retrospective"), key=sort_key, reverse=True)
    if refs:
        out += ["### Reference and project notes", "", "| Document | For | Type |", "|---|---|---|"]
        for d in refs:
            out.append(f"| [{d['title']}]({d['path']}) | {d['event']} | {d['type']} |")
        out.append("")
    block = f"{START}\n\n" + "\n".join(out).rstrip() + f"\n\n{END}"

    readme = (ROOT / "README.md").read_text()
    if START not in readme:
        sys.exit(f"README.md is missing the {START} / {END} markers")
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, readme, flags=re.S)

    index = [{k: v for k, v in d.items() if k != "has_breadcrumb"} for d in sorted(docs, key=sort_key, reverse=True)]
    if check:
        print(f"{len(docs)} documents checked")
        return
    (ROOT / "README.md").write_text(new)
    (ROOT / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote README.md and index.json ({len(docs)} documents)")


if __name__ == "__main__":
    main()
