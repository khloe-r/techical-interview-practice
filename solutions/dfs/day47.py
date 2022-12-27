"""
Day 47 - Sep 21

Given a binary tree, return whether or not it forms a reflection across its center (i.e. a line drawn straight down starting from the root). 
Note: a reflection is when an image, flipped across a specified line, forms the same image. 

Ex: Given the following tree…

   2
 /   \
1     1
return true as when the tree is reflected across its center all the nodes match.
Ex: Given the following tree…

    1
   / \
  5   5
   \    \
    7    7
return false as when the tree is reflected across its center the nodes containing sevens do not match.
"""


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPathTree(treel, treer):
    if not treel and not treer:
      return True
    if (not treel and treer) or (not treer and treel):
      return False
    if treel.val != treer.val:
      return False
      
    return allPathTree(treel.right, treer.left) and allPathTree(treel.left, treer.right)

def allPath(tree):
    return allPathTree(tree, tree)


"""
Time Complexity: O(n) where n = # of nodes of tree
"""

t1 = BinaryTree(2, BinaryTree(1), BinaryTree(1))
print(allPath(t1))

t1 = BinaryTree(1, BinaryTree(5, None, BinaryTree(7)),
                   BinaryTree(5, None, BinaryTree(7)))
print(allPath(t1))

t1 = BinaryTree(1, BinaryTree(5, BinaryTree(7), None),
                   BinaryTree(5, None, BinaryTree(7)))
print(allPath(t1))

t1 = BinaryTree(1, BinaryTree(5, BinaryTree(7), BinaryTree(8)),
                   BinaryTree(5, BinaryTree(9), BinaryTree(7)))
print(allPath(t1))
