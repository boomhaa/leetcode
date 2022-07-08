# link to the problem - https://leetcode.com/problems/max-consecutive-ones-iii/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# link to submission - https://leetcode.com/submissions/detail/741640519/

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = ans = 0
        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                while nums[l] != 0:
                    l += 1
                k += 1
                l += 1
            r += 1
            ans = max(ans, (r - l))
        return ans
