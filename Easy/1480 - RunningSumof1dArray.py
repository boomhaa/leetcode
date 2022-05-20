#link to the problem - https://leetcode.com/problems/running-sum-of-1d-array/

#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

#link to submission - https://leetcode.com/submissions/detail/685490345/

class Solution(object):
    def runningSum(self, nums):
        new_list=[]
        for i in range(len(nums)):
            new_list.append(sum(nums[:i+1]))
        return new_list
