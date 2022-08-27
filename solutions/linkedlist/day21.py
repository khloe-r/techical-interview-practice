"""
Day 21 - Aug 26

Given a linked list, containing unique values, reverse it, and return the result. 

Ex: Given the following linked lists...

1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = input()
list1 = list1.split(' ')
list1 = list(map(lambda x: int(x), list1))
for i in range(len(list1) - 1, -1, -1):
    if i == len(list1) - 1:
        list1[i] = ListNode(list1[i])
    else:
        list1[i] = ListNode(list1[i], list1[i + 1])

l1 = list1[0]

def reverseList(lst):
  last = None
  while lst != None:
    new = ListNode(lst.val, last)
    last = new
    lst = lst.next
    
  return last

"""
Time Complexity: O(n) where n = len(lst)
"""

ref = reverseList(l1)
while ref != None:
    print(ref.val)
    ref = ref.next