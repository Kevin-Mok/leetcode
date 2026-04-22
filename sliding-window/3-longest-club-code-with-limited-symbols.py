from __future__ import annotations

import argparse
import pprint
import sys
import traceback
import unittest
from typing import Any


PROBLEM_STATEMENT = """Longest Club Code With Limited Symbols

Given a string and `k`, find the longest contiguous section with at most `k`
distinct symbols.
"""


def longest_code_with_limited_symbols(code: str, k: int) -> int:
    """Return the maximum valid window length for the provided inputs."""
    raise NotImplementedError(
        "Implement longest_code_with_limited_symbols before running these tests."
    )


EXAMPLE_CASES = [
    {
        "name": "example prompt case",
        "input": {"code": "AAHBBCCB", "k": 2},
        "expected": 5,
    },
]

EDGE_CASES = [
    {
        "name": "empty string returns zero",
        "input": {"code": "", "k": 2},
        "expected": 0,
    },
    {
        "name": "non-positive k returns zero",
        "input": {"code": "ABC", "k": 0},
        "expected": 0,
    },
    {
        "name": "negative k returns zero",
        "input": {"code": "ABC", "k": -1},
        "expected": 0,
    },
    {
        "name": "k of one forces a single-symbol window",
        "input": {"code": "AABBA", "k": 1},
        "expected": 2,
    },
    {
        "name": "k larger than distinct count uses the whole string",
        "input": {"code": "ABCA", "k": 5},
        "expected": 4,
    },
    {
        "name": "all same character uses the whole string",
        "input": {"code": "AAAAAA", "k": 1},
        "expected": 6,
    },
    {
        "name": "all distinct characters are limited by k",
        "input": {"code": "ABCDE", "k": 2},
        "expected": 2,
    },
]

TRICKY_CASES = [
    {
        "name": "longest valid window appears at the start",
        "input": {"code": "AABBBCDE", "k": 2},
        "expected": 5,
    },
    {
        "name": "longest valid window appears in the middle",
        "input": {"code": "ZZABBBCCYY", "k": 2},
        "expected": 5,
    },
    {
        "name": "longest valid window appears at the end",
        "input": {"code": "XYZBBBCC", "k": 2},
        "expected": 5,
    },
    {
        "name": "duplicate heavy input requires count tracking",
        "input": {"code": "ABACCC", "k": 2},
        "expected": 4,
    },
    {
        "name": "shrinking may require multiple left moves",
        "input": {"code": "ECEBA", "k": 2},
        "expected": 3,
    },
    {
        "name": "zero count entries must stop counting as distinct",
        "input": {"code": "ABBCBBA", "k": 2},
        "expected": 6,
    },
]

ALL_CASES = EXAMPLE_CASES + EDGE_CASES + TRICKY_CASES


def run_case(case: dict[str, Any]) -> tuple[Any, Any, str | None, str | None]:
    """Execute one case and return expected/actual/error state."""
    try:
        actual = longest_code_with_limited_symbols(**case["input"])
    except NotImplementedError as exc:
        return case["expected"], f"<not implemented: {exc}>", "not_implemented", None
    except Exception as exc:  # pragma: no cover - surfaced in example mode
        trace = "".join(traceback.format_exception(exc)).rstrip()
        return (
            case["expected"],
            f"<exception: {exc.__class__.__name__}: {exc}>",
            "exception",
            trace,
        )
    return case["expected"], actual, None, None


def run_examples() -> None:
    """Print the example fixtures and the current implementation status."""
    print(PROBLEM_STATEMENT)
    print()
    for case in EXAMPLE_CASES:
        expected, actual, error, trace = run_case(case)
        print(case["name"])
        print(f"Input: {pprint.pformat(case['input'], sort_dicts=False)}")
        print(f"Expected: {expected!r}")
        print(f"Actual: {actual!r}")
        print(f"Matches expected: {error is None and actual == expected}")
        if error == "not_implemented":
            print("Status: implementation still needed")
        elif error == "exception":
            print("Status: implementation raised an exception")
        if trace:
            print("Traceback:")
            print(trace)
        print()


class GeneratedTests(unittest.TestCase):
    def test_all_cases(self) -> None:
        for case in ALL_CASES:
            with self.subTest(case=case["name"]):
                expected, actual, error, trace = run_case(case)
                if error == "not_implemented":
                    self.fail(
                        "Student implementation missing for "
                        f"{case['name']}: {actual}"
                    )
                if error == "exception":
                    message = f"Unexpected exception for {case['name']}: {actual}"
                    if trace:
                        message = f"{message}\n{trace}"
                    self.fail(message)
                self.assertEqual(expected, actual)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Longest Club Code With Limited Symbols scaffold."
    )
    parser.add_argument("--test", action="store_true", help="Run unittest coverage.")
    args = parser.parse_args()
    if args.test:
        unittest.main(argv=[sys.argv[0]])
        return
    run_examples()


if __name__ == "__main__":
    main()
