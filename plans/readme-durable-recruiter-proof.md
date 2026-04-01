# README Durability And Recruiter Proof Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the generated root README more durable and more technical by explicitly explaining the data-structure coverage it demonstrates and the generator workflow that keeps its claims current.

**Architecture:** Extend the existing README generator instead of hand-editing `README.md`. Add rendering coverage in `tests/test_update_readme.py`, update the generated opening and stack rationale in `scripts/update_readme.py`, regenerate `README.md`, and verify the generated output plus the targeted test suite.

**Tech Stack:** Python 3, standard-library `unittest`, generated Markdown README

---

### Task 1: Lock scope and capture the README contract

**Files:**
- Create: `plans/readme-durable-recruiter-proof.md`
- Inspect: `README.md`
- Inspect: `scripts/update_readme.py`
- Inspect: `tests/test_update_readme.py`

- [x] Step 1: Capture `git status --short` before editing tracked files.
- [x] Step 2: Inspect current README generator diffs and preserve in-flight edits already on this branch.
- [x] Step 3: Confirm the change belongs in the generator and tests, not only in generated output.

### Task 2: Add technical recruiter-proof copy at the generator level

**Files:**
- Modify: `scripts/update_readme.py`
- Modify: `tests/test_update_readme.py`

- [x] Step 1: Add test expectations for stronger technical explanation of recruiter proof and data-structure coverage.
- [x] Step 2: Update the generated README opening and stack section so they explain arrays, linked lists, trees, stacks, heaps, hash maps, dynamic programming, and the generator workflow.
- [x] Step 3: Keep the recruiter-first hierarchy intact without reintroducing scattered recruiter sections.

### Task 3: Regenerate and verify

**Files:**
- Modify: `README.md`
- Modify: `plans/readme-durable-recruiter-proof.md`

- [x] Step 1: Regenerate `README.md` from `scripts/update_readme.py`.
- [x] Step 2: Run `python3 -m unittest tests.test_update_readme -v`.
- [x] Step 3: Run `python3 scripts/update_readme.py --check`.
- [x] Step 4: Mark the plan complete and record verification results.

## Review

- Updated the README generator so the opening hook explicitly calls out the data-structure and algorithm categories that make the repo useful as recruiter proof.
- Added generated proof-surface bullets and two durability metrics: runnable harness count and detected regression-coverage count.
- Regenerated `README.md` from the generator instead of hand-editing the generated file, keeping the repo on the durable path.

### Verification

- `python3 -m unittest tests.test_update_readme -v`
- `python3 scripts/update_readme.py`
- `python3 scripts/update_readme.py --check`
