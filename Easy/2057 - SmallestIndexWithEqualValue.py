# link to the problem - https://leetcode.com/problems/smallest-index-with-equal-value/

# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
# x mod y denotes the remainder when x is divided by y.

# link to submission - https://leetcode.com/submissions/detail/696668174/

class Solution(object):
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if i%10==nums[i]:
                return i
        return -1