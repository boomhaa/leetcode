# link to the problem - https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# link to submission - https://leetcode.com/submissions/detail/704075069/

class Solution(object):
    def containsDuplicate(self, nums):
        copy_nums=set(nums)
        if len(copy_nums)==len(nums):
            return False
        return True