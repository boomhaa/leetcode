# link to the problem - https://leetcode.com/problems/the-kth-factor-of-n/

# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

# link to submission - https://leetcode.com/submissions/detail/757044835/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i

        if k > 0:
            return -1
