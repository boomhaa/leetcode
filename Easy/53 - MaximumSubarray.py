#link to the problem - https://leetcode.com/problems/maximum-subarray/

#description - Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        cur_sum=0
        max_sum=-1e8
        for i in range(len(nums)):
            cur_sum=max(nums[i],cur_sum+nums[i])
            max_sum=max(max_sum,cur_sum)
        return max_sum