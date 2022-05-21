# link to the problem - https://leetcode.com/problems/move-zeroes/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# link to submission - https://leetcode.com/submissions/detail/704116937/

class Solution(object):
    def moveZeroes(self, nums):
        ls = len(nums)
        n_pos = 0
        for i in range(ls):
            if nums[i] != 0:
                temp = nums[n_pos]
                nums[n_pos] = nums[i]
                nums[i] = temp
                n_pos += 1
