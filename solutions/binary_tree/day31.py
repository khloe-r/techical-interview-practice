"""
Day 31 - Sep 14

Given a binary search tree that contains unique values and two nodes within the tree, a, and b, return their lowest common ancestor. 
Note: the lowest common ancestor of two nodes is the deepest node within the tree such that both nodes are descendants of it.

Ex: Given the following tree...
       7
      / \
    2    9
   / \ 
  1   5 
and a = 1, b = 9, return a reference to the node containing 7.
Ex: Given the following tree...

        8
       / \
      3   9
     / \ 
    2   6
and a = 2, b = 6, return a reference to the node containing 3.
Ex: Given the following tree...

        8
       / \
      6   9
and a = 6, b = 8, return a reference to the node containing 8.
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def lowestCommonAncestorv2(tree, a, b):
  if tree != None:
    mid = tree.val == a or tree.val == b
    left = lowestCommonAncestor(tree.left, a, b)
    right = lowestCommonAncestor(tree.right, a, b)
    if (mid and left) or (mid and right) or (left and right):
      return tree
    else:
      return mid or left or right

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

tree = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9))
lst = lowestCommonAncestor(tree, 1, 9)
print(lst.val)

tree3 = BinaryTree(8, BinaryTree(3, BinaryTree(2), BinaryTree(6)), BinaryTree(9))
lst = lowestCommonAncestor(tree3, 6, 2)
print(lst.val)

tree2 = BinaryTree(8, BinaryTree(6), BinaryTree(9))
lst = lowestCommonAncestor(tree2, 6, 8)
print(lst.val)