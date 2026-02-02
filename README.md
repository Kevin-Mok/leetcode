# LeetCode Solutions

A collection of algorithmic problem solutions demonstrating proficiency in data structures, algorithms, and problem-solving techniques.

![Python](https://img.shields.io/badge/Python-100%25-blue)
![Problems](https://img.shields.io/badge/Problems-14-green)
![Categories](https://img.shields.io/badge/Categories-9-orange)

## Problem Categories

| Category | Problems | Key Concepts |
|----------|----------|--------------|
| **Dynamic Programming** | 300, 322, 894 | Memoization, 2D DP, combinatorial DP |
| **Binary Tree** | 108, 226 | BST construction, tree traversal, recursion |
| **Linked List** | 21, Remove Duplicates | Two-pointer, merge operations |
| **Stack** | 20 | Bracket matching, LIFO operations |
| **Array & String** | 88 | Two-pointer merge, in-place modification |
| **Hash Map** | 383 | Frequency counting, character mapping |
| **Heap** | Various | Priority queue operations |
| **Divide and Conquer** | 108 | Recursive subdivision |
| **Greedy** | 2160 | Optimal local choices |

## Notable Solutions

### Hard
- **894 - All Possible Full Binary Trees**: Complex combinatorial recursion generating all structurally unique full binary trees

### Medium
- **300 - Longest Increasing Subsequence**: Classic DP with O(n²) solution
- **322 - Coin Change**: 2D dynamic programming for minimum coin combination
- **108 - Convert Sorted Array to BST**: Divide and conquer tree construction

### Easy (Foundation)
- **20 - Valid Parentheses**: Stack-based bracket validation
- **21 - Merge Two Sorted Lists**: Linked list manipulation
- **226 - Invert Binary Tree**: Recursive tree transformation

## Repository Structure

```
leetcode/
├── array-and-string/
│   └── 88-merge.py
├── binary-tree/
│   ├── 108-sorted-to-bst.py
│   └── 226-invert-tree.py
├── divide-and-conquer/
├── dynamic-programming/
│   ├── 300-longest-inc-subseq.py
│   ├── 322-coin-change.py
│   └── 894-full-binary-trees.py
├── greedy/
├── hash-map/
├── heap/
├── linked-list/
└── stack/
    └── 20-valid-parens.py
```

## Code Style

Each solution includes:
- Clear variable naming
- Inline comments explaining logic
- Test cases in `__main__` section
- Multiple approach explorations where applicable

## Why This Repository is Interesting

### Demonstrates Core CS Fundamentals
- **Algorithmic Breadth**: Covers 9 major algorithm paradigms
- **Problem Complexity Range**: From easy warm-ups to hard combinatorial challenges
- **Classic Interview Problems**: Includes canonical questions frequently asked in technical interviews

### Shows Learning Progression
- Git history reveals iterative problem-solving approach
- Solutions evolve from initial attempts to optimized versions
- Edge case handling demonstrates thoroughness

### Technical Skills Showcased
- **Data Structures**: Trees, linked lists, stacks, heaps, hash maps
- **Algorithm Design**: DP, divide & conquer, greedy, two-pointer
- **Python Proficiency**: Clean, idiomatic Python code
- **Problem Decomposition**: Breaking complex problems into manageable parts

## Running Solutions

```bash
# Run any solution
python dynamic-programming/322-coin-change.py

# Each file includes test cases
python stack/20-valid-parens.py
```

## Author

[Kevin Mok](https://github.com/Kevin-Mok)
