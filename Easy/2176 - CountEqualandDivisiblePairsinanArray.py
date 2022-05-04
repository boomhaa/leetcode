# link to the problem - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

# link to submission - https://leetcode.com/submissions/detail/692923890/

class Solution(object):
    def countPairs(self, nums, k):
        cnt=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    cnt+=1
        return cnt