# link to the problem - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

# You are given an integer array nums sorted in non-decreasing order.
# Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

# link to submission - https://leetcode.com/submissions/detail/747586265/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        for i in range(len(nums)):
            result[0]+=abs(nums[i]-nums[0])
        for i in range(1,len(nums)):
            result[i]=result[i-1]+(nums[i]-nums[i-1])*(2*i-len(nums))
        return result