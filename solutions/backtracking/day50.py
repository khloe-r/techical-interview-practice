"""
Day 50 - Sep 24

Given a string s consisting of only letters and digits, where we are allowed to transform any letter to uppercase or lowercase, return a list containing all possible permutations of the string.

Ex: Given the following string…

S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]
"""

"""
Time Complexity: O(nm) where n = len(str) and m = # of permutations
"""
def capitalizationPerms(str):
  ans = [""]
  for i in range(len(str)):
    if str[i].isalpha():
      l = len(ans)
      for j in range(l):
        ans.append(ans[j] + str[i].lower())
        ans[j] += str[i].upper()
    else:
      for j in range(len(ans)):
        ans[j] += str[i]
  return ans

"""
Time Complexity: O(2^n) where n = len(str)
"""
def capPerms(str, ans, i):
  if i >= len(str):
    ans.append(str)
    return
  elif str[i].isalpha():
    capPerms(str[:i] + str[i].upper() + str[i+1:], ans, i+1)
    capPerms(str[:i] + str[i].lower() + str[i+1:], ans, i+1)
  else:
    capPerms(str, ans, i+1)

  return ans

print(capitalizationPerms("c7w2"))
print(capitalizationPerms("abcd"))