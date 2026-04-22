from __future__ import annotations

import argparse
import pprint
import sys
import traceback
import unittest
from typing import Any


PROBLEM_STATEMENT = """Smallest Announcement Clip

Given a string and a required list, find the shortest consecutive substring
containing all required characters at least once. Return an empty string if it
is impossible.
"""


def smallest_announcement_clip(announcement: str, required: list[str]) -> str:
    """Return the smallest valid substring for the provided inputs."""
    raise NotImplementedError(
        "Implement smallest_announcement_clip before running these tests."
    )


EXAMPLE_CASES = [
    {
        "name": "example prompt case",
        "input": {"announcement": "xbacbabca", "required": ["a", "b", "c"]},
        "expected": "bac",
    },
]

EDGE_CASES = [
    {
        "name": "empty required list returns empty string",
        "input": {"announcement": "abc", "required": []},
        "expected": "",
    },
    {
        "name": "empty announcement cannot satisfy non-empty required list",
        "input": {"announcement": "", "required": ["a"]},
        "expected": "",
    },
    {
        "name": "impossible coverage returns empty string",
        "input": {"announcement": "ab", "required": ["a", "b", "c"]},
        "expected": "",
    },
    {
        "name": "single character valid window",
        "input": {"announcement": "zzaz", "required": ["a"]},
        "expected": "a",
    },
    {
        "name": "whole string may be the only valid answer",
        "input": {"announcement": "abc", "required": ["a", "b", "c"]},
        "expected": "abc",
    },
]

TRICKY_CASES = [
    {
        "name": "smallest window appears at the start",
        "input": {"announcement": "abcxxxx", "required": ["a", "b", "c"]},
        "expected": "abc",
    },
    {
        "name": "smallest window appears at the end",
        "input": {"announcement": "xxxxabc", "required": ["a", "b", "c"]},
        "expected": "abc",
    },
    {
        "name": "multiple candidate windows choose the shortest one",
        "input": {"announcement": "ADOBECODEBANC", "required": ["A", "B", "C"]},
        "expected": "BANC",
    },
    {
        "name": "irrelevant characters around the answer are ignored",
        "input": {"announcement": "xxabcyy", "required": ["a", "b", "c"]},
        "expected": "abc",
    },
    {
        "name": "repeated required characters inside the window do not confuse coverage",
        "input": {"announcement": "aaabcbcdbca", "required": ["a", "b", "c"]},
        "expected": "abc",
    },
    {
        "name": "shrinking stops exactly when the window becomes invalid",
        "input": {"announcement": "cabefgecdaecf", "required": ["c", "a", "e"]},
        "expected": "aec",
    },
    {
        "name": "required order does not matter",
        "input": {"announcement": "xbacbabca", "required": ["c", "a", "b"]},
        "expected": "bac",
    },
]

ALL_CASES = EXAMPLE_CASES + EDGE_CASES + TRICKY_CASES


def run_case(case: dict[str, Any]) -> tuple[Any, Any, str | None]:
    """Execute one case and return expected/actual/error state."""
    try:
        actual = smallest_announcement_clip(**case["input"])
    except NotImplementedError as exc:
        return case["expected"], f"<not implemented: {exc}>", "not_implemented"
    except Exception as exc:  # pragma: no cover - surfaced in example mode
        trace = "".join(traceback.format_exception(exc)).rstrip()
        return case["expected"], f"<exception: {trace}>", "exception"
    return case["expected"], actual, None


def run_examples() -> None:
    """Print the example fixtures and the current implementation status."""
    print(PROBLEM_STATEMENT)
    print()
    for case in EXAMPLE_CASES:
        expected, actual, error = run_case(case)
        print(case["name"])
        print(f"Input: {pprint.pformat(case['input'], sort_dicts=False)}")
        print(f"Expected: {expected!r}")
        print(f"Actual: {actual!r}")
        print(f"Matches expected: {error is None and actual == expected}")
        if error is not None:
            print("Status: implementation still needed")
        print()


class GeneratedTests(unittest.TestCase):
    def test_all_cases(self) -> None:
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                expected, actual, error = run_case(case)
                if error == "not_implemented":
                    self.fail(
                        "Student implementation missing for "
                        f"{case['name']}: {actual}"
                    )
                if error == "exception":
                    self.fail(f"Unexpected exception for {case['name']}: {actual}")
                self.assertEqual(expected, actual)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Smallest Announcement Clip scaffold."
    )
    parser.add_argument("--test", action="store_true", help="Run unittest coverage.")
    args = parser.parse_args()
    if args.test:
        unittest.main(argv=[sys.argv[0]])
        return
    run_examples()


if __name__ == "__main__":
    main()
