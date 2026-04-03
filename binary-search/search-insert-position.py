from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target <= nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return left

if __name__ == "__main__":
    sol = Solution()
    samples = [
        # ([1, 3, 5, 6], 5, 2),
        # ([1, 3, 5, 6], 2, 1),
        # ([1, 3, 5, 6], 7, 4),
        # Finishes by matching exactly: right (27), left (71), right (44), then match at 58.
        ([2, 5, 9, 14, 20, 27, 35, 44, 58, 71, 86, 103], 58, 8),
        # Finishes by exhausting the loop and returning left = 4.
        ([2, 5, 9, 14, 20, 27, 35, 44, 58, 71, 86, 103], 18, 4),
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
