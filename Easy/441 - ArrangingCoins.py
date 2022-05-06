# link to the problem - https://leetcode.com/problems/arranging-coins/

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# link to submission - https://leetcode.com/submissions/detail/694399525/

class Solution:
    def arrangeCoins(self, n):
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right