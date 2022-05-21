# link to the problem - https://leetcode.com/problems/add-digits/

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# link to submission - https://leetcode.com/submissions/detail/704085218/

class Solution(object):
    def addDigits(self, num):
        if num <= 9:
            return num

        sum = 0
        while num > 9:

            sum = sum + num % 10
            num = num / 10

            if num >= 1 and num <= 9:
                sum = sum + num
                num = sum
                sum = 0

        return num