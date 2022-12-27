
"""
Day 44 - Sep 18

Given a binary tree, return a list of strings containing all root to leaf paths. 

Ex: Given the following tree…

   1
 /   \
2     3
return ["1->2", "1->3"]
Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return ["8->2", "8->29->3", "8->29->9"]
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def allPathTree(tree, paths, parent):
  if tree == None:
    return
  if tree.left == None and tree.right == None:
    paths.append(parent + str(tree.val))

  parent += str(tree.val)
  allPathTree(tree.left, paths, parent + "->")
  allPathTree(tree.right, paths, parent + "->")
  return paths

def allPath(tree):
  return allPathTree(tree, [], "")

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(1, BinaryTree(2), BinaryTree(3))
print(allPath(t1))

t1 = BinaryTree(8, BinaryTree(2), BinaryTree(29, BinaryTree(3), BinaryTree(9)))
print(allPath(t1))

t1 = BinaryTree(5, BinaryTree(1), BinaryTree(29, BinaryTree(4), BinaryTree(13, BinaryTree(11, None, BinaryTree(12)))))
print(allPath(t1))