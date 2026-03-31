# LeetCode Practice Repository

This repository is a runnable archive of LeetCode solutions grouped by problem family. It is worth reviewing because the work is kept as plain Python scripts instead of notes or screenshots, which makes the author's implementation choices, recursion style, and edge-case handling easy to inspect directly.

## Why This Repo Stands Out

This codebase shows repeated algorithm practice across binary trees, linked lists, dynamic programming, greedy problems, heaps, arrays, strings, and hash maps. For a recruiter or interviewer, that is more useful than a single polished demo because it reveals how the author approaches different data structures under the same lightweight workflow.

The repo also favors executable artifacts over pseudocode. Most solution files are simple scripts, and several include `__main__` harnesses so the approach can be run locally instead of read in isolation.

## Tech Stack And Why Chosen

- Python 3: concise enough for algorithm work and close to the execution model used by LeetCode.
- Plain classes and functions: keeps each solution close to platform-style method signatures without framework overhead.
- Topic-based directories such as `binary-tree/`, `dynamic-programming/`, and `linked-list/`: makes it easy to browse breadth by problem family and compare related solutions.
- Standard-library `unittest`: supports targeted regression checks without adding third-party dependencies to a small practice repo.
- Git and GitHub: preserve a visible history of practice, iteration, and solution-by-solution growth.

## Repo Layout

The repository is organized by category, with one Python file per problem or exercise. Current top-level areas include:

- `array-string/`
- `binary-tree/`
- `divide-and-conquer/`
- `dynamic-programming/`
- `greedy/`
- `hash-map/`
- `heap/`
- `linked-list/`
- `stack/`
- `strings/`
- `tests/`

## Install Or Bootstrap

No package install step is currently required. Clone the repository and use a local Python 3 interpreter.

```bash
git clone git@github.com:Kevin-Mok/leetcode.git
cd leetcode
python3 --version
```

## Day-To-Day Use

Add new solutions under the directory that matches the problem family, or update an existing solution in place. For problems that include an inline harness, run the script directly. For problems with regression coverage in `tests/`, run the targeted unittest command.

Example direct run:

```bash
python3 binary-tree/94-binary-tree-inorder-traversal.py
```

Example targeted regression check:

```bash
python3 -m unittest discover -s tests -p 'test_94_binary_tree_inorder_traversal.py' -v
```

## Command Reference

`python3 <path-to-solution>.py`

- No repo-specific flags are defined for individual solution scripts.
- Swap in the path to the solution you want to run.

`python3 -m unittest discover -s tests -p 'test_94_binary_tree_inorder_traversal.py' -v`

- `-m unittest` runs Python's built-in test runner as a module.
- `discover` tells `unittest` to find matching tests automatically.
- `-s tests` sets the search directory.
- `-p 'test_94_binary_tree_inorder_traversal.py'` limits discovery to the inorder traversal regression file.
- `-v` prints verbose test names and results.

## Recruiter Notes

This repository is not a framework-heavy application, and that is part of the point. It demonstrates disciplined practice in recursion, pointer manipulation, array operations, and incremental verification with minimal tooling, which makes the author's reasoning and coding style easy to audit.
