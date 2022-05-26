# link to the problem - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# link to submission - https://leetcode.com/submissions/detail/707543598/

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ditc={}
        for i in range(1,len(nums)+1):
            ditc[i]=0
        for i in nums:
            ditc[i]+=1
        answer=[]
        for i in range(1,len(nums)+1):
            if ditc[i]==0:
                answer.append(i)
        return answer