# link to the problem - https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# link to submission - https://leetcode.com/submissions/detail/687299019/

class Solution(object):
    def subtractProductAndSum(self, n):
        product=1
        sum=0
        while n>0:
            product*=n%10
            sum+=n%10
            n//=10
        return product-sum