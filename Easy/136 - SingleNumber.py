#link to the problem - https://leetcode.com/problems/single-number/

#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        res=0
        for n in nums:
            res = res^n
        return res

