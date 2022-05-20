# link to the problem - https://leetcode.com/problems/find-target-indices-after-sorting-array/

# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# link to submission - https://leetcode.com/submissions/detail/692942269/

class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        return [i for i, num in enumerate(nums) if num == target]