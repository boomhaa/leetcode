# link to the problem - https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space

# link to submission - https://leetcode.com/submissions/detail/762121802/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i])]>0:
                nums[abs(nums[i])]=-nums[abs(nums[i])]
            else:
                return abs(nums[i])