# link to the problem - https://leetcode.com/problems/3sum-closest/

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# link to submission - https://leetcode.com/submissions/detail/741565694/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = -1
        d = 10 ** 10
        for i in range(n):
            k = i + 1
            j = n - 1
            while k < j:
                summ = nums[i] + nums[j] + nums[k]
                if summ > target:
                    j -= 1
                else:
                    k += 1
                if abs(target - summ) < d:
                    d = abs(target - summ)
                    res = summ
        return res
