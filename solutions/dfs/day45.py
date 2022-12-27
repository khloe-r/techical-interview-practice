
"""
Day 45 - Sep 19

Given a binary tree and a target, return whether or not there exists a root to leaf path such that all values along the path sum to the target. 

Ex: Given the following tree…

      1
     / \
    5   2
   /   / \
  1  12   29
and a target of 15, return true as the path 1->2->12 sums to 15.
Ex: Given the following tree…

     104
    /   \
  39     31
 / \    /  \
32  1  9    10
and a target of 175, return true as the path 104->39->32 sums to 175.
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def allPathTree(tree, target, parent):
  if tree == None:
    return
  if tree.left == None and tree.right == None:
    if target == parent + tree.val:
      return True

  parent += tree.val
  if allPathTree(tree.left, target, parent) or allPathTree(tree.right, target, parent):
    return True
  return False

def allPath(tree, target):
  return allPathTree(tree, target, 0)

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(1, BinaryTree(2), BinaryTree(3))
print(allPath(t1, 1))

t1 = BinaryTree(1, BinaryTree(5, BinaryTree(1)), BinaryTree(2, BinaryTree(12), BinaryTree(29)))
print(allPath(t1, 15))

t1 = BinaryTree(104, BinaryTree(39, BinaryTree(32), BinaryTree(1)), BinaryTree(31, BinaryTree(9), BinaryTree(10)))
print(allPath(t1, 175))