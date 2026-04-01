# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        elif root.left == None: 
            return self.minDepth(root.right) + 1
        elif root.right == None: 
            return self.minDepth(root.left) + 1
        # elif root.left == None and root.right == None:
            # return 0
        return min(self.minDepth(root.left),
                   self.minDepth(root.right)) + 1

if __name__ == "__main__":
    sol = Solution()

    # 1
    # tree = TreeNode(3, 
                    # TreeNode(9), TreeNode(20,
                                          # TreeNode(15),
                                          # TreeNode(7)))

    # only 1 side
    tree = TreeNode(2, None, TreeNode(3, None, TreeNode(4)))

    min_depth = sol.minDepth(tree)
    print(min_depth)
