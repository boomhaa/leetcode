# link to the problem - https://leetcode.com/problems/fibonacci-number/

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# link to submission - https://leetcode.com/submissions/detail/701517977/

class Solution:
    def fib(self, N):
        if N in [0, 1]:
            return N
        pre, cur = 0, 1
        while N > 1:
            res = pre + cur
            pre = cur
            cur = res
            N -= 1
        return res