#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


class MergeWorkflowError(RuntimeError):
    """Raised when the merge workflow cannot proceed safely."""


def run_command(command: list[str], *, capture_output: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        check=True,
        capture_output=capture_output,
        text=True,
    )


def git_output(*args: str) -> str:
    return run_command(["git", *args], capture_output=True).stdout.strip()


def ensure_clean_worktree() -> None:
    if git_output("status", "--short"):
        raise MergeWorkflowError("Working tree is dirty; commit or stash changes before merging.")


def current_branch() -> str:
    branch_name = git_output("branch", "--show-current")
    if not branch_name:
        raise MergeWorkflowError("Unable to determine current branch.")
    return branch_name


def find_latest_problem_path(changed_paths: list[str]) -> Path:
    for raw_path in changed_paths:
        path = Path(raw_path.strip())
        if not raw_path.strip():
            continue
        if path.suffix != ".py":
            continue
        if path.parts[0] in {"tests", "scripts"}:
            continue
        if path.name.startswith("test_"):
            continue
        return path
    raise MergeWorkflowError("No changed LeetCode solution file found relative to the base branch.")


def latest_problem_path(base_branch: str) -> Path:
    changed = git_output("diff", "--name-only", f"{base_branch}...HEAD")
    return find_latest_problem_path(changed.splitlines())


def worktree_path_for_branch(branch_name: str) -> str | None:
    output = git_output("worktree", "list", "--porcelain")
    current_worktree = None
    for line in output.splitlines():
        if line.startswith("worktree "):
            current_worktree = line.removeprefix("worktree ").strip()
            continue
        if line.startswith("branch refs/heads/") and current_worktree is not None:
            listed_branch = line.removeprefix("branch refs/heads/").strip()
            if listed_branch == branch_name:
                return current_worktree
    return None


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge the current worktree branch into main and push.")
    parser.add_argument("--base-branch", default="main", help="Base branch to merge into.")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing them.")
    parser.add_argument("--keep-branch", action="store_true", help="Do not delete the merged branch.")
    parser.add_argument("--keep-worktree", action="store_true", help="Do not remove the merged worktree.")
    return parser.parse_args(argv)


def build_commands(branch_name: str, base_branch: str, problem_path: Path) -> list[list[str]]:
    return [
        ["python3", str(problem_path), "--test"],
        ["git", "checkout", base_branch],
        ["git", "pull"],
        ["git", "merge", branch_name],
        ["git", "push", "origin", base_branch],
    ]


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or [])
    try:
        branch_name = current_branch()
        if branch_name == args.base_branch:
            raise MergeWorkflowError(f"Already on {args.base_branch}; run this from a feature worktree branch.")

        problem_path = latest_problem_path(args.base_branch)
        commands = build_commands(branch_name, args.base_branch, problem_path)

        if args.dry_run:
            print(f"Latest problem: {problem_path}")
            for command in commands:
                print(" ".join(command))
            if not args.keep_branch:
                print(f"git branch -d {branch_name}")
            if not args.keep_worktree:
                worktree_path = worktree_path_for_branch(branch_name)
                if worktree_path:
                    print(f"git worktree remove {worktree_path}")
            return 0

        ensure_clean_worktree()
        for command in commands:
            run_command(command)

        if not args.keep_branch:
            run_command(["git", "branch", "-d", branch_name])

        if not args.keep_worktree:
            worktree_path = worktree_path_for_branch(branch_name)
            if worktree_path:
                run_command(["git", "worktree", "remove", worktree_path])
        return 0
    except MergeWorkflowError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
