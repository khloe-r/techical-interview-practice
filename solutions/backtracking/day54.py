"""
Day 54 - Sep 28

Given an integer N, where N represents the number of pairs of parentheses (i.e. ”(“ and ”)”) you are given, return a list containing all possible well-formed parentheses you can create.

Ex: Given the following value of N…

N = 3, 
return [  
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

def brackets(pairs, max):
  if pairs == 0.5:
    return [")"]

  remaining = brackets(pairs - 0.5, max)
  r = len(remaining)
  for j in range(r):
    if (remaining[j].count(")") == remaining[j].count("(")):
      remaining[j] = ")" + remaining[j]
    elif (remaining[j].count(")") == max):
      remaining[j] = "(" + remaining[j]
    else:
      remaining.append(")" + remaining[j])
      remaining[j] = "(" + remaining[j]
  
  return remaining
  
"""
Time Complexity: O(n^2) where n = # of bracket combinations
"""

print(brackets(2, 2))
print(brackets(3, 3))
print(brackets(4, 4))