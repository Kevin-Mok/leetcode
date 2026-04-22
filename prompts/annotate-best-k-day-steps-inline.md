Annotate the existing `best_k_day_steps` function with short inline teaching comments for explanation purposes.

Context:
- File: `sliding-window/1-best-k-day-step-streak.py`
- Function:

```python
def best_k_day_steps(steps: list[int], k: int) -> int | None:
    """Return the best fixed-size window sum for the provided inputs."""
    if k <= 0 or k > len(steps):
        return None

    left = 0
    right = k - 1
    cur_total_steps = sum(steps[left:right + 1])
    best_total_steps = cur_total_steps
    while right < len(steps) - 1:
        cur_total_steps -= steps[left]
        left += 1
        right += 1
        cur_total_steps += steps[right]
        best_total_steps = max(best_total_steps,
                               cur_total_steps)
    return best_total_steps
```

What I want:
- Add concise inline comments directly inside the function.
- Keep the algorithm and output exactly the same.
- Do not rewrite it into a different style unless absolutely necessary.
- Use the comments to teach the fixed-size sliding window concept.

Please make the comments explain:
- Why the early return handles important edge cases:
  - `k <= 0`
  - `k > len(steps)`
- Why `right` starts at `k - 1` instead of `k`
- Why the initial sum uses `steps[left:right + 1]`
- Why the loop condition is `while right < len(steps) - 1`
- The exact order of operations when the window slides:
  - subtract the outgoing left value
  - move `left`
  - move `right`
  - add the incoming right value
- How that order helps avoid off-by-one mistakes
- Why `best_total_steps` starts as the first full window
- That this is a fixed-size window, not a variable-size one

Tone and style:
- Make the comments beginner-friendly but not verbose
- Highlight common off-by-one pitfalls
- Mention boundary reasoning where it helps
- Keep comments focused on understanding, not restating obvious syntax

Output requirements:
- Return only the updated function
- Preserve valid Python formatting
- Keep comments short enough that the code still feels clean
