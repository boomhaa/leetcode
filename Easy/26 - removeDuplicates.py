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
