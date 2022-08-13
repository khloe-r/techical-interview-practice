"""

Day 7 - Aug 12

Given a string and the ability to delete at most one character, return whether or not it can form a palindrome. 
Note: a palindrome is a sequence of characters that reads the same forwards and backwards. 

Ex: Given the following strings...

"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false

"""

string_input = input()


def almostPalindrome(input):
  low = 0
  high = len(input) - 1
  skipped = False
  while low < high:
    if input[low] == input[high]:
      low += 1
      high -= 1
    else:
      if skipped:
        return False
      if input[low + 1] == input[high]:
        low += 1
        high -= 1
        skipped = True
      elif input[low] == input[high - 1]:
        low += 1
        high -= 1
        skipped = True
      else:
        return False
  return True


"""
Time Complexity: O(n) where n = len(string_input) / 2
"""

print(almostPalindrome(string_input))