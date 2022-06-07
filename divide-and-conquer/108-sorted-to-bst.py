from math import floor

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}\n{self.left}\n{self.right}"

class Solution:
    """
    find midpoint
    create BST for L/R
    combine tree with midpoint
    """
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid_index = len(nums) // 2
        #  print(len(nums), mid_index)
        return TreeNode(nums[mid_index], 
                self.sortedArrayToBST(nums[:mid_index]),
                self.sortedArrayToBST(nums[mid_index + 1:]))

#  if __name__ == "__main__":
    #  solution = Solution()
    #  print(solution.sortedArrayToBST([-10,-3,0,5,9]))
