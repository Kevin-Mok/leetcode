# Sliding-Window Student Scaffolds Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add student-facing sliding-window Python scaffold files with runnable example/test harnesses, without including solutions.

**Architecture:** Each problem lives in a self-contained Python script under `sliding-window/` with a function stub, example runner, and inline `unittest` coverage. The README generator excludes these files so they do not appear as solved LeetCode entries.

**Tech Stack:** Python 3, standard-library `unittest`

---

### Task 1: Exclude student scaffolds from README solved-problem discovery

**Files:**
- Modify: `scripts/update_readme.py`

- [x] Add `sliding-window/` to the excluded prefixes used by solution discovery.
- [x] Keep the change path-based so the practice scaffolds remain outside solved counts without needing metadata.

### Task 2: Add self-contained student scaffold scripts

**Files:**
- Create: `sliding-window/best-k-day-step-streak.py`
- Create: `sliding-window/shortest-study-sprint.py`
- Create: `sliding-window/longest-club-code-with-limited-symbols.py`
- Create: `sliding-window/smallest-announcement-clip.py`

- [x] Add a student-facing function stub to each file that raises `NotImplementedError`.
- [x] Add example fixtures and broader correctness fixtures for boundary conditions, invalid inputs, and tricky cases.
- [x] Add `run_examples()` output that reports not-implemented status clearly.
- [x] Add inline `unittest` coverage behind `--test`.

### Task 3: Keep the scaffolds instructional and solution-free

**Files:**
- Create: `sliding-window/best-k-day-step-streak.py`
- Create: `sliding-window/shortest-study-sprint.py`
- Create: `sliding-window/longest-club-code-with-limited-symbols.py`
- Create: `sliding-window/smallest-announcement-clip.py`

- [x] Use problem statements and fixtures derived from the sliding-window lesson data.
- [x] Do not include any reference implementation, brute-force oracle, or hidden solution helper.
- [x] Make failing tests communicate that the student still needs to implement the function.
