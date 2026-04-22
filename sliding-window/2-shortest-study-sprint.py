from __future__ import annotations

import argparse
import pprint
import sys
import traceback
import unittest
from typing import Any


PROBLEM_STATEMENT = """Shortest Study Sprint

You get focused minutes per study block and a target. Find the shortest
consecutive block total that is at least the target, or `0` if no such block
exists.
"""


def shortest_study_sprint(blocks: list[int], target: int) -> int:
    """Return the shortest valid window length for the provided inputs."""
    # If the target is 0, the empty window already meets it, so the shortest length is 0.
    if target == 0:
        return 0

    # This is a variable-size window: expand right to reach the target, then shrink left.
    left, right = 0, 0
    # Start with the first one-element window because `right` is inclusive.
    cur_window_sum = sum(blocks[:right + 1])
    # Any real answer must be smaller than infinity, so this is a safe "not found yet" marker.
    shortest_window = float('inf')
    # Stop once `right` is at the last index; expanding again would go out of bounds.
    while right < len(blocks) - 1:
        # If the window is too small, grow it by moving `right` and adding the new value.
        while ((cur_window_sum < target) and 
               (right < len(blocks) - 1)):
            right += 1
            cur_window_sum += blocks[right]
        # Once the sum is large enough, record this window before trying to shorten it.
        if cur_window_sum >= target:
            shortest_window = min(shortest_window, 
                                  right - left + 1)
        # Then shrink from the left while the window still meets the target.
        # Checking after each shrink is what finds the shortest valid length.
        while ((cur_window_sum >= target) and 
               (left < len(blocks) - 1)):
            cur_window_sum -= blocks[left]
            left += 1
            if cur_window_sum >= target:
                shortest_window = min(shortest_window, 
                                      right - left + 1)
    return shortest_window if shortest_window != float('inf') else 0

EXAMPLE_CASES = [
    {
        "name": "example prompt case",
        "input": {"blocks": [2, 1, 5, 2, 3, 2], "target": 7},
        "expected": 2,
    },
]

EDGE_CASES = [
    {
        "name": "returns zero when no window reaches the target",
        "input": {"blocks": [1, 1, 1], "target": 5},
        "expected": 0,
    },
    {
        "name": "single block can satisfy the target",
        "input": {"blocks": [8, 1, 1], "target": 7},
        "expected": 1,
    },
    {
        "name": "full array is the shortest valid window",
        "input": {"blocks": [1, 2, 3], "target": 6},
        "expected": 3,
    },
    {
        "name": "empty input cannot satisfy a positive target",
        "input": {"blocks": [], "target": 4},
        "expected": 0,
    },
    {
        "name": "zero target should allow an empty-length answer convention",
        "input": {"blocks": [2, 3, 4], "target": 0},
        "expected": 0,
    },
]

TRICKY_CASES = [
    {
        "name": "requires repeated shrinking after one expansion",
        "input": {"blocks": [2, 1, 5, 2, 8], "target": 7},
        "expected": 1,
    },
    {
        "name": "best window appears at the start",
        "input": {"blocks": [4, 4, 1, 1], "target": 8},
        "expected": 2,
    },
    {
        "name": "best window appears at the end",
        "input": {"blocks": [1, 1, 3, 4], "target": 7},
        "expected": 2,
    },
    {
        "name": "duplicate values still find the shortest answer",
        "input": {"blocks": [3, 3, 3, 3], "target": 6},
        "expected": 2,
    },
    {
        "name": "exact hit in the middle beats longer windows",
        "input": {"blocks": [1, 2, 6, 1, 1], "target": 6},
        "expected": 1,
    },
    {
        "name": "multiple valid windows choose the shortest one",
        "input": {"blocks": [1, 4, 4], "target": 4},
        "expected": 1,
    },
    {
        "name": "late shrink after accumulating many values",
        "input": {"blocks": [1, 2, 3, 4, 5], "target": 11},
        "expected": 3,
    },
]

ALL_CASES = EXAMPLE_CASES + EDGE_CASES + TRICKY_CASES
SELECTED_CASES = ALL_CASES


def select_cases(case_name: str | None) -> list[dict[str, Any]]:
    """Return all cases or the single named case."""
    if case_name is None:
        return ALL_CASES
    for case in ALL_CASES:
        if case["name"] == case_name:
            return [case]
    raise ValueError(f"Unknown case: {case_name!r}")


def run_case(case: dict[str, Any]) -> tuple[Any, Any, str | None, str | None]:
    """Execute one case and return expected/actual/error state."""
    try:
        actual = shortest_study_sprint(**case["input"])
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


def run_examples(cases: list[dict[str, Any]]) -> None:
    """Print the example fixtures and the current implementation status."""
    print(PROBLEM_STATEMENT)
    print()
    for case in cases:
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
    def test_select_cases_returns_named_case(self) -> None:
        selected = select_cases("returns zero when no window reaches the target")
        self.assertEqual(
            ["returns zero when no window reaches the target"],
            [case["name"] for case in selected],
        )

    def test_select_cases_rejects_unknown_case(self) -> None:
        with self.assertRaises(ValueError):
            select_cases("missing case")

    def test_all_cases(self) -> None:
        for case in SELECTED_CASES:
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
    global SELECTED_CASES
    parser = argparse.ArgumentParser(description="Run the Shortest Study Sprint scaffold.")
    parser.add_argument("--test", action="store_true", help="Run unittest coverage.")
    parser.add_argument(
        "--case",
        help="Run only the case with the exact matching name.",
    )
    args = parser.parse_args()
    try:
        SELECTED_CASES = select_cases(args.case)
    except ValueError as exc:
        parser.error(str(exc))
    if args.test:
        unittest.main(argv=[sys.argv[0]])
        return
    run_examples(SELECTED_CASES)


if __name__ == "__main__":
    main()
