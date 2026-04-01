from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [0] * len(nums)
        i = 0
        j = k = len(nums) - 1
        while i <= j:
            left_squared = nums[i] ** 2
            right_squared = nums[j] ** 2
            if left_squared >= right_squared:
                squared[k] = left_squared
                i += 1
            else:
                squared[k] = right_squared
                j -= 1
            k -= 1
            # squared += [nums[i] ** 2]
        return squared


if __name__ == "__main__":
    sol = Solution()
    samples = [
        # ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ]

    for nums, expected in samples:
        print("Input:", nums)
        print("Expected:", expected)
        try:
            actual = sol.sortedSquares(nums)
            print("Actual:", actual)
            print("Matches expected:", actual == expected)
        except NotImplementedError as exc:
            print("Actual: not implemented")
            print("Matches expected: False")
            print("Note:", exc)
        print()
