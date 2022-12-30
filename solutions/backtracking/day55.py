"""
Day 55 - Sep 29

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

def uniqSums(numbers, target):
  ans = []
  numbers.sort()
  def uniqSumshelper(sum, paths):
    for n in numbers:
      if not paths or n >= paths[-1]:
        if sum + n == target:
            ans.append(paths + [n])
        elif sum + n < target:
            uniqSumshelper(sum + n, paths + [n])
            continue
        
        return

  uniqSumshelper(0, [])
  return ans
  
"""
Time Complexity: O(nm) where n = len(numbers) and m = # of elements in all combinations
"""

print(uniqSums([2,4,6,3], 6))
print(uniqSums([1,2,3,4,5], 6))