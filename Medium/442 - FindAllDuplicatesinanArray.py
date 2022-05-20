# link to the problem - https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# link to submission - https://leetcode.com/submissions/detail/702868820/

class Solution(object):
    def findDuplicates(self, nums):
        answer=[]
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                answer.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1]=-nums[abs(nums[i])-1]
        return list(map(abs,answer))