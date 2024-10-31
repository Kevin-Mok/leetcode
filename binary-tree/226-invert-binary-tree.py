# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return None
        elif (root.left == None) and (root.right == None):
            return root
        elif root.left == None:
            # return TreeNode(root.val, root.right, None)
            root.left = root.right
            root.right = None
            # return TreeNode(root.val, root.right, None)
        elif root.right == None:
            root.right = root.left
            root.left = None
            # return TreeNode(root.val, root.left, None)
        else:
            # return TreeNode(root.val, root.right, root.left)
            temp_root = root.right
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(temp_root)
        return root

        # return root
        # return TreeNode(root.val, root.right, root.left)

if __name__ == "__main__":
    sol = Solution()

    # 1
    # tree = TreeNode(4, \
            # TreeNode(2, TreeNode(1), TreeNode(3)), \
            # TreeNode(7, TreeNode(6), TreeNode(9)))

    # 23
    tree = TreeNode(2, TreeNode(3, TreeNode(1)), None)
            # TreeNode(3, None, TreeNode(1)))

    inverted_tree = sol.invertTree(tree)
    print(inverted_tree)
