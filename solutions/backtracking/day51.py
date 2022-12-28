"""
Day 51 - Sep 25

This question is asked by Google. Given a string of digits, return all possible text messages those digits could send. Note: The mapping of digits to letters is as follows…

0 -> null
1 -> null
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"
Ex: digits = "23" return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

guide = {
  "0": "",
  "1": "",
  "2": "abc",
  "3": "def",
  "4": "ghi",
  "5": "jkl",
  "6": "mno",
  "7": "pqrs",
  "8": "tuv",
  "9": "wxyz"
}

def capitalizationPerms(str):
  if len(str) == 1:
    return [ch for ch in guide[str[0]]]
  
  ans = [i+j for i in guide[str[0]] for j in capitalizationPerms(str[1:])]
  return ans
  
"""
Time Complexity: O(n^2) where n = len(str)
"""

print(capitalizationPerms("23"))
print(capitalizationPerms("234"))