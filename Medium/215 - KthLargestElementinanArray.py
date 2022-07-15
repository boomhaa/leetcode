# link to the problem - https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

# link to submission - https://leetcode.com/submissions/detail/747611467/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]