"""

Day 8 - Aug 13

Given an array of integers, return whether or not two numbers sum to a given target, k. 
Note: you may not sum a number with itself. 

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)

"""

numbers = input()

numbers = numbers.split(' ')
numbers = list(map(lambda x: int(x), numbers))
k = int(input())


def twoSum(numbers, k):
  dict = {}
  for num in numbers:
    if num in dict:
      return True
    else:
      dict[k - num] = True
  return False

"""
Time Complexity: O(n) where n = len(numbers)
"""

print(twoSum(numbers, k))