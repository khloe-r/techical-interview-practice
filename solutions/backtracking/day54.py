"""
Day 54 - Sep 28

Given a list of positive numbers without duplicates and a target number, find all unique combinations of the numbers that sum to the target. Note: You may use the same number more than once.

Ex: Given the following numbers and target…

numbers = [2,4,6,3], target = 6,
return [
    [2,2,2],
    [2,4],
    [3,3],
    [6]
]
"""

def brackets(pairs):
  return bracketsHelp(pairs, pairs)

def bracketsHelp(pairs, max):
  if pairs == 0.5:
    return [")"]

  remaining = bracketsHelp(pairs - 0.5, max)
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

print(brackets(2))
print(brackets(3))
print(brackets(4))