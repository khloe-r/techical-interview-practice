
"""

Day 32 - Sep 6

Given an array of numbers sorted in ascending order, return a height-balanced binary search tree using every number from the array. 
Note: height-balanced meaning that the level of any node’s two subtrees should not differ by more than one. 

Ex: Given the following nums...

nums = [1, 2, 3] return a reference to the following tree...
       2
      /  \
     1    3
Ex: Given the following nums...

nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
      2   5
     /   / \
    1   4   6
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def arrToBinaryTree(arr):
  if len(arr) == 0:
    return None
  mid = 0 if len(arr) == 2 else len(arr) // 2 
  left = arrToBinaryTree(arr[:mid])
  right = arrToBinaryTree(arr[mid + 1:])
  return BinaryTree(arr[mid], left, right)

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = arrToBinaryTree([1,2,3])
print(t1.val, t1.left.val, t1.right.val)
t2 = arrToBinaryTree([1, 2, 3, 4, 5, 6])
print(t2.val)
print(t2.left.val, t2.right.val)
print(t2.left.left.val, t2.left.right.val, t2.right.right.val)
t2 = arrToBinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(t2.val)
print(t2.left.val, t2.right.val)
print(t2.left.left.val, t2.left.right.val, t2.right.left.val, t2.right.right.val)
print(t2.left.left.right.val, t2.right.left.right.val)
