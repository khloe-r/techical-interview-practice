"""
Day 24 - Aug 29

Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result. 

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
"""

s = input()

def removeDups(s):
  stack = []
  for char in s:
    if len(stack) and stack[-1] == char:
      stack.pop()
    else:
      stack.append(char)
  return ''.join(stack)

"""
Time Complexity: O(n) where n = max(len(s), len(t))
"""

print(removeDups(s))