
"""
Day 41 - Sep 15

Given an n-ary tree, return its level order traversal. 
Note: an n-ary tree is a tree in which each node has no more than N children. 

Ex: Give the following n-ary tree…

    8
  / | \
 2  3  29
return [[8], [2, 3, 29]]
Ex: Given the following n-ary tree…

     2
   / | \
  1  6  9
 /   |   \
8    2    2
   / | \
 19 12 90
return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
"""

class UnaryTree:
  def __init__(self, val, children=[]):
    self.val = val
    self.children = children

def unaryTraverse(tree):
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
      
    for i in node.children:
      nodes.append(i)
      nextLevelSize += 1

    if levelSize == 0:
      ans.append(temp)
      temp = []
      levelSize = nextLevelSize
      nextLevelSize = 0

  return ans

"""
Time Complexity: O(nm) where n = # of nodes of tree and m = # of nodes in the largest level
"""

t1 = UnaryTree(8, [UnaryTree(2), UnaryTree(3), UnaryTree(9)])
print(unaryTraverse(t1))

t1 = UnaryTree(2, [UnaryTree(1, [UnaryTree(8)]), UnaryTree(6, [UnaryTree(2, [UnaryTree(19), UnaryTree(20), UnaryTree(90)])]), UnaryTree(9, [UnaryTree(2)])])
print(unaryTraverse(t1))