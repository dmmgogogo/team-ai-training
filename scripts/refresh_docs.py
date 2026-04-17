#!/usr/bin/env python3
"""
Minimal documentation refresh utility.

Goals:
1) Update "最后更新" markers to current YYYY年M月.
2) Update README "最近更新：YYYY-MM-DD" date to today.
3) Emit a markdown audit report with touched files and unresolved stale markers.

This script intentionally avoids altering semantic content. It keeps automation safe
for a 3-day cadence and leaves deep content rewrites to humans/agents.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports"
REPORT_FILE = REPORT_DIR / "auto-refresh-report.md"

TARGET_FILES = [
    ROOT / "README.md",
    ROOT / "references.md",
    ROOT / "02-llm-landscape" / "01-global-models.md",
    ROOT / "02-llm-landscape" / "02-domestic-models.md",
    ROOT / "02-llm-landscape" / "03-comparison.md",
    ROOT / "03-ai-coding-tools" / "01-overview.md",
    ROOT / "03-ai-coding-tools" / "02-cursor.md",
    ROOT / "03-ai-coding-tools" / "03-other-tools.md",
    ROOT / "05-practical" / "11-cost-management.md",
    ROOT / "07-skills" / "04-opencli.md",
]


def today() -> dt.date:
    return dt.date.today()


def update_month_markers(text: str, current_month_zh: str) -> tuple[str, int]:
    # Match "最后更新：2026年3月" style.
    pattern = re.compile(r"(最后更新：)\d{4}年\d{1,2}月")
    new_text, count = pattern.subn(rf"\1{current_month_zh}", text)
    return new_text, count


def update_readme_day_marker(text: str, current_day_iso: str) -> tuple[str, int]:
    # Match "最近更新：2026-04-12" in README top line.
    pattern = re.compile(r"(最近更新：)\d{4}-\d{2}-\d{2}")
    new_text, count = pattern.subn(rf"\1{current_day_iso}", text)
    return new_text, count


def find_stale_markers(text: str) -> list[str]:
    # Only report candidates; do not auto-modify historical content.
    markers: list[str] = []
    for m in re.finditer(r"2026年3月|2026-03", text):
        start = max(0, m.start() - 24)
        end = min(len(text), m.end() + 24)
        snippet = text[start:end].replace("\n", " ")
        markers.append(snippet.strip())
    return markers


def main() -> int:
    d = today()
    current_month_zh = f"{d.year}年{d.month}月"
    current_day_iso = d.strftime("%Y-%m-%d")

    touched: list[tuple[Path, int]] = []
    stale_hits: list[tuple[Path, list[str]]] = []

    for file_path in TARGET_FILES:
        if not file_path.exists():
            continue

        old = file_path.read_text(encoding="utf-8")
        new = old
        change_count = 0

        new, c1 = update_month_markers(new, current_month_zh)
        change_count += c1

        if file_path.name == "README.md":
            new, c2 = update_readme_day_marker(new, current_day_iso)
            change_count += c2

        if new != old:
            file_path.write_text(new, encoding="utf-8")
            touched.append((file_path, change_count))

        hits = find_stale_markers(new)
        if hits:
            stale_hits.append((file_path, hits[:6]))

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Auto Refresh Report",
        "",
        f"- Run date: `{current_day_iso}`",
        f"- Current month marker: `{current_month_zh}`",
        "",
        "## Updated files",
        "",
    ]

    if touched:
        for fp, count in touched:
            rel = fp.relative_to(ROOT)
            lines.append(f"- `{rel}` (replacements: {count})")
    else:
        lines.append("- No file updated.")

    lines.extend(["", "## Remaining stale marker candidates", ""])
    if stale_hits:
        for fp, snippets in stale_hits:
            rel = fp.relative_to(ROOT)
            lines.append(f"- `{rel}`")
            for s in snippets:
                lines.append(f"  - `{s}`")
    else:
        lines.append("- None found in target files.")

    lines.append("")
    lines.append("> Note: historical event references may remain intentionally.")
    lines.append("")

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written: {REPORT_FILE.relative_to(ROOT)}")
    print(f"Updated files: {len(touched)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
