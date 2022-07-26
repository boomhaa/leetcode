# link to the problem - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

# Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:
# Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
# Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
# Reduce nums[i] to nextLargest.
# Return the number of operations to make all elements in nums equal.

# link to submission - https://leetcode.com/submissions/detail/757073594/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums, n = sorted(nums), len(nums)
        return sum([n-i if nums[i-1] != nums[i] else 0 for i in range(1, n)])