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
- Give as little hinting as possible by default.
- Prefer the smallest useful nudge over a step-by-step walkthrough.
- Do not give multiple hints at once unless the user explicitly asks for more detail.
- When practical, focus on whether the current approach violates the prompt requirements before suggesting new implementation details.

## README Upkeep

- Every time a problem is solved or added to the repo, refresh the root `README.md` in the same change.
- Use `python3 scripts/update_readme.py` as the source of truth for README updates instead of editing the generated README by hand.
- If a new problem filename cannot be resolved cleanly to a LeetCode problem, add the required metadata to `scripts/readme_problem_overrides.json` before regenerating the README.
