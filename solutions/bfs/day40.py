
"""
Day 40 - Sep 14

Given a binary tree, return its zig-zag level order traversal (i.e. its level order traversal from left to right the first level, right to left the level the second, etc.). 

Ex: Given the following tree…

    1
   / \
  2   3
return [[1], [3, 2]]
Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return [[8], [29, 2], [3, 9]]
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def zigZagTraverse(tree):
  nodes = [tree]
  ans = []
  temp = []
  levelSize = 1
  nextLevelSize = 0
  
  while len(nodes) > 0:
    node = nodes[0]
    nodes = nodes[1:]
    temp.append(node.val)
    levelSize -= 1
      
    if node.left:
      nodes.append(node.left)
      nextLevelSize += 1
    if node.right:
      nodes.append(node.right)
      nextLevelSize += 1

    if levelSize == 0:
      if (len(ans) % 2 != 0):
        temp.reverse()
      ans.append(temp)
      temp = []
      levelSize = nextLevelSize
      nextLevelSize = 0

  return ans

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(1, BinaryTree(2), BinaryTree(3))
print(zigZagTraverse(t1))

t1 = BinaryTree(2, BinaryTree(10), BinaryTree(15, None, BinaryTree(20)))
print(zigZagTraverse(t1))

t1 = BinaryTree(8, BinaryTree(2), BinaryTree(29, BinaryTree(3), BinaryTree(9)))
print(zigZagTraverse(t1))

t1 = BinaryTree(7, BinaryTree(4, BinaryTree(1), BinaryTree(4)), BinaryTree(9, BinaryTree(8), BinaryTree(9, None, BinaryTree(9))))
print(zigZagTraverse(t1))