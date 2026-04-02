# AGENTS.repo.md

Repo-local Codex addendum for `/home/kevin/coding/leetcode`.

These rules only add stricter local guidance and do not relax higher-precedence instructions.

## LeetCode Local Harnesses

- When a LeetCode solution file can be run locally, add an `if __name__ == "__main__":` block.
- The `__main__` block should exercise the prompt's sample inputs when practical.
- Print the sample input, the actual output, and the expected output so local runs mirror LeetCode's `Run Code` feedback.
- For in-place problems, print the mutated input after calling the solution and the expected mutated value.
- Prefer one or two prompt examples plus simple assertions over large local test scaffolding when the prompt examples already define the behavior clearly.
- Keep the harness self-contained and runnable with the standard library only.

## LeetCode Coaching Style

- For LeetCode problem-solving help in this repo, do not write the full solution by default.
- Only provide a full solution when the user explicitly asks for one in a later prompt.
- Treat requests like `init <problem>`, `set up <problem>`, or similar shorthand as permission to create scaffolding only, not to implement the algorithm.
- If the user's wording is ambiguous about whether they want scaffolding versus a solution, default to no solution and ask a clarifying question instead of implementing logic.
- Distinguish assistant-authored solution code from user-authored solution code. The restriction is on Codex writing or initializing LeetCode solution logic without explicit permission, not on the repository containing user-written solutions.
- Do not block commit plans or commits just because a dirty LeetCode file contains solution logic if the user may have written it. If authorship matters to the decision, ask before treating the file as out of scope.
- Give as little hinting as possible by default.
- If the user asks about a language feature, library API, or utility function for a LeetCode problem, answer that narrow question without adding solution-adjacent hints.
- If the user explicitly says not to give hints related to the solution, do not point toward the repo's implementation or suggest next steps that narrow the algorithmic approach.
- If the user later asks for the efficient solution directly, provide it plainly without scaffolding, intermediate hints, or references to the repo's actual solution file.
- Prefer the smallest useful nudge over a step-by-step walkthrough.
- Do not give multiple hints at once unless the user explicitly asks for more detail.
- When practical, focus on whether the current approach violates the prompt requirements before suggesting new implementation details.

## README Upkeep

- Every time a problem is solved or added to the repo, refresh the root `README.md` in the same change.
- Use `python3 scripts/update_readme.py` as the source of truth for README updates instead of editing the generated README by hand.
- If a new problem filename cannot be resolved cleanly to a LeetCode problem, add the required metadata to `scripts/readme_problem_overrides.json` before regenerating the README.
