# link to the problem - https://leetcode.com/problems/sort-array-by-parity/

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# link to submission - https://leetcode.com/submissions/detail/695544033/

class Solution(object):
    def sortArrayByParity(self, nums):
        l=0
        r=len(nums)-1
        while r>l:
            if nums[r]%2==1:
                r-=1
            elif nums[l]%2==0:
                l+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
        return nums