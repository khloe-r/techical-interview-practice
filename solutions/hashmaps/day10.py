"""
Day 10 - Aug 15

Given two strings s and t return whether or not s is an anagram of t. 
Note: An anagram is a word formed by reordering the letters of another word. 

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false

"""

s = input()
t = input()

def isAnagram(s, t):
  hash = {}
  for letter in s:
    if letter in hash:
      hash[letter] += 1
    else:
      hash[letter] = 1
  for letter in t:
    if letter in hash and hash[letter] > 0:
      hash[letter] -= 1
    else:
      return False
  for letter in s:
    if hash[letter] != 0:
      return False
  return True

"""
Time Complexity: O(n) where n = max(len(s), len(t))
"""

print(isAnagram(s, t))