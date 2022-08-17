"""
Day 11 - Aug 16

Given a string, return the index of its first unique character. If a unique character does not exist, return -1. 

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""

string_input = input()

def firstUnique(input):
  hash = {}
  min = -1
  for i in range(len(input)):
    if input[i] in hash:
      hash[input[i]] = -1
    else:
      hash[input[i]] = i

  for char in hash.keys():
    if hash[char] != -1 and (min == -1 or hash[char] < min):
      min = hash[char]

  return min
      

"""
Time Complexity: O(n) where n = len(string_input)
"""

print(firstUnique(string_input))