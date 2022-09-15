
"""
Day 36 - Sep 10

Given a binary tree, return its level order traversal where the nodes in each level are ordered from left to right.

Ex: Given the following tree...

    4
   / \
  2   7
return [[4], [2, 7]]
Ex: Given the following tree...

    2
   / \
  10  15
        \
         20
return [[2], [10, 15], [20]]
Ex: Given the following tree...

    1
   / \
  9   32
 /      \
3        78
return [[1], [9, 32], [3, 78]]
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def levelOrderTraverse(tree):
  nodes = [tree]
  ans = []
  temp = []
  levelSize = 1
  tempLevelSize = 0
  
  while len(nodes) > 0:
    node = nodes[0]
    nodes = nodes[1:]
    temp.append(node.val)
    levelSize -= 1
      
    if node.left:
      nodes.append(node.left)
      tempLevelSize += 1
    if node.right:
      nodes.append(node.right)
      tempLevelSize += 1

    if levelSize == 0:
      ans.append(temp)
      temp = []
      levelSize = tempLevelSize
      tempLevelSize = 0

  return ans

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(4, BinaryTree(2), BinaryTree(7))
print(levelOrderTraverse(t1))

t1 = BinaryTree(2, BinaryTree(10), BinaryTree(15, None, BinaryTree(20)))
print(levelOrderTraverse(t1))

t1 = BinaryTree(1, BinaryTree(9, BinaryTree(3)), BinaryTree(32, None, BinaryTree(78)))
print(levelOrderTraverse(t1))

t1 = BinaryTree(1, BinaryTree(9, BinaryTree(3)), BinaryTree(32, BinaryTree(31), BinaryTree(78)))
print(levelOrderTraverse(t1))