"""
Day 4 - Aug 9

Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""

string_input = input()


def capitalization(input):
    if (input.isupper() or input.islower()):
        return True
    elif (input[0].isupper() and input[1:].islower()):
        return True
    else:
        return False


"""
Time Complexity: O(n) where n = len(string_input)
"""

print(capitalization(string_input))
