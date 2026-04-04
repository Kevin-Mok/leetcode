# Merge Worktree To Main Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a repo script that safely merges the current worktree branch into `main`, but only after the latest changed LeetCode solution file passes its local test harness, then pushes `origin main`.

**Architecture:** Add a small Python CLI in `scripts/` that gathers git state with `subprocess.run`, detects the latest changed LeetCode solution relative to `main`, runs `python3 <problem-file> --test`, and only then performs the merge workflow. Cover the command-building and safety gates with `unittest` mocks so the workflow can be verified without mutating git state.

**Tech Stack:** Python 3 standard library, `subprocess`, `pathlib`, `unittest`, `unittest.mock`

---

### Task 1: Define script behavior with tests

**Files:**
- Create: `tests/test_merge_worktree_to_main.py`
- Test: `tests/test_merge_worktree_to_main.py`

- [ ] **Step 1: Write the failing tests**

Cover:
- latest changed LeetCode solution detection from `git diff --name-only main...HEAD`
- rejection when no changed solution file exists
- default merge flow runs latest-problem test before checkout/merge/push
- cleanup flags keep the branch or worktree when requested

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_merge_worktree_to_main -v`
Expected: FAIL because `scripts/merge_worktree_to_main.py` does not exist yet

### Task 2: Implement the merge helper

**Files:**
- Create: `scripts/merge_worktree_to_main.py`
- Modify: `tests/test_merge_worktree_to_main.py`

- [ ] **Step 1: Write the minimal implementation**

Implement:
- argument parsing for `--dry-run`, `--keep-branch`, `--keep-worktree`, and `--base-branch`
- clean working tree check
- branch detection and refusal to run from `main`
- latest changed LeetCode `.py` file detection from the branch diff against `main`
- latest problem test command: `python3 <problem-file> --test`
- merge sequence: checkout base branch, pull, merge current branch, push origin base branch
- optional branch deletion and worktree removal

- [ ] **Step 2: Run test to verify it passes**

Run: `python3 -m unittest tests.test_merge_worktree_to_main -v`
Expected: PASS

### Task 3: Verify the dry-run workflow

**Files:**
- Modify: `scripts/merge_worktree_to_main.py` if output needs adjustment

- [ ] **Step 1: Run the full targeted test set**

Run: `python3 -m unittest tests.test_merge_worktree_to_main tests.test_update_readme -v`
Expected: PASS

- [ ] **Step 2: Run a dry-run from the current worktree**

Run: `python3 scripts/merge_worktree_to_main.py --dry-run`
Expected: prints the latest changed LeetCode problem path, its test command, and the merge/push command sequence without mutating git state

- [ ] **Step 3: Review plan results**

Confirm:
- the script fails closed on unsafe state
- the latest changed LeetCode test runs before any merge action
- the default path merges to `main` and pushes `origin main`
