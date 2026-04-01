import subprocess
import sys
from pathlib import Path
import unittest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "stack" / "simplify-path.py"


class SimplifyPathHarnessTests(unittest.TestCase):
    def test_main_reports_match_status_for_prompt_samples(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )

        output = result.stdout

        self.assertIn("Input: /home/", output)
        self.assertIn("Expected: /home", output)
        self.assertIn("Actual: /home", output)
        self.assertIn("Matches expected: True", output)
        self.assertNotIn("Actual: not implemented", output)


if __name__ == "__main__":
    unittest.main()
