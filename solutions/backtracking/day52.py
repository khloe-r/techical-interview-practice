"""
Day 52 - Sep 26

Given a 2D board that represents a word search puzzle and a string word, return whether or the given word can be formed in the puzzle by only connecting cells horizontally and vertically.

Ex: Given the following board and words…

board =
[
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]
word = "CAT", return true
word = "TEA", return true
word = "SEAT", return true
word = "BAT", return false
"""

def wordSnake(board, target):
  return len(wordSnakeHelper(board, target)) > 0

def wordSnakeHelper(board, target):
  if (len(target) == 1):
    locations = []
    for i in range(len(board)):
      for j in range(len(board[i])):
        if target == board[i][j]:
          locations.append([i, j])
    return locations

  opts = wordSnakeHelper(board, target[1:])
  new_opts = []
  for opt in opts:
    y_1 = opt[0]
    x_1 = opt[1]
    tar = target[0]
    by = len(board)
    bx = len(board[0])
    
    if x_1 + 1 < bx and (board[y_1][x_1 + 1] == tar):
      new_opts.append([y_1, x_1 + 1])
    if x_1 - 1 >= 0 and (board[y_1][x_1 - 1] == tar):
      new_opts.append([y_1, x_1 - 1])
    if y_1 + 1 < by and (board[y_1 + 1][x_1] == tar):
      new_opts.append([y_1 + 1, x_1])
    if y_1 - 1 >= 0 and (board[y_1 - 1][x_1] == tar):
      new_opts.append([y_1 - 1, x_1])

  return new_opts
  
"""
Time Complexity: O(xyz) where x = len(board[0]) and y = len(board) and z = len(target)
"""


board = [
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]
print(wordSnake(board, "CAT"))
print(wordSnake(board, "SEAT"))
print(wordSnake(board, "TEA"))
print(wordSnake(board, "BAT"))