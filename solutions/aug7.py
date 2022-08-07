"""
Day 2 - Aug 7

Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters. 
Note: a palindrome is a sequence of characters that reads the same forwards and backwards. 

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""

string_input = input()


"""
Time Complexity: O(n) where n = len(string_input)
"""

def isPalindrome(input):
  input = input.lower()
  input = list(filter(lambda x: x.islower(), input))
  reversed_input = reversed(input)

  for a, b in zip(reversed_input, input):
    if (a != b):
      return False
  return True

"""
Time Complexity: O(n) where n = len(string_input)
"""

def isPalindromeV2(input):
  input = input.lower()
  input = list(filter(lambda x: x.islower(), input))

  half = int(len(input) / 2 + 1)
  for i in range(half):
    if input[i] != input[-1 * (i+1)]:
      return False
  return True

"""
Time Complexity: O(n * m) where n = len(string_input) and m = len() of only the letters of string_input
"""

def isPalindromeV3(input):
  input = input.lower()
  input = ''.join(list(filter(lambda x: x.islower(), input)))

  return input == input[::-1]
  
print(isPalindromeV3(string_input))
