import subprocess
import sys
from pathlib import Path
import unittest


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "strings" / "344-reverse-string.py"
)


class ReverseStringHarnessTests(unittest.TestCase):
    def test_main_reports_match_status_for_correct_samples(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )

        output = result.stdout

        self.assertIn("Actual:", output)
        self.assertIn("Expected:", output)
        self.assertIn("Matches expected: True", output)
        self.assertNotIn("Diff:", output)


if __name__ == "__main__":
    unittest.main()
