"""
Day 33 - Sep 7

Given two binary trees, return whether or not the two trees are identical. Note: identical meaning they exhibit the same structure and the same values at each node. Ex: Given the following trees...

        2
       / \
      1   3
    2
   / \
  1   3

return true.
Ex: Given the following trees...

        1
         \
          9
           \
           18
    1
   /
  9
   \
    18

return false.
Ex: Given the following trees...

        2
       / \
      3   1
    2
   / \
  1   3

return false.  
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def binaryTreeEqual(tree1, tree2):
  if (tree1 and tree2) or (not tree1 and not tree2):
    if not tree1 and not tree2:
      return True
    if tree1.val == tree2.val:
      return binaryTreeEqual(tree1.left, tree2.left) and binaryTreeEqual(tree1.right, tree2.right)
    else:
      return False
  else:
    return False

"""
Time Complexity: O(n) where n = # of nodes of tree
Space Complexity: O(n) where n = # of nodes of tree (based on stack size for recursive calls)
"""
      
t1 = BinaryTree(2, BinaryTree(1), BinaryTree(3))
print(binaryTreeEqual(t1, t1))

t2 = BinaryTree(1, None, BinaryTree(9, None, BinaryTree(18)))
t3 = BinaryTree(1, BinaryTree(9, None, BinaryTree(18)), None)
print(binaryTreeEqual(t2, t3))

t4 = BinaryTree(2, BinaryTree(1), BinaryTree(3))
t5 = BinaryTree(2, BinaryTree(3), BinaryTree(1))
print(binaryTreeEqual(t4, t5))