# link to the problem - https://leetcode.com/problems/string-to-integer-atoi/

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

# link to submission - https://leetcode.com/submissions/detail/707010364/

class Solution:
    def myAtoi(self, input: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(input)
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        while index < n and input[index] == ' ':
            index += 1
        if index < n and input[index] == '+':
            sign = 1
            index += 1
        elif index < n and input[index] == '-':
            sign = -1
            index += 1
        while index < n and input[index].isdigit():
            digit = int(input[index])
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                return INT_MAX if sign == 1 else INT_MIN
            result = 10 * result + digit
            index += 1
        return sign * result