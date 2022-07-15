# link to the problem - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# link to submission - https://leetcode.com/submissions/detail/747544838/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first_index = self.bs(nums, target)
        last_index = self.mod_bs(nums, target)

        return [first_index, last_index]

    def mod_bs(self, nums, target):

        low = len(nums) - 1
        high = 0

        ind = -1

        while low >= high:

            mid = high + (low - high) // 2

            item = nums[mid]

            if item == target:
                ind = mid

            if item <= target:
                high = mid + 1
            else:
                low = mid - 1

        return ind

    def bs(self, nums, target):
        low = 0
        high = len(nums) - 1

        ind = -1

        while low <= high:

            mid = low + (high - low) // 2

            item = nums[mid]

            if item == target:
                ind = mid

            if item < target:
                low = mid + 1
            else:
                high = mid - 1

        return ind