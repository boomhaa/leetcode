#link to the problem - https://leetcode.com/problems/sqrtx/

#Given a non-negative integer x, compute and return the square root of x.
#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

class Solution(object):
    def mySqrt(self, x):
        right=x
        left=0
        middle=(right+left)//2
        while right>=left:
            if middle**2==x:
                return middle
            elif middle**2<x and (middle+1)**2>x:
                return middle
            else:
                if middle**2<x:
                    left=middle+1
                    middle=(right+left)//2
                else:
                    right= middle - 1
                    middle = (right + left) // 2

