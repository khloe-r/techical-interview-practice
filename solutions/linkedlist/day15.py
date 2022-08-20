"""
Day 15 - Aug 20

Given two sorted linked lists, merge them together in ascending order and return a reference to the merged list 

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = input()
list1 = list1.split(' ')
for i in range(len(list1) - 1, -1, -1):
  if i == len(list1) - 1:
    list1[i] = ListNode(list1[i])
  else:
    list1[i] = ListNode(list1[i], list1[i+1])
    
list2 = input()
list2 = list2.split(' ')
for i in range(len(list2) - 1, -1, -1):
  if i == len(list2) - 1:
    list2[i] = ListNode(list2[i])
  else:
    list2[i] = ListNode(list2[i], list2[i+1])

l1 = list1[0]
l2 = list2[0]

def sortLinkedList(list1, list2):
  start = ListNode(min(list1.val, list2.val))
  first = None
  if list1.val < list2.val:
    list1 = list1.next
  else:
    list2 = list2.next
    
  while list1 != None or list2 != None:
    if list2 == None or (list1 != None and list1.val < list2.val):
      start.next = ListNode(list1.val)
      list1 = list1.next
    else:
      start.next = ListNode(list2.val)
      list2 = list2.next
    if first == None:
      first = start
    start = start.next
  return first    

"""
Time Complexity: O(n) where n = len(list1) + len(list2)
"""

ref = sortLinkedList(l1, l2)
while ref != None:
  print(ref.val)
  ref = ref.next
