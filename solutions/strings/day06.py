"""
Day 6 - Aug 11

Given an array of strings, return the longest common prefix that is shared amongst all strings. 
Note: you may assume all strings only contain lowercase alphabetical characters. 

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""

arr_input = [input(), input(), input(), input()]


def commonPrefix(arr_input):
  checked = list(filter(lambda x: arr_input[0][0] == x[0], arr_input))
  if (len(checked) != len(arr_input)):
    return ""
  
  minWord = min(arr_input, key=len)
  half = int(len(minWord) / 2) + 1
  minWidth = 0
  while half < minWidth or half > len(minWord):
    checked = list(filter(lambda x: minWord[:half] in x, arr_input))
    if (len(checked) == len(arr_input)):
      half += 1
      minWidth = half
    else:
      half -= 1
  return minWord[:half]
    

"""
Time Complexity: O(n * m) where n = len(minWord) / 2 and m = len(arr_input)

- The outer while True loop runs at max until half reaches 0 or len(minWord) or which it is halfway between thus max n times
- The filter function has timeComplexity of O(m) where m is the length of the array
"""

print(commonPrefix(arr_input))
