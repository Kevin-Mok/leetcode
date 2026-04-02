from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        index = 0
        mid = (i + j) // 2
        while (((nums[i] < target) or (nums[j] > target))
               and i < j):
            mid = (i + j) // 2
            # Hint: binary search decisions usually come from nums[mid],
            # not from comparing only nums[i] and nums[j].
            if ((target == nums[i]) or
                    ((target >= nums[i - 1]) and
                     (target <= nums[i]))):
                # Hint: watch nums[i - 1] when i == 0.
                return i
            elif target == nums[j]:
                # Hint: if target exactly matches the right endpoint,
                # double-check whether returning j - 1 makes sense.
                return j - 1
            elif target < nums[j]:
                # Hint: for a sorted array, ask whether this branch should
                # move the left bound or the right bound. The window should
                # shrink around mid every iteration.
                i = mid
            elif target > nums[i]:
                # Hint: compare target with nums[mid] and update bounds from
                # that result: target > nums[mid] moves left up, target <
                # nums[mid] moves right down.
                j = mid
        return j


if __name__ == "__main__":
    sol = Solution()
    samples = [
        # ([1, 3, 5, 6], 5, 2),
        # ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ]

    for nums, target, expected in samples:
        print(f"Input: nums = {nums}, target = {target}")
        print("Expected:", expected)
        try:
            actual = sol.searchInsert(nums, target)
            print("Actual:", actual)
            print("Matches expected:", actual == expected)
        except NotImplementedError as exc:
            print("Actual: not implemented")
            print("Matches expected: False")
            print("Note:", exc)
        print()
