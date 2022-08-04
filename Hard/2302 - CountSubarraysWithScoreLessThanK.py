# link to the problem - https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

# The score of an array is defined as the product of its sum and its length.
# For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
# Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.
# A subarray is a contiguous sequence of elements within an array.

# link to submission - https://leetcode.com/submissions/detail/764832330/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = cur = l = 0
        for r, n in enumerate(nums):
            cur += n
            while cur * (r - l + 1) >= k:
                cur -= nums[l]
                l += 1
            res += r - l + 1
        return res