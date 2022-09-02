"""
Day 28 - Sep 2

Design a class to implement a stack using only a single queue. Your class, QueueStack, should support the following stack methods: push() (adding an item), pop() (removing an item), peek() (returning the top value without removing it), and empty() (whether or not the stack is empty).
"""

from collections import deque

class QueueStack:
  def __init__(self):
    self.queue = deque()

  def push(self, val):
    self.queue.append(val)

  def pop(self):
    return self.queue.pop()

  def peek(self):
    return list(self.queue)[-1]

  def empty(self):
    return len(list(self.queue)) == 0

q = QueueStack()
print(q.empty())
q.push(4)
print(q.empty())
q.push(5)
q.push(6)
q.push(7)
print(q.peek())
print(q.pop())
print(q.pop())