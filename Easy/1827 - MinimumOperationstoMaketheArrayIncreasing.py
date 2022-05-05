# link to the problem - https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

# You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
# For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.
# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

# link to submission - https://leetcode.com/submissions/detail/693570213/

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        pre_max = nums[0]
        times = 0
        for i in range(1, n):
            if nums[i] <= pre_max:
                steps = pre_max - nums[i] + 1
                times += steps
                pre_max = nums[i] + steps
            else:
                pre_max = nums[i]
        return times