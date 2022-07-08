# link to the problem - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# link to submission - https://leetcode.com/submissions/detail/741689833/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices) - 1):
            ans += max(0, prices[i + 1] - prices[i])
        return ans
