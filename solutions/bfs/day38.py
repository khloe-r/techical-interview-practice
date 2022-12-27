
"""
Day 38 - Sep 12

Given a binary tree return all the values you’d be able to see if you were standing on the left side of it with values ordered from top to bottom.

Ex: Given the following tree…

-->    4
      / \
-->  2   7
return [4, 2]
Ex: Given the following tree…

-->        7
         /  \
-->     4     9
       / \   / \
-->   1   4 8   9
                 \
-->               9
return [7, 4, 1, 9]
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def levelOrderTraverse(tree):
  nodes = [tree]
  ans = []
  temp = None
  levelSize = 1
  nextLevelSize = 0
  
  while len(nodes) > 0:
    node = nodes[0]
    nodes = nodes[1:]
    if not temp:
      temp = node.val
    levelSize -= 1
      
    if node.left:
      nodes.append(node.left)
      nextLevelSize += 1
    if node.right:
      nodes.append(node.right)
      nextLevelSize += 1

    if levelSize == 0:
      ans.append(temp)
      temp = None
      levelSize = nextLevelSize
      nextLevelSize = 0

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

t1 = BinaryTree(7, BinaryTree(4, BinaryTree(1), BinaryTree(4)), BinaryTree(9, BinaryTree(8), BinaryTree(9, None, BinaryTree(9))))
print(levelOrderTraverse(t1))