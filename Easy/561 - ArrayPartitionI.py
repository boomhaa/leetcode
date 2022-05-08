# link to the problem - https://leetcode.com/problems/array-partition-i/

# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# link to submission - https://leetcode.com/submissions/detail/695548174/

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sum = 0
        for i in range(0,len(nums),2):
            sum += nums[i]
        return sum