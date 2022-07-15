# link to the problem - https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# link to submission - https://leetcode.com/submissions/detail/747636995/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for x in range(len(nums)):
            res[x] *= prefix
            prefix *= nums[x]
        postfix = 1
        for x in range(len(nums)-1,-1,-1):
            res[x] *= postfix
            postfix *= nums[x]
        return res