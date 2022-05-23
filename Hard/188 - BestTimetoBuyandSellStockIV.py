# link to the problem - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# link to submission - https://leetcode.com/submissions/detail/699115652/

class Solution:
    def maxProfit(self, k, prices):

        n = len(prices)
        if k >= n:
            return self.maxProfit_unlimited_transactions(prices)

        l = [0 for _ in range(k + 1)]
        g = [0 for _ in range(k + 1)]
        gmax = 0
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(k, 0, -1):
                l[j] = max(g[j - 1] + diff, l[j] + diff)
                g[j] = max(l[j], g[j])
                gmax = max(gmax, g[j])

        return gmax

    def maxProfit_unlimited_transactions(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit