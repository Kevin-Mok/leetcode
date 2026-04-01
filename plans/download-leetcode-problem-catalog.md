# LeetCode Problem Catalog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a repo-local artifact containing LeetCode problem numbers and names, plus a small script to refresh it from LeetCode.

**Architecture:** Reuse the repo's existing LeetCode HTTP pattern instead of adding a new dependency. Add one script that fetches the current problem list, normalizes number and title fields into a stable JSON file, and document the command in the generated README.

**Tech Stack:** Python 3 standard library, `unittest`, generated `README.md`

---

### Task 1: Define the catalog contract with tests

**Files:**
- Create: `tests/test_download_problem_catalog.py`
- Modify: `scripts/download_problem_catalog.py`

- [x] Step 1: Write a failing test for parsing the LeetCode problem payload into sorted `{frontend_id, title}` records.
- [x] Step 2: Run `python3 -m unittest tests.test_download_problem_catalog -v` and verify it fails for the expected missing-module reason.
- [x] Step 3: Implement the minimal parsing and file-writing helpers in `scripts/download_problem_catalog.py`.
- [x] Step 4: Re-run `python3 -m unittest tests.test_download_problem_catalog -v` and verify it passes.

### Task 2: Generate the local catalog artifact

**Files:**
- Create: `data/leetcode-problem-catalog.json`
- Modify: `scripts/download_problem_catalog.py`

- [x] Step 1: Run the refresh script against LeetCode and write the catalog JSON file.
- [x] Step 2: Verify the output file contains number and title entries and is sorted by problem number.

### Task 3: Document the workflow

**Files:**
- Modify: `README.md`
- Modify: `plans/download-leetcode-problem-catalog.md`

- [x] Step 1: Update the README generator inputs or generated README content so the new command and artifact are discoverable.
- [x] Step 2: Regenerate `README.md`.
- [x] Step 3: Mark this plan complete and add a short review note with verification commands.

## Review

- Added `scripts/download_problem_catalog.py` plus `tests/test_download_problem_catalog.py` to fetch and validate a repo-local LeetCode catalog.
- Generated `data/leetcode-problem-catalog.json` with 3,888 `{frontend_id, title, title_slug}` entries sorted by `frontend_id`.
- Updated the generated README workflow so `README.md` documents the catalog artifact and refresh command.

### Verification

- `python3 -m unittest tests.test_download_problem_catalog -v`
- `python3 -m unittest tests.test_update_readme.RenderReadmeTests -v`
- `python3 scripts/download_problem_catalog.py`
- `python3 scripts/update_readme.py`
- `python3 scripts/update_readme.py --check`
- `python3 -m unittest discover -s tests -v`
