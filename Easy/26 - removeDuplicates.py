#link to the problem - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#decription - Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

class Solution(object):
    def removeDuplicates(self, nums):
        i=1
        count_of_removed=0
        while i<len(nums):
            if nums[i]==nums[i-1]:
                count_of_removed+=1
                del nums[i]
            else:
                i+=1

        count_of_left_numbers=len(nums)
        return count_of_left_numbers
