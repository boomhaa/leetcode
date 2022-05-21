# link to the problem - https://leetcode.com/problems/power-of-three/

# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# link to submission - https://leetcode.com/submissions/detail/704082259/

class Solution(object):
    def isPowerOfThree(self, n):
        i = 1
        while i < n:
            i *= 3
        return i == n