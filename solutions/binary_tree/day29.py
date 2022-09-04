"""
Day 29 - Sep 3

Given the reference to the root of a binary search tree and a search value, return the reference to the node that contains the value if it exists and null otherwise. 
Note: all values in the binary search tree will be unique. 

Ex: Given the tree...

        3
       / \
      1   4
and the search value 1 return a reference to the node containing 1.
Ex: Given the following tree...

        7
       / \
      5   9
         / \ 
        8   10
and the search value 9 return a reference to the node containing 9.
Ex: Given the following tree...

        8
       / \
      6   9
and the search value 7 return null.
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def searchBinaryTree(tree, val):
  while tree != None:
    if tree.val == val:
      return tree
    elif tree.val > val:
      tree = tree.left
    else:
      tree = tree.right
  return None

"""
Time Complexity: O(n) where n = height of tree
"""

tree1 = BinaryTree(3, BinaryTree(1), BinaryTree(4))
print(searchBinaryTree(tree1, 1).val)

tree2 = BinaryTree(7, BinaryTree(5), BinaryTree(9, BinaryTree(8), BinaryTree(10)))
print(searchBinaryTree(tree2, 9).val)

tree3 = BinaryTree(8, BinaryTree(6), BinaryTree(9))
print(searchBinaryTree(tree3, 7))
  