#link to the problem - https://leetcode.com/problems/remove-element/

#description - Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.

class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while i<len(nums):
            if nums[i]==val:
                del nums[i]
            else:
                i+=1
        return len(nums)
