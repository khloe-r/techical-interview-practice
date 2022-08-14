"""
Day 9 - Aug 14

Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels. 

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""

jewels = input()
stones = input()

def stonesAndJewels(jewels, stones):
  jewel_dict = {}
  total_jewels = 0
  for jewel in jewels:
    if (jewel not in jewel_dict):
      jewel_dict[jewel] = 0

  for stone in stones:
    if (stone in jewel_dict):
      total_jewels += 1
  return total_jewels

"""
Time Complexity: O(n) where n = max(len(jewels), len(stones))
"""

print(stonesAndJewels(jewels, stones))