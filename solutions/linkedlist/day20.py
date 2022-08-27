"""
Day 20 - Aug 25

Given a potentially cyclical linked list where each value is unique, return the node at which the cycle starts. If the list does not contain a cycle, return null. 

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(lst):
  hash = {}
  while lst != None:
    if lst.val in hash:
      return lst
    else:
      hash[lst.val] = True
    lst = lst.next
  return None

"""
Time Complexity: O(n) where n = len(lst)
"""

# Test Cases

x3 = ListNode(3)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

y5 = ListNode(5)
y4 = ListNode(4, y5)
y3 = ListNode(3, y4)
y2 = ListNode(2, y3)
y1 = ListNode(1, y2)
y5.next = y2

z4 = ListNode(7)
z3 = ListNode(3, z4)
z2 = ListNode(9, z3)
z1 = ListNode(1, z2)
z4.next = z4

print(middleNode(x1))
print(middleNode(y1).val)
print(middleNode(z1).val)