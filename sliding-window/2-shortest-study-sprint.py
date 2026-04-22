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
    raise NotImplementedError(
        "Implement shortest_study_sprint before running these tests."
    )


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
    parser = argparse.ArgumentParser(description="Run the Shortest Study Sprint scaffold.")
    parser.add_argument("--test", action="store_true", help="Run unittest coverage.")
    args = parser.parse_args()
    if args.test:
        unittest.main(argv=[sys.argv[0]])
        return
    run_examples()


if __name__ == "__main__":
    main()
