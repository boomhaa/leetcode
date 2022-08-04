# link to the problem - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

# You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.
# A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.
# Return the number of smooth descent periods.

# link to submission - https://leetcode.com/submissions/detail/764817526/

class Solution:
    def getDescentPeriods(self, A):
        res = count = 1
        for i in range(1,len(A)):
            if A[i] == A[i-1] - 1:
                count += 1
            else:
                count = 1
            res += count
        return res