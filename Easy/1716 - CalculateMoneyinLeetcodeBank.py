# link to the problem - https://leetcode.com/problems/calculate-money-in-leetcode-bank/

# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

# link to submission - https://leetcode.com/submissions/detail/705436054/

class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = 0
        week = 7
        for i in range(n):
            if i % week == 0:
                current = monday + 1
                monday = current
                others = current
            else:
                current = others + 1
                others = current
            total += current
        return total