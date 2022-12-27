"""
Day 48 - Sep 22

Given two binary trees, return whether or not both trees have the same leaf sequence. Two trees have the same leaf sequence if both trees’ leaves read the same from left to right. 

Ex: Given the following trees…

   1
 /   \
1     3
and


   7
 /   \
1     2
return false as both the trees' leaves don't read the same from left to right (i.e. [1, 3] and [1, 2]).
Ex: Given the following trees…

    8
   / \
  2   29
    /  \
   3    9
and

    8
   / \
  2  29
 /   /  \
2   3    9
     \
      3
return true as both the trees' leaves read the same from left to right (i.e. [2, 3, 9] and [2, 3, 9]).
"""


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPathTree(tree, leaves):
  if tree == None:
    return
  if tree.left == None and tree.right == None:
    leaves.append(tree.val)
    return

  if tree.left:
    allPathTree(tree.left, leaves)
  if tree.right:
    allPathTree(tree.right, leaves)

  return leaves

def allPath(tree1, tree2):
    arr1 = allPathTree(tree1, [])
    arr2 = allPathTree(tree2, [])
    return arr1 == arr2

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(1, BinaryTree(1), BinaryTree(3))
t2 = BinaryTree(7, BinaryTree(1), BinaryTree(2))
print(allPath(t1, t2))

t1 = BinaryTree(8, BinaryTree(2),
                   BinaryTree(29, BinaryTree(3), BinaryTree(9)))
t2 = BinaryTree(8, BinaryTree(2, BinaryTree(2)),
                   BinaryTree(29, BinaryTree(3, None, BinaryTree(3)), BinaryTree(9)))
print(allPath(t1, t2))
