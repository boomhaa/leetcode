# link to the problem - https://leetcode.com/problems/single-number-ii/

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# link to submission - https://leetcode.com/submissions/detail/710526221/

class Solution(object):
    def singleNumber(self, nums):
        ditc=dict()
        for i in nums:
            ditc[i]=ditc.get(i,0)+1

        for i in nums:
            if ditc[i]==1:
                return i