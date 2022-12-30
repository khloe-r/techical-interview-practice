"""
Day 57 - Oct 1

A ship is about to set sail and you are responsible for its safety precautions. More specifically, you are responsible for determining how many life rafts to carry onboard. You are given a list of all the passengers’ weights and are informed that a single life raft has a maximum capacity of limit and can hold at most two people. Return the minimum number of life rafts you must take onboard to ensure the safety of all your passengers. Note: You may assume that a the maximum weight of any individual is at most limit.

Ex: Given the following passenger weights and limit…

weights = [1, 3, 5, 2] and limit = 5, return 3
weights = [1, 2] and limit = 3, return 1
weights = [4, 2, 3, 3] and limit = 5 return 3
"""

def lifeRafts(weights, limit):
  extras = {}
  weights.sort()

  rafts = weights.count(limit)
  weights = weights[:len(weights) - rafts]

  i, j = 0, len(weights) - 1
  
  while len(weights) > 0:
    if len(weights) == 1:
      rafts += 1
      break
    if weights[i] + weights[j] <= limit:
      rafts += 1
      weights.pop(j)
      weights.pop(i)
      i, j = 0, len(weights) - 1
    elif j - 1 != i:
      j -= 1
    else:
      rafts += len(weights)
      break

  return rafts

"""
Time Complexity: O(n^2) where n = len(weights)
"""

print(lifeRafts([1, 3, 5, 2], 5))
print(lifeRafts([3, 3, 4, 4, 5], 5))
print(lifeRafts([1, 2, 4, 3, 5], 5))
print(lifeRafts([1, 2], 3))
print(lifeRafts([4, 2, 3, 3], 5))