# link to the problem - https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# link to submission - https://leetcode.com/submissions/detail/704112125/

class Solution(object):
    def missingNumber(self, nums):
        sum1=sum(nums)
        sum2=(1+len(nums))*len(nums)//2
        return sum2-sum1