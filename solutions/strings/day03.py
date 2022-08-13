"""
Day 3 - Aug 8

Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""

string_input = input()


def vaccuumCleaner(input):
    x = input.count("L") - input.count("R")
    y = input.count("U") - input.count("D")
    return x == 0 and y == 0


"""
Time Complexity: O(n) where n = len(string_input)
"""

print(vaccuumCleaner(string_input))
