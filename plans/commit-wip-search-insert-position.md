# ExecPlan: Commit WIP Search Insert Position

## Goal

Create a local git worktree for the current `search-insert-position` problem and capture the finished local solution state in a clearly labeled commit.

## Assumptions

1. The user wants an isolated worktree for this problem and explicitly requested a new worktree.
2. The current solution file is complete and should be committed alongside the workflow artifacts that explain the setup.
3. The commit should stay scoped to the worktree setup, the problem file, the README refresh, and any required repo-maintenance files for this workflow.

## Steps

- [x] Inspect repo state, worktree prerequisites, and README gate inputs.
- [x] Add the local worktree ignore rule and create this ExecPlan.
- [ ] Create a local worktree on a dedicated branch for `search-insert-position`.
- [ ] Run the README gate and regenerate `README.md` if required by the repo rules.
- [ ] Commit the scoped solution changes with a Conventional Commit message that reflects the finished problem state.
- [ ] Push the branch if the workflow remains a single-commit flow and no repo conflict blocks it.

## Review

Search-insert-position is finished locally and passes the sample harness. The remaining work is to refresh the README gate output and commit the scoped changes.
