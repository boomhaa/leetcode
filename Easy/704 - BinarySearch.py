# link to the problem - https://leetcode.com/problems/binary-search/

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# link to submission - https://leetcode.com/submissions/detail/738249510/

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
        return -1

