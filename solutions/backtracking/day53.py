"""
Day 53 - Sep 27

Given a 2D matrix that represents a gold mine, where each cell’s value represents an amount of gold, return the maximum amount of gold you can collect given the following rules:

You may start and stop collecting gold from any position
You can never visit a cell that contains 0 gold
You cannot visit the same cell more than once
From the current cell, you may walk one cell to the left, right, up, or down
Ex: Given the following gold mine…

goldMine = [
    [0,2,0],
    [8,6,3],
    [0,9,0]
],
return 23 (start at 9 and then move to 6 and 8 respectively)
"""

def mining(mine):
  locations = []
  for i in range(len(mine)):
    for j in range(len(mine[i])):
      if 0 != mine[i][j]:
        history = {}
        history[i] = [j]
        locations.append([i, j, mine[i][j], history])
  if len(locations) == 0:
    return 0
  return max(miningHelper(mine, locations, []))

def miningHelper(board, opts, sums):    
  new_opts = []
  for opt in opts:
    y_1 = opt[0]
    x_1 = opt[1]
    sum = opt[2]
    history = opt[3]
    by = len(board)
    bx = len(board[0])
    original = len(new_opts)
    
    if x_1 + 1 < bx and (board[y_1][x_1 + 1] != 0):
      if history[y_1].count(x_1 + 1) == 0:
        history[y_1].append(x_1 + 1)
        new_opts.append([y_1, x_1 + 1, sum + board[y_1][x_1 + 1], history])
    if x_1 - 1 >= 0 and (board[y_1][x_1 - 1] != 0):
      if history[y_1].count(x_1 - 1) == 0:
        history[y_1].append(x_1 - 1)
        new_opts.append([y_1, x_1 - 1, sum + board[y_1][x_1 - 1], history])
    if y_1 + 1 < by and (board[y_1 + 1][x_1] != 0):
      if (y_1 + 1) not in history:
        history[y_1 + 1] = [x_1]
        new_opts.append([y_1 + 1, x_1, sum + board[y_1 + 1][x_1], history])
      elif history[y_1 + 1].count(x_1) == 0:
        history[y_1 + 1].append(x_1)
        new_opts.append([y_1 + 1, x_1, sum + board[y_1 + 1][x_1], history])
    if y_1 - 1 >= 0 and (board[y_1 - 1][x_1] != 0):
      if (y_1 - 1) not in history:
        history[y_1 - 1] = [x_1]
        new_opts.append([y_1 - 1, x_1, sum + board[y_1 - 1][x_1], history])
      elif history[y_1 - 1].count(x_1) == 0:
        history[y_1 - 1].append(x_1)
        new_opts.append([y_1 - 1, x_1, sum + board[y_1 - 1][x_1], history])

    if len(new_opts) == original:
      sums.append(sum)

  if len(new_opts) == 0:
    return sums
  return miningHelper(board, new_opts, sums)
  
"""
Time Complexity: O(z^2) where z = number of elements in the mine
"""


goldMine = [
    [0,2,0],
    [8,6,3],
    [0,9,0]
]
print(mining(goldMine))
goldMine = [
    [3,2,9],
    [0,0,0],
    [9,1,9]
]
print(mining(goldMine))