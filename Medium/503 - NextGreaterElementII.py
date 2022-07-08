# link to the problem - https://leetcode.com/problems/next-greater-element-ii/

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# link to submission - https://leetcode.com/submissions/detail/741648218/

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        next_greater = [-1] * len(nums)
        stack = [(0, nums[0])]
        for i in range(2 * len(nums)):
            while stack and stack[-1][1] < nums[i % len(nums)]:
                next_greater[stack.pop()[0]] = nums[i % len(nums)]

            stack.append((i % len(nums), nums[i % len(nums)]))

        return next_greater