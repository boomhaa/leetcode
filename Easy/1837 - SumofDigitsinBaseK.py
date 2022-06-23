# link to the problem - https://leetcode.com/problems/sum-of-digits-in-base-k/

# Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.
# After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

# link to submission - https://leetcode.com/submissions/detail/729048486/

class Solution(object):
    def sumBase(self, n, k):
        count=0
        while n>=k:
            count+=n%k
            n//=k
        count+=n
        return count
