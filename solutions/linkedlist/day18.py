
"""
Day 18 - Aug 23

Given a non-empty linked list, return the middle node of the list. If the linked list contains an even number of elements, return the node closer to the end. 
Ex: Given the following linked lists... 

1->2->3->null, return 2
1->2->3->4->null, return 3
1->null, return 1

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

def middleNode(lst):
  length = 0
  first = lst
  while lst != None:
    length += 1
    lst = lst.next

  mid = int((length / 2))
  length = 0
  while length != mid:
    first = first.next
    length += 1

  return first.val

"""
Time Complexity: O(n) where n = len(lst)
"""

print(middleNode(l1))