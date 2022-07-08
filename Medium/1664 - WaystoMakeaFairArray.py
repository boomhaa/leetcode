# link to the problem - https://leetcode.com/problems/ways-to-make-a-fair-array/

# You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.
# For example, if nums = [6,1,7,4,1]:
# Choosing to remove index 1 results in nums = [6,7,4,1].
# Choosing to remove index 2 results in nums = [6,1,4,1].
# Choosing to remove index 4 results in nums = [6,1,7,4].
# An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.
# Return the number of indices that you could choose such that after the removal, nums is fair.

# link to submission - https://leetcode.com/submissions/detail/741609779/

from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        nums += [0]
        res, diff = 0, sum(nums[1::2]) - sum(nums[0::2])
        for i in range(len(nums) - 2, -1, -1):
            if i % 2 == 0:
                diff += (nums[i] - nums[i + 1])
            else:
                diff += (nums[i + 1] - nums[i])
            if diff==0:
                res+=1
        return res
