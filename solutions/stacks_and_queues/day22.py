""" 
Day 22 - Aug 27

Given a string only containing the following characters (, ), {, }, [, and ] return whether or not the opening and closing characters are in a valid order. 

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
"""

brackets = input()

def validBrackets(brackets):
  hash = {
    "{": "}",
    "(": ")",
    "[": "]"
  }
  stack = []
  for char in brackets:
    if char in hash:
      stack.append(char)
    else:
      if len(stack) and hash[stack[-1]] == char:
        stack.pop()
      else:
        return False

  if len(stack) == 0:
    return True
  return False

"""
Time Complexity: O(n) where n = len(brackets)
"""

print(validBrackets(brackets))