import importlib.util
from pathlib import Path
import unittest
from unittest import mock


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "merge_worktree_to_main.py"


def load_module(test_case: unittest.TestCase):
    if not MODULE_PATH.exists():
        test_case.fail("Merge helper script should exist")
    spec = importlib.util.spec_from_file_location("merge_worktree_to_main", MODULE_PATH)
    if spec is None or spec.loader is None:
        test_case.fail("Merge helper module spec should load")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def completed(stdout: str = ""):
    return mock.Mock(stdout=stdout, returncode=0)


class LatestProblemDetectionTests(unittest.TestCase):
    def test_find_latest_problem_prefers_first_changed_solution_file(self):
        module = load_module(self)

        latest = module.find_latest_problem_path(
            [
                "README.md",
                "binary-search/longest-subsequence-with-limited-sum.py",
                "tests/test_update_readme.py",
                "binary-search/longest-subsequence-with-limited-sum.txt",
            ]
        )

        self.assertEqual(latest, Path("binary-search/longest-subsequence-with-limited-sum.py"))

    def test_find_latest_problem_rejects_when_no_solution_file_changed(self):
        module = load_module(self)

        with self.assertRaises(module.MergeWorkflowError):
            module.find_latest_problem_path(["README.md", "tests/test_update_readme.py"])


class MergeWorkflowTests(unittest.TestCase):
    def test_dry_run_skips_clean_tree_gate_but_prints_merge_plan(self):
        module = load_module(self)
        commands = []

        def fake_run(command, *, cwd=None, check=True, capture_output=False, text=False):
            commands.append(tuple(command))
            if command == ["git", "branch", "--show-current"]:
                return completed("wip/problem\n")
            if command == ["git", "diff", "--name-only", "main...HEAD"]:
                return completed("stack/71-simplify-path.py\n")
            if command == ["git", "worktree", "list", "--porcelain"]:
                return completed(
                    "worktree /repo/.worktrees/wip/problem\n"
                    "branch refs/heads/wip/problem\n"
                )
            if command == ["git", "status", "--short"]:
                raise AssertionError("dry-run should not require a clean tree")
            return completed("")

        with mock.patch.object(module.subprocess, "run", side_effect=fake_run):
            exit_code = module.main(["--dry-run"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            commands,
            [
                ("git", "branch", "--show-current"),
                ("git", "diff", "--name-only", "main...HEAD"),
                ("git", "worktree", "list", "--porcelain"),
            ],
        )

    def test_default_flow_runs_latest_problem_test_before_merge_and_push(self):
        module = load_module(self)
        commands = []

        def fake_run(command, *, cwd=None, check=True, capture_output=False, text=False):
            commands.append((tuple(command), cwd, capture_output, text))
            if command == ["git", "status", "--short"]:
                return completed("")
            if command == ["git", "branch", "--show-current"]:
                return completed("wip/longest-subsequence-with-limited-sum\n")
            if command == ["git", "diff", "--name-only", "main...HEAD"]:
                return completed(
                    "README.md\nbinary-search/longest-subsequence-with-limited-sum.py\n"
                )
            if command == ["git", "worktree", "list", "--porcelain"]:
                return completed(
                    "worktree /repo\nbranch refs/heads/main\n\n"
                    "worktree /repo/.worktrees/wip-longest-subsequence-with-limited-sum\n"
                    "branch refs/heads/wip/longest-subsequence-with-limited-sum\n"
                )
            return completed("")

        with mock.patch.object(module.subprocess, "run", side_effect=fake_run):
            exit_code = module.main([])

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            [command for command, _, _, _ in commands],
            [
                ("git", "branch", "--show-current"),
                ("git", "diff", "--name-only", "main...HEAD"),
                ("git", "status", "--short"),
                ("python3", "binary-search/longest-subsequence-with-limited-sum.py", "--test"),
                ("git", "worktree", "list", "--porcelain"),
                ("git", "pull", "--rebase", "origin", "main"),
                ("git", "merge", "wip/longest-subsequence-with-limited-sum"),
                ("git", "push", "origin", "main"),
                ("git", "branch", "-d", "wip/longest-subsequence-with-limited-sum"),
                ("git", "worktree", "list", "--porcelain"),
                (
                    "git",
                    "worktree",
                    "remove",
                    "/repo/.worktrees/wip-longest-subsequence-with-limited-sum",
                ),
            ],
        )
        self.assertEqual(
            commands[4:8],
            [
                (("git", "worktree", "list", "--porcelain"), None, True, True),
                (("git", "pull", "--rebase", "origin", "main"), "/repo", False, True),
                (
                    ("git", "merge", "wip/longest-subsequence-with-limited-sum"),
                    "/repo",
                    False,
                    True,
                ),
                (("git", "push", "origin", "main"), "/repo", False, True),
            ],
        )

    def test_default_flow_runs_base_branch_commands_in_its_existing_worktree(self):
        module = load_module(self)
        commands = []

        def fake_run(command, *, cwd=None, check=True, capture_output=False, text=False):
            commands.append((tuple(command), cwd, capture_output, text))
            if command == ["git", "status", "--short"]:
                return completed("")
            if command == ["git", "branch", "--show-current"]:
                return completed("wip/problem\n")
            if command == ["git", "diff", "--name-only", "main...HEAD"]:
                return completed("stack/71-simplify-path.py\n")
            if command == ["git", "worktree", "list", "--porcelain"]:
                return completed(
                    "worktree /repo\n"
                    "branch refs/heads/main\n\n"
                    "worktree /repo/.worktrees/wip/problem\n"
                    "branch refs/heads/wip/problem\n"
                )
            if command == ["git", "checkout", "main"]:
                raise AssertionError("base branch commands should run in the main worktree")
            return completed("")

        with mock.patch.object(module.subprocess, "run", side_effect=fake_run):
            exit_code = module.main([])

        self.assertEqual(exit_code, 0)
        self.assertIn((("git", "pull", "--rebase", "origin", "main"), "/repo", False, True), commands)
        self.assertIn((("git", "merge", "wip/problem"), "/repo", False, True), commands)
        self.assertIn((("git", "push", "origin", "main"), "/repo", False, True), commands)

    def test_keep_flags_skip_cleanup_commands(self):
        module = load_module(self)
        commands = []

        def fake_run(command, *, cwd=None, check=True, capture_output=False, text=False):
            commands.append(tuple(command))
            if command == ["git", "status", "--short"]:
                return completed("")
            if command == ["git", "branch", "--show-current"]:
                return completed("wip/problem\n")
            if command == ["git", "diff", "--name-only", "main...HEAD"]:
                return completed("stack/71-simplify-path.py\n")
            if command == ["git", "worktree", "list", "--porcelain"]:
                return completed("worktree /repo\nbranch refs/heads/main\n")
            return completed("")

        with mock.patch.object(module.subprocess, "run", side_effect=fake_run):
            exit_code = module.main(["--keep-branch", "--keep-worktree"])

        self.assertEqual(exit_code, 0)
        self.assertNotIn(("git", "branch", "-d", "wip/problem"), commands)


if __name__ == "__main__":
    unittest.main()
