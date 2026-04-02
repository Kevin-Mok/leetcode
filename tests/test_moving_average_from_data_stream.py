import importlib.util
from pathlib import Path
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


if __name__ == "__main__":
    unittest.main()
