
"""
Day 39 - Sep 13

Given a binary tree, returns of all its levels in a bottom-up fashion (i.e. last level towards the root). Ex: Given the following tree…

        2
       / \
      1   2
return [[1, 2], [2]]
Ex: Given the following tree…

       7
      / \
    6    2
   / \ 
  3   3 
return [[3, 3], [6, 2], [7]]
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
      ans.append(temp)
      temp = []
      levelSize = nextLevelSize
      nextLevelSize = 0

  ans.reverse()
  return ans

"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(2, BinaryTree(1), BinaryTree(2))
print(levelOrderTraverse(t1))

t1 = BinaryTree(2, BinaryTree(10), BinaryTree(15, None, BinaryTree(20)))
print(levelOrderTraverse(t1))

t1 = BinaryTree(7, BinaryTree(6, BinaryTree(3), BinaryTree(3)), BinaryTree(2))
print(levelOrderTraverse(t1))

t1 = BinaryTree(7, BinaryTree(4, BinaryTree(1), BinaryTree(4)), BinaryTree(9, BinaryTree(8), BinaryTree(9, None, BinaryTree(9))))
print(levelOrderTraverse(t1))