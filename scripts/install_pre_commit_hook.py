#!/usr/bin/env python3
from pathlib import Path
import stat
import subprocess
import sys


HOOK_BODY = """#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

staged_files="$(git diff --cached --name-only)"
relevant_files="$(printf '%s\n' "$staged_files" | grep -Ev '^(tests/|plans/|tasks/)' || true)"

if ! printf '%s\n' "$relevant_files" | grep -Eq '^(README\\.md|scripts/update_readme\\.py|scripts/readme_problem_overrides\\.json|[^/]+/.*\\.py|[0-9].*\\.py)'; then
  exit 0
fi

python3 scripts/update_readme.py
git add README.md
"""


def main():
    repo_root = Path(__file__).resolve().parents[1]
    git_dir = subprocess.run(
        ["git", "rev-parse", "--git-dir"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    hook_path = (repo_root / git_dir / "hooks" / "pre-commit").resolve()
    hook_path.write_text(HOOK_BODY)
    current_mode = hook_path.stat().st_mode
    hook_path.chmod(current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print(f"Installed pre-commit hook at {hook_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
