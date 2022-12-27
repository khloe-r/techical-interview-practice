
"""
Day 43 - Sep 17

Given a binary tree, return its maximum depth. 
Note: the maximum depth is defined as the number of nodes along the longest path from root node to leaf node. 

Ex: Given the following tree…

    9
   / \
  1   2
return 2
Ex: Given the following tree…

    5
   / \
  1  29
    /  \
   4   13
return 3
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def maxDepthTree(tree, level):
  if tree == None:
    return level
  return max(level, maxDepthTree(tree.right, level + 1), maxDepthTree(tree.left, level + 1))

def maxDepth(tree):
  return maxDepthTree(tree, 0)

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(9, BinaryTree(1), BinaryTree(2))
print(maxDepth(t1))

t1 = BinaryTree(5, BinaryTree(1), BinaryTree(29, BinaryTree(4), BinaryTree(13)))
print(maxDepth(t1))

t1 = BinaryTree(5, BinaryTree(1), BinaryTree(29, BinaryTree(4), BinaryTree(13, BinaryTree(11, None, BinaryTree(12)))))
print(maxDepth(t1))