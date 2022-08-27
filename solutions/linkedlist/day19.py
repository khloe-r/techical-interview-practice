""" 
Day 19 - Aug 24

Given a linked list, containing unique numbers, return whether or not it has a cycle. 
Note: a cycle is a circular arrangement (i.e. one node points back to a previous node) 

Ex: Given the following linked lists...

1->2->3->1 -> true (3 points back to 1)
1->2->3 -> false
1->1 true (1 points to itself)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(lst):
  hash = {}
  while lst != None:
    if lst.val in hash:
      return True
    else:
      hash[lst.val] = True
    lst = lst.next
  return False

"""
Time Complexity: O(n) where n = len(lst)
"""

# Test Cases

x3 = ListNode(3)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)
x3.next = x1

y3 = ListNode(3, None)
y2 = ListNode(2, y3)
y1 = ListNode(1, y2)

z1 = ListNode(1)
z1.next = z1

print(middleNode(x1))
print(middleNode(y1))
print(middleNode(z1))