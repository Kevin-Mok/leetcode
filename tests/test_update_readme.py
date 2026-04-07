import importlib.util
import tempfile
from pathlib import Path
import unittest
from unittest import mock


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "update_readme.py"


def load_update_readme_module(test_case: unittest.TestCase):
    if not MODULE_PATH.exists():
        test_case.fail("README updater script should exist")
    spec = importlib.util.spec_from_file_location("update_readme", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    if spec is None or spec.loader is None:
        test_case.fail("README updater module spec should load")
    spec.loader.exec_module(module)
    return module


class FakeLeetCodeClient:
    def __init__(self, *, by_id=None, by_slug=None, search_results=None):
        self.by_id = by_id or {}
        self.by_slug = by_slug or {}
        self.search_results = search_results or {}

    def question_by_frontend_id(self, frontend_id):
        question = self.by_id.get(str(frontend_id))
        if not question:
            return None
        return make_problem_metadata(question)

    def question_by_slug(self, title_slug):
        question = self.by_slug.get(title_slug)
        if not question:
            return None
        return make_problem_metadata(question)

    def search_questions(self, keyword):
        return [make_problem_metadata(question) for question in self.search_results.get(keyword, [])]


def make_problem_metadata(question):
    return type(
        "ProblemMetadataStub",
        (),
        {
            "frontend_id": question["frontend_id"],
            "title": question["title"],
            "title_slug": question["title_slug"],
            "difficulty": question["difficulty"],
        },
    )()


class ResolveProblemMetadataTests(unittest.TestCase):
    def test_resolve_problem_metadata_prefers_frontend_id_from_filename(self):
        module = load_update_readme_module(self)
        client = FakeLeetCodeClient(
            by_id={
                "94": {
                    "frontend_id": "94",
                    "title": "Binary Tree Inorder Traversal",
                    "title_slug": "binary-tree-inorder-traversal",
                    "difficulty": "Easy",
                }
            }
        )

        problem = module.resolve_problem_metadata(
            "binary-tree/94-binary-tree-inorder-traversal.py",
            {},
            client,
        )

        self.assertEqual(problem.frontend_id, "94")
        self.assertEqual(problem.title_slug, "binary-tree-inorder-traversal")
        self.assertEqual(problem.difficulty, "Easy")

    def test_resolve_problem_metadata_uses_slug_when_filename_has_no_leading_id(self):
        module = load_update_readme_module(self)
        client = FakeLeetCodeClient(
            by_slug={
                "minimum-depth-of-binary-tree": {
                    "frontend_id": "111",
                    "title": "Minimum Depth of Binary Tree",
                    "title_slug": "minimum-depth-of-binary-tree",
                    "difficulty": "Easy",
                }
            }
        )

        problem = module.resolve_problem_metadata(
            "binary-tree/111-minimum-depth-of-binary-tree.py",
            {},
            client,
        )

        self.assertEqual(problem.frontend_id, "111")
        self.assertEqual(problem.title_slug, "minimum-depth-of-binary-tree")

    def test_resolve_problem_metadata_uses_override_before_lookup(self):
        module = load_update_readme_module(self)
        client = FakeLeetCodeClient(
            by_id={
                "1962": {
                    "frontend_id": "1962",
                    "title": "Remove Stones to Minimize the Total",
                    "title_slug": "remove-stones-to-minimize-the-total",
                    "difficulty": "Medium",
                }
            }
        )

        problem = module.resolve_problem_metadata(
            "heap/remove-stones-to-minimize-total.py",
            {
                "heap/remove-stones-to-minimize-total.py": {
                    "frontend_id": "1962",
                    "title_slug": "remove-stones-to-minimize-the-total",
                }
            },
            client,
        )

        self.assertEqual(problem.frontend_id, "1962")
        self.assertEqual(problem.difficulty, "Medium")

    def test_resolve_problem_metadata_fails_closed_when_search_is_ambiguous(self):
        module = load_update_readme_module(self)
        client = FakeLeetCodeClient(
            search_results={
                "remove-stones-to-minimize-total": [
                    {
                        "frontend_id": "1962",
                        "title": "Remove Stones to Minimize the Total",
                        "title_slug": "remove-stones-to-minimize-the-total",
                        "difficulty": "Medium",
                    },
                    {
                        "frontend_id": "1753",
                        "title": "Maximum Score From Removing Stones",
                        "title_slug": "maximum-score-from-removing-stones",
                        "difficulty": "Medium",
                    },
                ]
            }
        )

        with self.assertRaises(module.ProblemLookupError):
            module.resolve_problem_metadata(
                "heap/remove-stones-to-minimize-total.py",
                {},
                client,
            )


class NotableProblemSelectionTests(unittest.TestCase):
    def test_select_notable_problems_picks_the_hardest_entry_per_category(self):
        module = load_update_readme_module(self)

        problems = [
            module.ProblemEntry(
                repo_path="dynamic-programming/300-longest-increasing-subsequence.py",
                category="dynamic-programming",
                frontend_id="300",
                title="Longest Increasing Subsequence",
                title_slug="longest-increasing-subsequence",
                difficulty="Medium",
                has_harness=True,
                has_test=False,
                demonstrates="state modeling",
            ),
            module.ProblemEntry(
                repo_path="dynamic-programming/894-all-possible-full-binary-trees.py",
                category="dynamic-programming",
                frontend_id="894",
                title="All Possible Full Binary Trees",
                title_slug="all-possible-full-binary-trees",
                difficulty="Medium",
                has_harness=True,
                has_test=False,
                demonstrates="state modeling",
            ),
            module.ProblemEntry(
                repo_path="binary-tree/226-invert-binary-tree.py",
                category="binary-tree",
                frontend_id="226",
                title="Invert Binary Tree",
                title_slug="invert-binary-tree",
                difficulty="Easy",
                has_harness=True,
                has_test=False,
                demonstrates="tree recursion",
            ),
            module.ProblemEntry(
                repo_path="binary-tree/94-binary-tree-inorder-traversal.py",
                category="binary-tree",
                frontend_id="94",
                title="Binary Tree Inorder Traversal",
                title_slug="binary-tree-inorder-traversal",
                difficulty="Easy",
                has_harness=True,
                has_test=True,
                demonstrates="tree recursion",
            ),
            module.ProblemEntry(
                repo_path="heap/1962-remove-stones-to-minimize-the-total.py",
                category="heap",
                frontend_id="1962",
                title="Remove Stones to Minimize the Total",
                title_slug="remove-stones-to-minimize-the-total",
                difficulty="Medium",
                has_harness=True,
                has_test=False,
                demonstrates="priority queue updates",
            ),
            module.ProblemEntry(
                repo_path="linked-list/83-remove-duplicates-from-sorted-list.py",
                category="linked-list",
                frontend_id="83",
                title="Remove Duplicates from Sorted List",
                title_slug="remove-duplicates-from-sorted-list",
                difficulty="Easy",
                has_harness=False,
                has_test=False,
                demonstrates="pointer rewiring",
            ),
        ]

        notable = module.select_notable_problems(problems)

        self.assertEqual(len(notable), 4)
        self.assertEqual(
            [problem.repo_path for problem in notable],
            [
                "dynamic-programming/894-all-possible-full-binary-trees.py",
                "heap/1962-remove-stones-to-minimize-the-total.py",
                "binary-tree/94-binary-tree-inorder-traversal.py",
                "linked-list/83-remove-duplicates-from-sorted-list.py",
            ],
        )


class CollectProblemEntriesTests(unittest.TestCase):
    def test_collect_problem_entries_infers_demonstrates_when_override_is_missing(self):
        module = load_update_readme_module(self)
        client = FakeLeetCodeClient(
            by_id={
                "226": {
                    "frontend_id": "226",
                    "title": "Invert Binary Tree",
                    "title_slug": "invert-binary-tree",
                    "difficulty": "Easy",
                }
            }
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            override_path = repo_root / "overrides.json"
            override_path.write_text("{}\n")
            problem_path = repo_root / "binary-tree" / "226-invert-binary-tree.txt"
            problem_path.parent.mkdir(parents=True, exist_ok=True)
            problem_path.write_text(
                "Solution\n"
                "Given the root of a binary tree, invert the tree, and return its root.\n"
            )

            with mock.patch.object(module, "collect_solution_paths", return_value=["binary-tree/226-invert-binary-tree.py"]), mock.patch.object(
                module, "collect_test_paths", return_value=[]
            ), mock.patch.object(module, "detect_harness", return_value=True), mock.patch.object(
                module, "detect_test_coverage", return_value=False
            ):
                problems = module.collect_problem_entries(repo_root, override_path, client)

        self.assertEqual(
            problems[0].demonstrates,
            "inverting a binary tree and returning the flipped root structure",
        )

    def test_repo_override_file_preserves_custom_demonstrates(self):
        repo_root = Path(__file__).resolve().parents[1]
        overrides = load_update_readme_module(self).load_overrides(
            repo_root / "scripts" / "readme_problem_overrides.json"
        )

        self.assertEqual(
            overrides.get("stack/71-simplify-path.py", {}).get("demonstrates"),
            "0 ms runtime, 100th-percentile result on a Medium stack problem",
        )
        self.assertEqual(
            overrides.get("queue/346-moving-average-from-data-stream.py", {}).get("demonstrates"),
            "3 ms runtime, 82.25th-percentile speed, 22.10 MB memory, 92.75th-percentile memory efficiency",
        )

    def test_collect_problem_entries_preserves_custom_demonstrates_override(self):
        module = load_update_readme_module(self)
        client = FakeLeetCodeClient(
            by_id={
                "71": {
                    "frontend_id": "71",
                    "title": "Simplify Path",
                    "title_slug": "simplify-path",
                    "difficulty": "Medium",
                }
            }
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            override_path = repo_root / "overrides.json"
            override_path.write_text(
                '{\n'
                '  "stack/71-simplify-path.py": {\n'
                '    "demonstrates": "0 ms runtime, 100th-percentile result on a Medium stack problem"\n'
                "  }\n"
                "}\n"
            )

            with mock.patch.object(module, "collect_solution_paths", return_value=["stack/71-simplify-path.py"]), mock.patch.object(
                module, "collect_test_paths", return_value=[]
            ), mock.patch.object(module, "detect_harness", return_value=True), mock.patch.object(
                module, "detect_test_coverage", return_value=False
            ):
                problems = module.collect_problem_entries(repo_root, override_path, client)

        self.assertEqual(len(problems), 1)
        self.assertEqual(
            problems[0].demonstrates,
            "0 ms runtime, 100th-percentile result on a Medium stack problem",
        )

    def test_collect_problem_entries_uses_distinct_inferred_demonstrates_in_same_category(self):
        module = load_update_readme_module(self)
        client = FakeLeetCodeClient(
            by_id={
                "94": {
                    "frontend_id": "94",
                    "title": "Binary Tree Inorder Traversal",
                    "title_slug": "binary-tree-inorder-traversal",
                    "difficulty": "Easy",
                },
                "226": {
                    "frontend_id": "226",
                    "title": "Invert Binary Tree",
                    "title_slug": "invert-binary-tree",
                    "difficulty": "Easy",
                },
            }
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            override_path = repo_root / "overrides.json"
            override_path.write_text("{}\n")
            prompt_dir = repo_root / "binary-tree"
            prompt_dir.mkdir(parents=True, exist_ok=True)
            (prompt_dir / "94-binary-tree-inorder-traversal.txt").write_text(
                "Solution\n"
                "Given the root of a binary tree, return the inorder traversal of its nodes' values.\n"
            )
            (prompt_dir / "226-invert-binary-tree.txt").write_text(
                "Solution\n"
                "Given the root of a binary tree, invert the tree, and return its root.\n"
            )

            with mock.patch.object(
                module,
                "collect_solution_paths",
                return_value=[
                    "binary-tree/94-binary-tree-inorder-traversal.py",
                    "binary-tree/226-invert-binary-tree.py",
                ],
            ), mock.patch.object(module, "collect_test_paths", return_value=[]), mock.patch.object(
                module, "detect_harness", return_value=True
            ), mock.patch.object(module, "detect_test_coverage", return_value=False):
                problems = module.collect_problem_entries(repo_root, override_path, client)

        demonstrates_by_path = {problem.repo_path: problem.demonstrates for problem in problems}
        self.assertEqual(
            demonstrates_by_path["binary-tree/94-binary-tree-inorder-traversal.py"],
            "walking a binary tree in left-root-right order and returning the visited values",
        )
        self.assertEqual(
            demonstrates_by_path["binary-tree/226-invert-binary-tree.py"],
            "inverting a binary tree and returning the flipped root structure",
        )


class RenderReadmeTests(unittest.TestCase):
    def test_render_readme_groups_problems_by_difficulty_and_includes_metrics(self):
        module = load_update_readme_module(self)
        problems = [
            module.ProblemEntry(
                repo_path="heap/1962-remove-stones-to-minimize-the-total.py",
                category="heap",
                frontend_id="1962",
                title="Remove Stones to Minimize the Total",
                title_slug="remove-stones-to-minimize-the-total",
                difficulty="Medium",
                has_harness=True,
                has_test=False,
                demonstrates="priority queue updates",
            ),
            module.ProblemEntry(
                repo_path="binary-tree/94-binary-tree-inorder-traversal.py",
                category="binary-tree",
                frontend_id="94",
                title="Binary Tree Inorder Traversal",
                title_slug="binary-tree-inorder-traversal",
                difficulty="Easy",
                has_harness=True,
                has_test=True,
                demonstrates="tree recursion",
            ),
        ]

        rendered = module.render_readme(problems, regression_test_count=2)

        self.assertIn("Solved Problems By Difficulty", rendered)
        self.assertIn("## Medium", rendered)
        self.assertIn("## Easy", rendered)
        self.assertNotIn("## Hard", rendered)
        self.assertNotIn("| Hard problems |", rendered)
        self.assertLess(rendered.index("## Medium"), rendered.index("## Easy"))
        self.assertIn("| Solved problems | 2 |", rendered)
        self.assertIn("| Runnable local harnesses | 2 |", rendered)
        self.assertIn("| Problems with detected regression coverage | 2 |", rendered)
        self.assertIn("[1962. Remove Stones to Minimize the Total](heap/1962-remove-stones-to-minimize-the-total.py)", rendered)
        self.assertIn("[94. Binary Tree Inorder Traversal](binary-tree/94-binary-tree-inorder-traversal.py)", rendered)
        self.assertIn("[Heap](heap)", rendered)
        self.assertIn("[Binary Tree](binary-tree)", rendered)
        self.assertNotIn("| Problem | Category | Repo Path | What This Demonstrates |", rendered)
        self.assertNotIn("`heap/1962-remove-stones-to-minimize-the-total.py`", rendered)
        self.assertIn("What This Demonstrates", rendered)
        self.assertIn("python3 scripts/update_readme.py", rendered)
        self.assertIn("python3 scripts/download_problem_catalog.py", rendered)
        self.assertIn("python3 scripts/merge_worktree_to_main.py --dry-run", rendered)
        self.assertIn("`python3 scripts/merge_worktree_to_main.py`", rendered)
        self.assertIn("Supports `--dry-run` to print the exact merge sequence", rendered)
        self.assertIn("data/leetcode-problem-catalog.json", rendered)
        self.assertIn("This repository turns LeetCode practice into recruiter-facing proof", rendered)
        self.assertIn("arrays and strings, stacks, hash maps, heaps, linked lists, binary trees", rendered)
        self.assertIn("The README is generated from tracked solution files plus live LeetCode metadata", rendered)
        self.assertIn("## Recruiter Proof Surface", rendered)
        self.assertIn("Generated metrics and notable-problem tables turn the repo into a durable evidence surface", rendered)
        self.assertIn("Generated README workflow backed by tracked files and live difficulty metadata", rendered)
        self.assertNotIn("## Why This Repo Is Worth Reviewing", rendered)
        self.assertNotIn("## Recruiter Notes", rendered)


class MainCheckModeTests(unittest.TestCase):
    def test_main_check_mode_returns_zero_when_readme_is_current(self):
        module = load_update_readme_module(self)

        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            readme_path = repo_root / "README.md"
            rendered = "# generated\n"
            readme_path.write_text(rendered)

            with mock.patch.object(module, "collect_problem_entries", return_value=[]), mock.patch.object(
                module, "render_readme", return_value=rendered
            ):
                exit_code = module.main(["--check", "--repo-root", str(repo_root)])

        self.assertEqual(exit_code, 0)

    def test_main_check_mode_returns_nonzero_when_readme_differs(self):
        module = load_update_readme_module(self)

        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            (repo_root / "README.md").write_text("# stale\n")

            with mock.patch.object(module, "collect_problem_entries", return_value=[]), mock.patch.object(
                module, "render_readme", return_value="# generated\n"
            ):
                exit_code = module.main(["--check", "--repo-root", str(repo_root)])

        self.assertEqual(exit_code, 1)


if __name__ == "__main__":
    unittest.main()
