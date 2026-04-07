# Lessons

2026-03-31 - When the user asks why their LeetCode code is not working, respond with a small hint and avoid changing their solution unless they explicitly ask for a fix.
2026-04-01 - In this repo, do not write LeetCode solution logic. If the user asks for help on a problem, limit changes to scaffolding such as a `__main__` harness or provide hints without implementing the algorithm.
2026-04-01 - In this repo, keep LeetCode hints minimal. Prefer the smallest useful nudge over a full explanation unless the user asks for more detail.
2026-04-01 - When initializing a new LeetCode problem in this repo, check for a same-name `.txt` file first and use it as the source for local test cases when present.
2026-04-01 - When the user reports a LeetCode error, explain the cause without solving the algorithm. Only state whether the issue is a placeholder/stub that still needs implementation versus a repo-side harness problem.
2026-04-01 - In this repo, never give a LeetCode solution unless the user explicitly asks for one. Default to the smallest useful hint only, and avoid strong solution direction unless they ask for more.
2026-04-01 - In this repo, when the user asks whether a language feature or helper like `split` is allowed, answer only that narrow question and do not add stack, parsing, or algorithm guidance unless they explicitly ask for it.
2026-04-02 - In this repo, never implement or initialize LeetCode solution logic unless the user explicitly asks for the solution. Treat requests like "init <problem>" as scaffold-only, not permission to solve the problem.
2026-04-02 - In this repo, the no-solution rule applies to Codex writing solution logic without explicit permission, not to user-authored solution code already present in the worktree. If commit decisions depend on authorship, ask instead of assuming.
2026-04-03 - In this repo, prompts like "am I close?", "is this right?", or "what am I missing?" are evaluation requests, not permission to provide the answer. Respond with a minimal nudge or issue callout unless the user explicitly asks for the solution.
2026-04-03 - In this repo, when the user asks for LeetCode help on an existing solution file, put the hint into inline `Hint:` comments in the file when practical instead of relying only on chat.
2026-04-03 - In this repo, refresh inline LeetCode `Hint:` comments when the user asks for help again, and delete stale or superseded hints instead of stacking them.
2026-04-03 - When manually editing files in this repo, use the dedicated `apply_patch` tool directly instead of invoking it through `exec_command`.
2026-04-03 - In this repo, when committing a LeetCode solution, include the raw problem text file that captures the prompt examples and expected outputs in the same commit scope.
2026-04-03 - In this repo, when the user asks for additional examples in a harness, preserve the existing examples by commenting them out instead of deleting them.
2026-04-03 - In this repo, when the user asks for a LeetCode hint, give only the next minimal hint. Do not include a broader explanation or multiple steps unless they explicitly ask for more.
2026-04-03 - In this repo, when the user asks only for a LeetCode problem's difficulty, answer with just the difficulty and avoid any solution direction or hinting.
2026-04-04 - When pushing from this repo, push to the upstream branch with the same name as the local branch and set upstream during the push if it is missing.
2026-04-05 - In this repo, when the user asks for hints on their LeetCode helper, do not add new tests or attempt a fix unless they explicitly ask for code changes.
2026-04-07 - In this repo, when the user asks a conceptual LeetCode question like whether helpers are needed, do not reveal the replacement algorithm or traversal strategy unless they explicitly ask for the solution.
