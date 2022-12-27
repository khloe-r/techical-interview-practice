"""
Day 46 - Sep 20

Given a binary tree, containing unique values, determine if it is a valid binary search tree. 
Note: the invariants of a binary search tree (in our case) are all values to the left of a given node are less than the current node’s value, all values to the right of a given node are greater than the current node’s value, and both the left and right subtrees of a given node must also be binary search trees. 

Ex: Given the following binary tree…

   1
 /   \
2     3
return false.

Ex: Given the following tree…

   2
 /   \
1     3
return true.
"""


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPathTree(tree, min, max):
    if tree == None:
      return True
    if tree.val < min or tree.val > max:
      return False
      
    return allPathTree(tree.left, min, tree.val - 1) and allPathTree(tree.right, tree.val + 1, max)

def allPath(tree):
    return allPathTree(tree, float('-inf'), float('inf'))


"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(2, BinaryTree(1), BinaryTree(3))
print(allPath(t1))

t1 = BinaryTree(10, BinaryTree(7, BinaryTree(3), BinaryTree(11)),
                BinaryTree(15, BinaryTree(12), BinaryTree(29)))
print(allPath(t1))

t1 = BinaryTree(104, BinaryTree(39, BinaryTree(20, BinaryTree(1))))
print(allPath(t1))

t1 = BinaryTree(104, BinaryTree(39, BinaryTree(20, BinaryTree(1), BinaryTree(19))))
print(allPath(t1))
