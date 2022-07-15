# link to the problem - https://leetcode.com/problems/maximum-ice-cream-bars/

# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.
# Return the maximum number of ice cream bars the boy can buy with coins coins.
# Note: The boy can buy the ice cream bars in any order.

# link to submission - https://leetcode.com/submissions/detail/747602638/

class Solution:
    def maxIceCream(self, costs, coins: int) -> int:
        costs.sort()
        x=0
        i=0
        while x<coins and i<len(costs):
            temp=costs[i]+x
            if temp<=coins:
                x=temp
                i+=1
            else:
                break
        return i