# link to the problem - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums.
# Note: Subsets with the same elements should be counted multiple times.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

# link to submission - https://leetcode.com/submissions/detail/693558990/

class Solution:
    def subsetXORSum(self, nums):
        def dfs(nums, depth, prev):
            self.res += prev
            for num in nums[depth:]:
                prev ^= num
                depth += 1
                dfs(nums, depth, prev)
                prev ^= num

        self.res = 0
        dfs(nums, 0, 0)
        return self.res