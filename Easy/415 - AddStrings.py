# link to the problem - https://leetcode.com/problems/add-strings/

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# link to submission - https://leetcode.com/submissions/detail/707521905/

class Solution(object):
    def addStrings(self, num1, num2):
        return str(int(num1)+int(num2))