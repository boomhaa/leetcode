# link to the problem - https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# link to submission - https://leetcode.com/submissions/detail/705397702/

class Solution(object):
    def reverse(self, x):
        copy_x=x
        r = 0
        x=abs(x)
        while x != 0:
            r *= 10
            r += x % 10
            x //= 10
        if copy_x<0:
            r-=2*r
        if r>2**31-1 or r<-2**31:
            return 0
        return r