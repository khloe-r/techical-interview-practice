"""
Day 1 - Aug 6

Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""

string_input = input()


"""
Time Complexity: O(n) where n = len(string_input)
"""


def reverseString(input):
    output = ""
    for char in input:
        output = char + output
    return output


"""
Time Complexity: O(n) where n = len(string_input)
"""


def reverseStringV2(input):
    return input[::-1]


"""
Time Complexity: O(n^2) where n = len(string_input)
"""


def reverseStringV3(input):
    return ''.join(reversed(input))


print(reverseString(string_input))
