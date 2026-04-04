# Add Node-Child Difference Variant Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a custom binary-tree problem for maximum difference between a node and its immediate child while preserving the current 1026 solution attempt unchanged.

**Architecture:** Copy the existing 1026 scaffold into a new binary-tree problem with corrected prompt text, example expectations, and docstrings that match the narrower parent-child problem. Update the README generator to support explicitly custom local problem metadata so the new tracked file does not break repository metadata refreshes.

**Tech Stack:** Python 3, `unittest`, Markdown, existing README generator

---

### Task 1: Add The Custom Problem Variant

**Files:**
- Create: `binary-tree/maximum-difference-between-node-and-child.py`
- Create: `binary-tree/maximum-difference-between-node-and-child.txt`

- [ ] Copy the current `1026` Python scaffold into the new problem file.
- [ ] Rewrite the new prompt text and solution docstring so they describe immediate parent-child differences instead of ancestor-descendant differences.
- [ ] Replace the generated example expectations with cases that match the current algorithm exactly.

### Task 2: Keep Repository Metadata Safe

**Files:**
- Modify: `scripts/update_readme.py`
- Modify: `tests/test_update_readme.py`
- Modify: `scripts/readme_problem_overrides.json`

- [ ] Add support for fully local custom README metadata from overrides without requiring LeetCode lookup.
- [ ] Register the new custom problem in the overrides file.
- [ ] Add regression coverage proving custom entries are accepted.

### Task 3: Verify Both Problem Files

**Files:**
- Verify: `binary-tree/1026-maximum-difference-between-node-and-ancestor.py`
- Verify: `binary-tree/maximum-difference-between-node-and-child.py`

- [ ] Run the new custom problem harness and confirm its examples pass.
- [ ] Run the original 1026 harness and confirm it still reflects the same current solution behavior.
- [ ] Review `git diff --stat` to confirm the change stayed focused.
