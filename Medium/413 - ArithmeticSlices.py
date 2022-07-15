# link to the problem - https://leetcode.com/problems/arithmetic-slices/

# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.
# A subarray is a contiguous subsequence of the array.

# link to submission - https://leetcode.com/submissions/detail/747628604/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        C = []
        c = 0
        d = nums[1] - nums[0]
        for ind in range(1, n):
            if nums[ind] - nums[ind - 1] == d:
                c += 1
            else:
                d = nums[ind] - nums[ind - 1]
                C.append(c + 1)
                c = 1

        C.append(c + 1)

        def number(c):
            if c < 3:
                return 0
            else:
                return int(c * (c - 3) / 2) + 1

        ans = 0
        for c in C:
            ans += number(c)
        return ans