"""
Day 56 - Sep 30

Given a string s, return all possible partitions of s such that each substring is a palindrome.

Ex: Given the following string s…

s = "abcba",
return [
    ["a","b","c","b","a"],
    ["a","bcb","a"],
    ["abcba"]
]
"""

def palindromes(str):
  ans = [[ch for ch in str]]
  
  def palinHelper(str, start):
    i, j = start, len(str) - 1
    while i <= j:
      if str[i] != str[j] or i == j:
        j -= 1
        if i == j:
          i += 1
          j = len(str) - 1
        if i == len(str) - 1:
          return
      else:
        possi, possj = i, j
        while str[i] == str[j] and i <= j:
          i += 1
          j -= 1
        if i - 1 == j + 1 or i == j + 1:
          ans.append(str[:possi] + [''.join(str[possi:possj+1])] + str[possj+1:])
          palinHelper(ans[-1], possi)
        if possj - 1 <= possi:
          i, j = possi + 1, len(str) - 1
        else:
          i, j = possi, possj - 1

  palinHelper([ch for ch in str], 0)
  return ans
  
"""
Time Complexity: O(m*n^2) where n = len(str) and m = # of combinations
"""

print(palindromes("abcba")) 
print(palindromes("abcb")) 
print(palindromes("abcbdbcba")) 
print(palindromes("fff")) 
print(palindromes("a")) 

