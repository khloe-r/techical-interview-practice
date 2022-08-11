"""

Day 5 - Aug 10

Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string). 
Note: neither binary string will contain leading 0s unless the string itself is 0 

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"

"""

input1 = input()
input2 = input()

def binarySum(num1, num2):
  return str(bin(int(num1, 2) + int(num2, 2)))[2:]

"""
Time Complexity: O(n log(m)) where n = max(len(input1), len(input2)) and m = len() of solution
"""

print(binarySum(input1, input2))