"""
Day 13 - Aug 18

Given two integer arrays, return their intersection. 
Note: the intersection is the set of elements that are common to both arrays. 

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

nums1 = input()
nums2 = input()

nums1 = nums1.split(' ')
nums1 = list(map(lambda x: int(x), nums1))
nums2 = nums2.split(' ')
nums2 = list(map(lambda x: int(x), nums2))

def intersection(nums1, nums2):
  hash = {}
  result = []
  for num in nums1:
    if num not in hash:
      hash[num] = 1
      
  for num in nums2:
    if num in hash and hash[num] > 0:
      hash[num] -= 1
      result.append(num)

  return result

"""
Time Complexity: O(n) where n = max(len(nums1), len(nums2))
"""

print(intersection(nums1, nums2))