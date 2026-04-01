import importlib.util
import json
import tempfile
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "download_problem_catalog.py"


def load_catalog_module(test_case: unittest.TestCase):
    if not MODULE_PATH.exists():
        test_case.fail("Problem catalog script should exist")
    spec = importlib.util.spec_from_file_location("download_problem_catalog", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    if spec is None or spec.loader is None:
        test_case.fail("Problem catalog module spec should load")
    spec.loader.exec_module(module)
    return module


class ProblemCatalogTests(unittest.TestCase):
    def test_extract_problem_catalog_returns_sorted_numbered_entries(self):
        module = load_catalog_module(self)

        payload = {
            "stat_status_pairs": [
                {
                    "stat": {
                        "frontend_question_id": 300,
                        "question__title": "Longest Increasing Subsequence",
                        "question__title_slug": "longest-increasing-subsequence",
                    }
                },
                {
                    "stat": {
                        "frontend_question_id": 2,
                        "question__title": "Add Two Numbers",
                        "question__title_slug": "add-two-numbers",
                    }
                },
                {
                    "stat": {
                        "frontend_question_id": 1,
                        "question__title": "Two Sum",
                        "question__title_slug": "two-sum",
                    }
                },
            ]
        }

        catalog = module.extract_problem_catalog(payload)

        self.assertEqual(
            catalog,
            [
                {"frontend_id": 1, "title": "Two Sum", "title_slug": "two-sum"},
                {"frontend_id": 2, "title": "Add Two Numbers", "title_slug": "add-two-numbers"},
                {
                    "frontend_id": 300,
                    "title": "Longest Increasing Subsequence",
                    "title_slug": "longest-increasing-subsequence",
                },
            ],
        )

    def test_write_problem_catalog_persists_pretty_json(self):
        module = load_catalog_module(self)
        catalog = [
            {"frontend_id": 1, "title": "Two Sum", "title_slug": "two-sum"},
            {"frontend_id": 2, "title": "Add Two Numbers", "title_slug": "add-two-numbers"},
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "catalog.json"

            module.write_problem_catalog(output_path, catalog)

            self.assertTrue(output_path.exists())
            written = json.loads(output_path.read_text())
            self.assertEqual(written, catalog)
            self.assertEqual(output_path.read_text().splitlines()[0], "[")


if __name__ == "__main__":
    unittest.main()
