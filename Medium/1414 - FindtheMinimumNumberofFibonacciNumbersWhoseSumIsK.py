# link to the problem - https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

# Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number can be used multiple times.
# The Fibonacci numbers are defined as:
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 for n > 2.
# It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.

# link to submission - https://leetcode.com/submissions/detail/747598177/

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        ans = 0
        while fib[-1] <= k:
            fib.append(fib[-1] + fib[-2])
        for i in range(len(fib) - 1, -1, -1):
            if fib[i] <= k:
                ans += 1
                k -= fib[i]
            if k == 0:
                return ans
