"""
Day 49 - Sep 23

Given a binary tree, return the sum of all left leaves of the tree. Ex: Given the following tree…

    5
   / \
  2   12
     /  \
    3    8
return 5 (i.e. 2 + 3)
Ex: Given the following tree…

       2
      / \
    4    2
   / \ 
  3   9 
return 3
"""


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPathTree(tree, leaves, left):
  if tree == None:
    return

  if tree.left == None and tree.right == None and left:
    leaves.append(tree.val)

  if tree.left:
    allPathTree(tree.left, leaves, True)
  if tree.right:
    allPathTree(tree.right, leaves, False)

  return leaves

def allPath(tree):
    return sum(allPathTree(tree, [], True))

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(1, BinaryTree(1), BinaryTree(3))
print(allPath(t1))

t1 = BinaryTree(5, BinaryTree(2),
                   BinaryTree(12, BinaryTree(3), BinaryTree(8)))
print(allPath(t1))

t1 = BinaryTree(2, BinaryTree(4, BinaryTree(3), BinaryTree(9)),
                   BinaryTree(2))
print(allPath(t1))
