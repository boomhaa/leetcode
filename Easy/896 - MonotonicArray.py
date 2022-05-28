# link to the problem - https://leetcode.com/problems/monotonic-array/

# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# link to submission - https://leetcode.com/submissions/detail/709017104/

class Solution(object):
    def isMonotonic(self, nums):
        increase=[nums[i]<=nums[i+1] for  i in range(len(nums)-1)]
        decrease=[nums[i]>=nums[i+1] for  i in range(len(nums)-1)]
        return all(decrease) or all(increase)