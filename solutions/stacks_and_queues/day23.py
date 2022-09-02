"""
Day 23 - Aug 28

Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result. 

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
"""

s = input()
t = input()

def matchingStrings(s, t):
  stack_s = []
  stack_t = []
  for char in s:
    if char == "#":
      stack_s.pop()
    else:
      stack_s.append(char)

  for char in t:
    if char == "#":
      stack_t.pop()
    else:
      stack_t.append(char)

  stack_s = ''.join(stack_s)
  stack_t = ''.join(stack_t)
  return stack_s == stack_t

"""
Time Complexity: O(n) where n = max(len(s), len(t))
"""

print(matchingStrings(s, t))