# link to the problem - https://leetcode.com/problems/find-the-middle-index-in-array/

# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
# If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.
# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

# link to submission - https://leetcode.com/submissions/detail/701532001/

class Solution(object):
    def findMiddleIndex(self, nums):
        l_sum=0
        r_sum=sum(nums)-nums[0]
        if l_sum!=r_sum:
            for i in range(1,len(nums)):
                l_sum+=nums[i-1]
                r_sum-=nums[i]
                if r_sum==l_sum:
                    return i
            return -1
        else:
            return 0
