
"""
Day 42 - Sep 16

Given a binary tree, return its column order traversal from top to bottom and left to right. Note: if two nodes are in the same row and column, order them from left to right. 

Ex: Given the following tree…

    8
   / \
  2   29
     /  \
    3    9
return [[2], [8, 3], [29], [9]]
[[8], [2,29], [N,N,3,9]]
Ex: Given the following tree…

     100
    /   \
  53     78
 / \    /  \
32  3  9    20
return [[32], [53], [100, 3, 9], [78], [20]]
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def columnTraverse(tree):
  nodes = [tree]
  parents = [0]
  columns = {}
  levelSize = 1
  tempLevelSize = 0
  
  while len(nodes) > 0:
    node = nodes[0]
    parent = parents[0]
    nodes = nodes[1:]
    parents = parents[1:]
    if parent in columns:
      columns[parent].append(node.val)
    else:
      columns[parent] = [node.val]
    levelSize -= 1
      
    if node.left:
      parents.append(parent - 1)
      nodes.append(node.left)
      tempLevelSize += 1
    if node.right:
      parents.append(parent + 1)
      nodes.append(node.right)
      tempLevelSize += 1

    if levelSize == 0:
      levelSize = tempLevelSize
      tempLevelSize = 0

  ans = []
  keys = list(columns.keys())
  for i in range(min(keys), max(keys) + 1):
    ans.append(columns[i])
  return ans

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(8, BinaryTree(2), BinaryTree(29, BinaryTree(3), BinaryTree(9)))
print(columnTraverse(t1))

t1 = BinaryTree(100, BinaryTree(53, BinaryTree(32), BinaryTree(3)), BinaryTree(78, BinaryTree(9), BinaryTree(20)))
print(columnTraverse(t1))