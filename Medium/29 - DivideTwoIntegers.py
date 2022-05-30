# link to the problem - https://leetcode.com/problems/divide-two-integers/

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

# link to submission - https://leetcode.com/submissions/detail/710336328/

class Solution(object):
    def divide(self, dividend, divisor):
        MAX = 2147483647
        MIN = -2147483648
        if divisor == 0 or (dividend == MIN and divisor == -1) or (dividend == MAX and divisor == 1):
            return MAX
        if divisor == 0 or (dividend == MAX and divisor == -1) or (dividend == MIN and divisor == 1):
            return MIN

        if (dividend<0 and divisor<0) or (dividend>=0 and divisor>0):
            j=1
        elif (dividend>=0 and divisor<0) or (dividend<0 and divisor>0):
            j=-1

        dividend=abs(dividend)
        divisor=abs(divisor)
        div = divisor
        left = dividend
        Q = 1
        ans = 0
        while left >= divisor:
            left -= div
            ans += Q
            Q += Q
            div += div
            if left < div:
                Q = 1
                div = divisor
        if j==-1:
            ans=-ans
        return ans