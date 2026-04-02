import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "queue"
    / "moving-average-from-data-stream.py"
)


def load_module(test_case: unittest.TestCase):
    spec = importlib.util.spec_from_file_location("moving_average_stream", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    if spec is None or spec.loader is None:
        test_case.fail("solution module spec should load")
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # pragma: no cover - red phase coverage
        test_case.fail(f"solution module should import cleanly: {exc}")
    return module


class MovingAverageTests(unittest.TestCase):
    def test_next_returns_prompt_sample_sequence(self):
        module = load_module(self)
        moving_average = module.MovingAverage(3)

        self.assertEqual(moving_average.next(1), 1.0)
        self.assertEqual(moving_average.next(10), 5.5)
        self.assertAlmostEqual(moving_average.next(3), 14 / 3)
        self.assertEqual(moving_average.next(5), 6.0)

    def test_main_prints_prompt_sample_harness(self):
        completed = subprocess.run(
            [sys.executable, str(MODULE_PATH)],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("Window size: 3", completed.stdout)
        self.assertIn("Input values: [1, 10, 3, 5]", completed.stdout)
        self.assertIn("Expected outputs: [1.0, 5.5, 4.666666666666667, 6.0]", completed.stdout)
        self.assertIn("Actual outputs: [1.0, 5.5, 4.666666666666667, 6.0]", completed.stdout)
        self.assertIn("Matches expected: True", completed.stdout)


if __name__ == "__main__":
    unittest.main()
