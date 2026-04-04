# Maximum Difference Between Node And Ancestor Init Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a solution-free local scaffold for `binary-tree/1026-maximum-difference-between-node-and-ancestor.py` using the repo's LeetCode initializer workflow.

**Architecture:** Create the prompt text and a minimal Python stub first, then run the shared initializer script so it generates the self-contained runner and inline unittest cases from the prompt examples. Finish by verifying the generated file still raises `NotImplementedError` and by refreshing the README metadata for the new problem.

**Tech Stack:** Python 3, `unittest`, Markdown

---

### Task 1: Resolve The Target Problem And Protect Existing Work

**Files:**
- Create: `plans/init-maximum-difference-between-node-and-ancestor.md`
- Inspect: `data/leetcode-problem-catalog.json`
- Inspect: `AGENTS.repo.md`

- [x] Capture initial `git status --short` before editing tracked files.
- [x] Resolve the canonical slug and placement under `binary-tree/`.
- [x] Confirm the task is scaffold-only and must not include solution logic.

### Task 2: Add The Prompt Dump And Stub Pair

**Files:**
- Create: `binary-tree/1026-maximum-difference-between-node-and-ancestor.txt`
- Create: `binary-tree/1026-maximum-difference-between-node-and-ancestor.py`

- [x] Add prompt text with the sample `Example` blocks used as scaffold inputs.
- [x] Add a minimal `Solution.maxAncestorDiff` stub that only raises `NotImplementedError`.
- [x] Keep the file safe for the initializer to rewrite.

### Task 3: Generate And Verify The Local Harness

**Files:**
- Modify: `binary-tree/1026-maximum-difference-between-node-and-ancestor.py`
- Modify: `README.md`

- [x] Run the shared `leetcode-init` script against the new file pair.
- [x] Verify the generated script still leaves the method unimplemented and that `--test` fails for the expected `NotImplementedError` reason.
- [ ] Refresh `README.md` via `python3 scripts/update_readme.py`.

## Review

- `python3 /home/kevin/linux-config/dot_agents/skills/leetcode-init/scripts/init_leetcode_problem.py binary-tree/1026-maximum-difference-between-node-and-ancestor.py` succeeded and generated the self-contained harness.
- `python3 binary-tree/1026-maximum-difference-between-node-and-ancestor.py --test` fails for the expected reason: the scaffolded `Solution.maxAncestorDiff` still raises `NotImplementedError`.
- `python3 binary-tree/1026-maximum-difference-between-node-and-ancestor.py` prints both prompt examples with expected vs actual output and a mismatch diff.
- `python3 scripts/update_readme.py` is still pending because the script needs outbound network access to resolve LeetCode metadata.
