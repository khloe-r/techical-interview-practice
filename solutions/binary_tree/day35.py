"""
Day 35 - Sep 9

Given a binary search tree, return its mode (you may assume the answer is unique). If the tree is empty, return -1. Note: the mode is the most frequently occurring value in the tree. 

Ex: Given the following tree...

        2
       / \
      1   2
return 2.

Ex: Given the following tree...

         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9  
return 9.
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def modeBinaryTree(tree):
  hashmap = {}
  nodes = [tree]
  while len(nodes) > 0:
    node = nodes.pop()
    if node.val in hashmap:
      hashmap[node.val] += 1
    else:
      hashmap[node.val] = 1
      
    if node.right:
      nodes.append(node.right)
    if node.left:
      nodes.append(node.left)

  vals = list(hashmap.keys())
  maxnum = hashmap[vals[0]]
  ans = vals[0]

  for x in vals:
    if hashmap[x] > maxnum:
      maxnum = hashmap[x]
      ans = x

  return ans


"""
Time Complexity: O(n) where n = # of nodes of tree
Space Complexity: O(n) where n = # of nodes of tree 
"""
      

t1 = BinaryTree(2, BinaryTree(1), BinaryTree(2))
print(modeBinaryTree(t1))

t2 = BinaryTree(7, BinaryTree(4, BinaryTree(1), BinaryTree(4)), BinaryTree(9, BinaryTree(8), BinaryTree(9, None, BinaryTree(9))))
print(modeBinaryTree(t2))
