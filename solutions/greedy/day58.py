"""
Day 58 - Oct 2

You are given a bag of coins, an initial energy of E, and want to maximize your number of points (which starts at zero). To gain a single point you can exchange coins[i] amount of energy (i.e. if I have 100 energy and a coin that has a value 50 I can exchange 50 energy to gain a point). If you do not have enough energy you can give away a point in exchange for an increase in energy by coins[i] amount (i.e. you give away a point and your energy is increased by the value of that coin: energy += coins[i]). Return the maximum number of points you can gain. 
Note: Each coin may only be used once.

Ex: Given the following coins and starting energy…

coins = [100, 150, 200] and E = 150, return 1
coins = [100,200,300,400] and E = 200, return 2
coins = [300] and E = 200, return 0
"""

def coinPoints(coins, E):
  coins.sort()

  earn = sum(coins)
  give = E 
  i = len(coins) - 1
  while earn > give:
    if i >= len(coins) / 2:
      earn -= coins[i]
      give += coins[i]
      i -= 1
    else:
      return 0

  return i + 1 - (len(coins) - i - 1)
    

"""
Time Complexity: O(n^2) where n = len(weights)
"""

print(coinPoints([100, 150, 200], 150)) 
print(coinPoints([100, 200, 300, 400], 200)) 
print(coinPoints([100, 100], 0)) 
print(coinPoints([300], 200))