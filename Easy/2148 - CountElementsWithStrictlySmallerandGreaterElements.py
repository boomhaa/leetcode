# link to the problem - https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

# link to submission - https://leetcode.com/submissions/detail/728286048/

from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        minEle = nums[0]
        maxEle = nums[-1]
        count = 0
        for i in range(len(nums)):
            if minEle < nums[i] < maxEle:
                count += 1
        return count