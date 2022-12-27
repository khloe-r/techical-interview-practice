
"""
Day 37 - Sep 11

Given a binary tree, return the largest value in each of its levels. Ex: Given the following tree…

    2
   / \
  10  15
        \
         20
return [2, 15, 20]
Ex: Given the following tree…

          1
         / \
        5   6
       / \   \  
      5   3   7 
return [1, 6, 7]
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
    temp = node.val if not temp else max(temp, node.val)
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

t1 = BinaryTree(1, BinaryTree(5, BinaryTree(5), BinaryTree(3)), BinaryTree(6, None, BinaryTree(7)))
print(levelOrderTraverse(t1))