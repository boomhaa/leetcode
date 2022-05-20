# link to the problem - https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence.
# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.
# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

# link to submission - https://leetcode.com/submissions/detail/701512664/

class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        res, cur, t = [], 0, sum(nums) / 2

        for i in nums:
            cur += i
            res.append(i)
            if cur > t:
                return res
        return res