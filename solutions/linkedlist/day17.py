"""
Day 17 - Aug 22

Given a linked list and a value, remove all nodes containing the provided value, and return the resulting list. 

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null
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
value = int(input())


def sortLinkedList(lst, value):
    if lst.val == value:
        first = lst.next
    else:
        first = lst

    while lst != None and lst.next != None:
        if lst.next.val == value:
            lst.next = lst.next.next
        else:
          lst = lst.next

    return first


"""
Time Complexity: O(n) where n = len(lst)
"""

ref = sortLinkedList(l1, value)
while ref != None:
    print(ref.val)
    ref = ref.next
