from __future__ import annotations

import argparse
import pprint
import sys
import traceback
import unittest
from typing import Any


PROBLEM_STATEMENT = """Best K-Day Step Streak

You get daily step counts and an integer `k`. Return the maximum total steps
over any window of exactly `k` consecutive days.

If `k <= 0` or `k` is bigger than the input size, return `None`.
"""


def best_k_day_steps(steps: list[int], k: int) -> int | None:
    """Return the best fixed-size window sum for the provided inputs."""
    # A fixed-size window must have at least 1 day and cannot be longer than the list.
    if k <= 0 or k > len(steps):
        return None

    left = 0
    # `right` is inclusive, so the first k-day window spans indices 0 through k - 1.
    right = k - 1
    # Slices stop before the end index, so `right + 1` includes the full first window.
    cur_total_steps = sum(steps[left:right + 1])
    # Start with the first full fixed-size window, then compare later windows against it.
    best_total_steps = cur_total_steps
    # Stop once `right` is at the last index; sliding again would step past the array.
    while right < len(steps) - 1:
        # Fixed-size window slide order: remove old left, move both ends, add new right.
        # This order keeps the window size at k and helps avoid off-by-one mistakes.
        cur_total_steps -= steps[left]
        left += 1
        right += 1
        cur_total_steps += steps[right]
        best_total_steps = max(best_total_steps,
                               cur_total_steps)
    return best_total_steps

EXAMPLE_CASES = [
    {
        "name": "example prompt case",
        "input": {"steps": [4, 2, 7, 1, 8, 3], "k": 3},
        "expected": 16,
    },
]

EDGE_CASES = [
    {
        "name": "returns none when k is zero",
        "input": {"steps": [4, 2, 7], "k": 0},
        "expected": None,
    },
    {
        "name": "returns none when k is negative",
        "input": {"steps": [4, 2, 7], "k": -2},
        "expected": None,
    },
    {
        "name": "returns none when k is larger than input length",
        "input": {"steps": [4, 2], "k": 3},
        "expected": None,
    },
    {
        "name": "returns none for empty input",
        "input": {"steps": [], "k": 1},
        "expected": None,
    },
    {
        "name": "k equal to array length uses the whole array",
        "input": {"steps": [3, 1, 2], "k": 3},
        "expected": 6,
    },
    {
        "name": "k of one returns the largest single value",
        "input": {"steps": [3, 9, 2, 5], "k": 1},
        "expected": 9,
    },
    {
        "name": "single element valid window",
        "input": {"steps": [11], "k": 1},
        "expected": 11,
    },
]

TRICKY_CASES = [
    {
        "name": "best window occurs at the start",
        "input": {"steps": [9, 8, 1, 1, 1], "k": 2},
        "expected": 17,
    },
    {
        "name": "best window occurs in the middle",
        "input": {"steps": [1, 3, 10, 2, 1], "k": 2},
        "expected": 13,
    },
    {
        "name": "best window occurs at the end",
        "input": {"steps": [1, 1, 2, 7, 9], "k": 2},
        "expected": 16,
    },
    {
        "name": "all equal values still slide correctly",
        "input": {"steps": [5, 5, 5, 5], "k": 3},
        "expected": 15,
    },
    {
        "name": "strictly increasing values",
        "input": {"steps": [1, 2, 3, 4, 5], "k": 2},
        "expected": 9,
    },
    {
        "name": "strictly decreasing values",
        "input": {"steps": [9, 7, 5, 3], "k": 2},
        "expected": 16,
    },
    {
        "name": "mixed positive and negative values",
        "input": {"steps": [4, -1, 6, -2, 3], "k": 2},
        "expected": 5,
    },
]

ALL_CASES = EXAMPLE_CASES + EDGE_CASES + TRICKY_CASES


def run_case(case: dict[str, Any]) -> tuple[Any, Any, str | None, str | None]:
    """Execute one case and return expected/actual/error state."""
    try:
        actual = best_k_day_steps(**case["input"])
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
                        f"Student implementation missing for {case['name']}: {actual}"
                    )
                if error == "exception":
                    message = f"Unexpected exception for {case['name']}: {actual}"
                    if trace:
                        message = f"{message}\n{trace}"
                    self.fail(message)
                self.assertEqual(expected, actual)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Best K-Day Step Streak scaffold.")
    parser.add_argument("--test", action="store_true", help="Run unittest coverage.")
    args = parser.parse_args()
    if args.test:
        unittest.main(argv=[sys.argv[0]])
        return
    run_examples()


if __name__ == "__main__":
    main()
