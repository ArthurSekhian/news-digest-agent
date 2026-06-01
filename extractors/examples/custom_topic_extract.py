#!/usr/bin/env python3

import argparse
import json


def build_candidates(start_date: str, end_date: str):
    # Replace this with your own source extraction logic.
    return [
        {
            "title": "Example update title",
            "url": "https://example.com/update",
            "source": "Example Source",
            "date": start_date,
            "category": "Example category",
            "score": 7,
            "include": True,
            "reason": "example item",
        }
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start_date")
    parser.add_argument("end_date")
    parser.add_argument("--included-only", action="store_true")
    args = parser.parse_args()

    candidates = build_candidates(args.start_date, args.end_date)

    if args.included_only:
        candidates = [c for c in candidates if c.get("include") is True]

    print(json.dumps({
        "status": "ok",
        "start_date": args.start_date,
        "end_date": args.end_date,
        "candidates": candidates,
    }, indent=2))


if __name__ == "__main__":
    main()
