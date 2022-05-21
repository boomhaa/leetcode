# link to the problem - https://leetcode.com/problems/power-of-two/

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# link to submission - https://leetcode.com/submissions/detail/704081481/

class Solution(object):
    def isPowerOfTwo(self, n):
        i = 1
        while i < n:
            i *= 2
        return i == n