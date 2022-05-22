# link to the problem - https://leetcode.com/problems/intersection-of-multiple-arrays/

# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

# link to submission - https://leetcode.com/submissions/detail/704863972/

class Solution(object):
    def intersection(self, nums):
        result = set(nums[0])
        for i in range(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return sorted(result)

