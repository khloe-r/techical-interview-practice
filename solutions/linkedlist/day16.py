""" 
Day 16 - Aug 21

Given a linked list and a value n, remove the nth to last node and return the resulting list. 

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
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
    list1[i] = ListNode(list1[i], list1[i+1])

l1 = list1[0]
n = int(input())

def sortLinkedList(lst, n):
  length = 0
  start = lst
  while lst != None:
    length += 1
    lst = lst.next

  if length == n:
    lst = start.next
    start = start.next
  else:
    lst = start
  
  while start != None:
    if length - 1 == n:
      start.next = start.next.next
      start = start.next
      length -= 1
    else:
      start = start.next
      length -= 1

  return lst
    

"""
Time Complexity: O(n) where n = len(lst)
"""

ref = sortLinkedList(l1, n)
while ref != None:
  print(ref.val)
  ref = ref.next