# link to the problem - https://leetcode.com/problems/sum-of-subarray-ranges/

# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
# Return the sum of all subarray ranges of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.

# link to submission - https://leetcode.com/submissions/detail/757909364/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        total = 0
        left = 0
        right = 1
        mx = nums[left]
        mn = nums[left]

        while left >= 0 and right < len(nums):
            mx = max(mx, nums[right])
            mn = min(mn, nums[right])
            total += mx - mn

            if right == len(nums) - 1:
                left += 1
                right = left + 1
                mx = nums[left]
                mn = nums[left]
            else:
                right += 1

        return total