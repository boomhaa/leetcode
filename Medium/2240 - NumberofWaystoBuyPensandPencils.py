# link to the problem - https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

# You are given an integer total indicating the amount of money you have. You are also given two integers cost1 and cost2 indicating the price of a pen and pencil respectively. You can spend part or all of your money to buy multiple quantities (or none) of each kind of writing utensil.
# Return the number of distinct ways you can buy some number of pens and pencils.

# link to submission - https://leetcode.com/submissions/detail/764819947/

class Solution:
    def waysToBuyPensPencils(self, t: int, m: int, n: int) -> int:
        a = t // m
        res = 0
        for x in range(0, a + 1):
            res += 1 + (t-m*x)//n

        return res