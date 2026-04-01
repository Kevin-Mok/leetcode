# Automated README Generator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate a recruiter-focused root README from tracked LeetCode solutions, with official difficulty lookups and an optional pre-commit hook that keeps the README current when problems are solved.

**Architecture:** Add a standard-library Python generator that inspects tracked solution files, resolves LeetCode metadata from the official GraphQL endpoint plus a small override file, and fully renders `README.md`. Back it with deterministic unit tests and an installer for a local `pre-commit` hook that reruns the generator when solution files change.

**Tech Stack:** Python 3, `unittest`, JSON, Markdown, Git, LeetCode GraphQL

---

### Task 1: Lock The Work Surface

**Files:**
- Create: `plans/automated-readme-generator.md`
- Inspect: `README.md`
- Inspect: `AGENTS.repo.md`

- [x] Capture `git status --short` before editing tracked files.
- [x] Confirm unrelated dirty files and leave them untouched.
- [x] Confirm the current README and repo guidance that the generator will replace or extend.

### Task 2: Add Failing Generator Tests

**Files:**
- Create: `tests/test_update_readme.py`

- [ ] Add unit tests for exact ID lookup, slug lookup, override lookup, and fail-closed behavior.
- [ ] Add rendering tests for difficulty ordering, notable-problem selection, and README section presence.
- [ ] Add `--check` style behavior coverage so the script can be used in automation.
- [ ] Run the targeted test file first and confirm it fails until the implementation exists.

### Task 3: Implement Metadata Resolution And Rendering

**Files:**
- Create: `scripts/update_readme.py`
- Create: `scripts/readme_problem_overrides.json`

- [ ] Implement tracked-file discovery from `git ls-files`.
- [ ] Implement metadata resolution against the LeetCode GraphQL API with override support.
- [ ] Implement deterministic README rendering grouped by `Hard`, `Medium`, then `Easy`.
- [ ] Implement notable-problem ranking and the recruiter-focused summary sections.

### Task 4: Add Hook Support And Repo Guidance

**Files:**
- Create: `scripts/install_pre_commit_hook.py`
- Modify: `AGENTS.repo.md`

- [ ] Install a local `pre-commit` hook that reruns the README generator only when relevant files are staged.
- [ ] Stage `README.md` from the hook after regeneration.
- [ ] Update repo guidance so newly solved problems must refresh the README in the same change.

### Task 5: Regenerate And Verify

**Files:**
- Modify: `README.md`

- [ ] Generate the new README from the script.
- [ ] Run `python3 -m unittest discover -s tests -p 'test_update_readme.py' -v`.
- [ ] Run `python3 scripts/update_readme.py --check`.
- [ ] Run `python3 -m unittest discover -s tests -v`.
- [ ] Review the generated README for truthful counts, difficulty grouping, and recruiter-first hierarchy.
