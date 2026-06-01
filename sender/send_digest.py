#!/usr/bin/env python3

import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path


EXTRACTORS = [
    "extractors/examples/custom_topic_extract.py",
]

DELIVERY_CHANNEL = "telegram"  # telegram or slack
TELEGRAM_ACCOUNT = "your_account"
TELEGRAM_TARGET = "your_target"


def calc_window(days: int = 7):
    today = datetime.now().date()
    end_date = today - timedelta(days=1)
    start_date = end_date - timedelta(days=days - 1)
    return str(start_date), str(end_date)


def run_extractor(path: str, start_date: str, end_date: str):
    output = subprocess.check_output([
        "python3",
        path,
        start_date,
        end_date,
        "--included-only",
    ], text=True)

    return json.loads(output).get("candidates", [])


def build_digest(items, start_date: str, end_date: str):
    lines = [
        "Weekly News Digest",
        "",
        f"Period: {start_date} — {end_date}",
        "",
    ]

    if not items:
        lines.append("No relevant updates found.")
        return "\n".join(lines)

    for i, item in enumerate(items, 1):
        lines.extend([
            f"{i}. {item.get('title')}",
            f"Date: {item.get('date')}",
            f"Category: {item.get('category')}",
            f"Score: {item.get('score')}/10",
            "",
            "Why it matters:",
            item.get("reason", "Relevant update."),
            "",
            "URL:",
            item.get("url"),
            "",
        ])

    return "\n".join(lines)


def main():
    start_date, end_date = calc_window()

    items = []
    for extractor in EXTRACTORS:
        items.extend(run_extractor(extractor, start_date, end_date))

    # Deduplicate by URL
    seen = set()
    deduped = []
    for item in items:
        url = item.get("url")
        if url and url not in seen:
            seen.add(url)
            deduped.append(item)

    digest = build_digest(deduped, start_date, end_date)

    print(digest)


if __name__ == "__main__":
    main()
