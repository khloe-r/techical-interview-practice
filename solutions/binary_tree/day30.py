"""
Day 30 - Sep 4

Given a binary search tree, rearrange the tree such that it forms a linked list where all its values are in ascending order.

Ex: Given the following tree...
        5
       / \
      1   6
return...

1
 \
  5
   \
    6
Ex: Given the following tree...

       5
      / \
    2    9
   / \ 
  1   3 
return...

1
 \
  2
   \
    3
     \
      5
       \
        9
Ex: Given the following tree...

5
 \
  6
return...

5
 \
  6
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def treeToList(tree):
  if tree == None:
    return None
  right = treeToList(tree.right)
  left = treeToList(tree.left)
  ans = None
  reversed = []

  while right != None:
    reversed.append(right.val)
    right = right.next
  for i in range(len(reversed) - 1, -1, -1):
    ans = Node(reversed[i], ans)
  reversed = []
  
  if tree != None:
    ans = Node(tree.val, ans)
  
  while left != None:
    reversed.append(left.val)
    left = left.next
  for i in range(len(reversed) - 1, -1, -1):
    ans = Node(reversed[i], ans)

  return ans

"""
Time Complexity: O(n^2) where n = height of tree
"""

tree1 = BinaryTree(5, BinaryTree(1), BinaryTree(6))
lst = treeToList(tree1)
while lst != None:
  print(lst.val)
  lst = lst.next

print('---')

tree2 = BinaryTree(5, BinaryTree(2, BinaryTree(1), BinaryTree(3)), BinaryTree(9))
lst = treeToList(tree2)
while lst != None:
  print(lst.val)
  lst = lst.next

print('---')

tree3 = BinaryTree(5, None, BinaryTree(6))
lst = treeToList(tree3)
while lst != None:
  print(lst.val)
  lst = lst.next
  