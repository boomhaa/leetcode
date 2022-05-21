# link to the problem - https://leetcode.com/problems/power-of-four/

# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.

# link to submission - https://leetcode.com/submissions/detail/704083368/

class Solution(object):
    def isPowerOfFour(self, n):
        i = 1
        while i < n:
            i *= 4
        return i == n