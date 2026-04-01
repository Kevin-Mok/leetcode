#!/usr/bin/env python3
import argparse
import json
import urllib.error
import urllib.request
from pathlib import Path


PROBLEMSET_URL = "https://leetcode.com/api/problems/all/"
DEFAULT_OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "leetcode-problem-catalog.json"


def fetch_problemset_payload(timeout_seconds=20):
    request = urllib.request.Request(
        PROBLEMSET_URL,
        headers={
            "Referer": "https://leetcode.com/problemset/",
            "User-Agent": "Mozilla/5.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"LeetCode catalog download failed: {exc}") from exc


def extract_problem_catalog(payload):
    catalog = []
    for question in payload.get("stat_status_pairs", []):
        stat = question.get("stat", {})
        frontend_id = stat.get("frontend_question_id")
        title = stat.get("question__title")
        title_slug = stat.get("question__title_slug")
        if frontend_id is None or not title or not title_slug:
            continue
        catalog.append(
            {
                "frontend_id": int(frontend_id),
                "title": title,
                "title_slug": title_slug,
            }
        )
    return sorted(catalog, key=lambda question: question["frontend_id"])


def write_problem_catalog(output_path, catalog):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(catalog, indent=2) + "\n")


def build_parser():
    parser = argparse.ArgumentParser(
        description="Download the current LeetCode problem catalog and store it locally.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help=f"Where to write the catalog JSON (default: {DEFAULT_OUTPUT_PATH})",
    )
    return parser


def main():
    args = build_parser().parse_args()
    payload = fetch_problemset_payload()
    catalog = extract_problem_catalog(payload)
    write_problem_catalog(args.output, catalog)
    print(f"Wrote {len(catalog)} problems to {args.output}")


if __name__ == "__main__":
    main()
