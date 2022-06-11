# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
   def __str__(self):
       #  print(self.val)
       #  if self.left is not None:
           #  print(self.left)
       #  if self.right is not None:
           #  print(self.right)
        return f"{self.val} [{self.left}] [{self.right}]"

class Solution:
    def allPossibleFBT(self, n: int) -> list[[TreeNode]]:
        #  possible_trees = [[] * n]
        possible_trees = []
        for i in range(n + 1):
            possible_trees.append([])
        print(possible_trees)
        for i in range(n + 1):
            if i % 2 == 0:
                continue
            elif i == 1:
                possible_trees[i].append(TreeNode(0))
            elif i == 3:
                possible_trees[i].append(TreeNode(0, 0, 0))
            else:
                print(i)
                for left_tree in possible_trees[i - 2]:
                    for right_tree in possible_trees[i - 4]:
                        print(left_tree, right_tree)
                        #  print(left_tree)
                        #  print(right_tree)
                        possible_trees[i].append(TreeNode(0,
                            left_tree, right_tree))
                print()
                for left_tree in possible_trees[i - 4]:
                    for right_tree in possible_trees[i - 2]:
                        print(left_tree, right_tree)
                        possible_trees[i].append(TreeNode(0,
                            left_tree, right_tree))
                print()
        return possible_trees[n]

if __name__ == "__main__":
    sol = Solution()
    #  print(sol.allPossibleFBT(7))
    print(len(sol.allPossibleFBT(7)))
    #  print(len(sol.allPossibleFBT(5)))
