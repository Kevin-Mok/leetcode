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
    #  def allPossibleFBT(self, n: int) -> list[[TreeNode]]:
        #  #  possible_trees = [[] * n]
        #  possible_trees = []
        #  for i in range(n + 1):
            #  possible_trees.append([])
        #  print(possible_trees)
        #  for i in range(n + 1):
            #  if i % 2 == 0:
                #  continue
            #  elif i == 1:
                #  possible_trees[i].append(TreeNode(0))
            #  elif i == 3:
                #  possible_trees[i].append(TreeNode(0, 0, 0))
            #  else:
                #  #  print(i)
                #  #  for left_tree in possible_trees[i - 2]:
                    #  #  for right_tree in possible_trees[i - 4]:
                        #  #  print(left_tree, right_tree)
                        #  #  #  print(left_tree)
                        #  #  #  print(right_tree)
                        #  #  possible_trees[i].append(TreeNode(0,
                            #  #  left_tree, right_tree))
                #  #  print()
                #  #  for left_tree in possible_trees[i - 4]:
                    #  #  for right_tree in possible_trees[i - 2]:
                        #  #  print(left_tree, right_tree)
                        #  #  possible_trees[i].append(TreeNode(0,
                            #  #  left_tree, right_tree))
                #  #  print()
        #  return possible_trees[n]

    def allPossibleFBT(self, n: int) -> list[[TreeNode]]:
        #  possible_trees = [[] * n]
        possible_trees = []
        for i in range(n + 1):
            possible_trees.append([])
        #  print(possible_trees)
        for i in range(n + 1):
            if i % 2 == 0:
                continue
            elif i == 1:
                possible_trees[i].append(TreeNode(0))
            else:
                left_counter = 1
                right_counter = i - 2
                while left_counter <= right_counter:
                    #  print(i, left_counter, right_counter)
                    for left_tree in possible_trees[left_counter]:
                        for right_tree in possible_trees[right_counter]:
                            #  print(left_tree, right_tree)
                            #  print(left_tree)
                            #  print(right_tree)
                            possible_trees[i].append(TreeNode(0,
                                left_tree, right_tree))
                    #  print()
                    if left_counter != right_counter:
                        for left_tree in possible_trees[right_counter]:
                            for right_tree in possible_trees[left_counter]:
                                #  print(left_tree, right_tree)
                                possible_trees[i].append(TreeNode(0,
                                    left_tree, right_tree))
                    #  print()
                    left_counter += 2
                    right_counter -= 2
        return possible_trees[n]

if __name__ == "__main__":
    sol = Solution()
    #  print(sol.allPossibleFBT(7))
    print(len(sol.allPossibleFBT(7)))
    #  print(len(sol.allPossibleFBT(5)))
    #  print(len(sol.allPossibleFBT(3)))
