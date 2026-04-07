# Minimum Cost To Connect Sticks Init Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a scaffold-only LeetCode harness for `heap/1167-minimum-cost-to-connect-sticks.py` using the prompt examples as executable local tests without implementing the algorithm.

**Architecture:** Save the prompt text as a same-name `.txt` file, add a matching `.py` stub with an unimplemented `Solution.connectSticks`, then run the repo's initializer script so the final problem file contains a self-contained local runner and inline unittest coverage generated from the prompt examples.

**Tech Stack:** Python 3, `unittest`, Markdown

---

### Task 1: Confirm Scope And Protect Existing Work

**Files:**
- Create: `plans/init-minimum-cost-to-connect-sticks.md`
- Create: `heap/1167-minimum-cost-to-connect-sticks.py`
- Create: `heap/1167-minimum-cost-to-connect-sticks.txt`

- [x] Capture initial `git status --short` before editing tracked files.
- [x] Confirm there is no existing same-name `.py` and `.txt` pair for this problem.
- [x] Treat unrelated dirty files as out of scope.

### Task 2: Create The Scaffold Inputs

**Files:**
- Create: `heap/1167-minimum-cost-to-connect-sticks.py`
- Create: `heap/1167-minimum-cost-to-connect-sticks.txt`

- [x] Save the prompt text locally as the source of truth for examples.
- [x] Add a placeholder `Solution.connectSticks` stub with no algorithm implementation.

### Task 3: Generate The Local Harness

**Files:**
- Modify: `heap/1167-minimum-cost-to-connect-sticks.py`

- [x] Run the bundled LeetCode initializer script against the new pair.
- [x] Review the generated file and confirm the solution method remains unimplemented.
- [x] Verify the generated `__main__` harness uses the prompt examples.

### Task 4: Refresh Generated Docs And Verify

**Files:**
- Modify: `README.md`

- [x] Regenerate `README.md` with `python3 scripts/update_readme.py`.
- [x] Run `python3 heap/1167-minimum-cost-to-connect-sticks.py`.
- [x] Run `python3 heap/1167-minimum-cost-to-connect-sticks.py --test`.

## Review

- `python3 ~/linux-config/dot_agents/skills/leetcode-init/scripts/init_leetcode_problem.py heap/1167-minimum-cost-to-connect-sticks.py` generated a self-contained harness from the prompt examples.
- The generated `heap/1167-minimum-cost-to-connect-sticks.py` still leaves `Solution.connectSticks` unimplemented via `NotImplementedError`.
- `python3 heap/1167-minimum-cost-to-connect-sticks.py` prints each prompt example, the expected output, and a clear not-implemented diff.
- `python3 heap/1167-minimum-cost-to-connect-sticks.py --test` fails for the expected reason: the solution is still unimplemented.
- `python3 scripts/update_readme.py` completed, but `README.md` did not change because the generator indexes tracked solution files and this new problem is currently untracked.
