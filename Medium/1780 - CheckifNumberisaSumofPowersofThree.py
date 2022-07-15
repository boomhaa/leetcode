# link to the problem - https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
# An integer y is a power of three if there exists an integer x such that y == 3x.

# link to submission - https://leetcode.com/submissions/detail/747607812/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 0:
            if n % 3 == 2:
                return False
            n = n // 3
        return True
