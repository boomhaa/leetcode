# link to the problem - https://leetcode.com/problems/non-decreasing-array/

# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# link to submission - https://leetcode.com/submissions/detail/734227891/

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        unstable = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                unstable += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

                if unstable > 1:
                    return False
        return True