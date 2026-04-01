# Simplify Path Init Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `stack/71-simplify-path.py` with a repo-consistent local harness and a regression test that checks the prompt-derived sample cases.

**Architecture:** Save the prompt text locally, add a small subprocess-based unittest for the script output, and implement a direct stack-based path simplifier with a `__main__` harness that prints the prompt examples and whether the implementation matches the expected canonical path. Keep the diff limited to this one problem and its regression coverage.

**Tech Stack:** Python 3, `unittest`, Markdown

---

### Task 1: Confirm Scope And Protect Existing Work

**Files:**
- Create: `plans/init-simplify-path.md`
- Inspect: `stack/71-simplify-path.py`
- Inspect: `stack/71-simplify-path.txt`

- [x] Capture initial `git status --short` before editing tracked files.
- [x] Confirm `stack/71-simplify-path.py` is currently just a placeholder stub.
- [x] Treat unrelated dirty files as out of scope.

### Task 2: Add A Failing Harness Reproducer

**Files:**
- Create: `tests/test_simplify_path_harness.py`

- [x] Add a subprocess-based unittest that runs `stack/71-simplify-path.py`.
- [x] Assert the script prints prompt sample data plus explicit match status.
- [x] Run the targeted unittest command and verify it fails before the implementation is in place.

### Task 3: Implement The Local Solution Harness

**Files:**
- Modify: `stack/71-simplify-path.py`

- [x] Implement `Solution.simplifyPath` for the canonical Unix path rules.
- [x] Add a `__main__` harness using prompt examples from `stack/71-simplify-path.txt`.
- [x] Re-run the targeted unittest command and verify it passes.

## Review

- Red phase: `python3 -m unittest discover -s tests -p 'test_simplify_path_harness.py' -v` failed before the solution and harness behavior were implemented.
- Green phase: the same unittest command passes after adding the solution logic and match-reporting harness output.
- Manual verification: `python3 stack/71-simplify-path.py` prints the prompt sample inputs, expected canonical paths, actual results, and `Matches expected: True` for each sample.
