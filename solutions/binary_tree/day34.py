
"""
Day 34 - Sep 8

Given a binary search tree, return the minimum difference between any two nodes in the tree.

Ex: Given the following tree...
        2
       / \
      3   1
return 1.
Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.
Ex: Given the following tree...
        2
         \
         100
return 98.
"""

class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def mergeSort(arr):
  if len(arr) == 1:
    return arr
  mid = len(arr) // 2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])

  i = j = k = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
      k += 1
    else:
      arr[k] = right[j]
      j += 1
      k += 1

  while i < len(left):
    arr[k] = left[i]
    i += 1
    k += 1

  while j < len(right):
    arr[k] = right[j]
    j += 1
    k += 1

  return arr    

def minDiff(tree):
  nodes = [tree]
  vals = []
  while len(nodes) > 0:
    node = nodes.pop()
    vals.append(node.val)
    if node.left:
      nodes.append(node.left)
    if node.right:
      nodes.append(node.right)

  mergeSort(vals)
  minnum = abs(vals[0] - vals[1])

  for x in range(1, len(vals) - 1):
    minnum = min(minnum, abs(vals[x] - vals[x+1]))

  return minnum
     
"""
Assumptions: At least 2 nodes per tree
Time Complexity: O(n log(n)) where n = # of nodes in a tree
Space Complexity: O(n)
"""

t1 = BinaryTree(2, BinaryTree(3), BinaryTree(1))
print(minDiff(t1))

t2 = BinaryTree(29, BinaryTree(17, BinaryTree(1)), BinaryTree(50, BinaryTree(42), BinaryTree(59)))
print(minDiff(t2))

t3 = BinaryTree(2, None, BinaryTree(100))
print(minDiff(t3))
