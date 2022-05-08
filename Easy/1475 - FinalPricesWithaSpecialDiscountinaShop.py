# link to the problem - https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

# Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.
# Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

# link to submission - https://leetcode.com/submissions/detail/695560412/

class Solution:
    def finalPrices(self, prices):
        for i in range(len(prices)):

            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break

        return prices