#link to the problem - https://leetcode.com/problems/majority-element/

#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.

#link to submission - https://leetcode.com/submissions/detail/684633918/

class Solution(object):
    def majorityElement(self, nums):
        hesh = {}
        for i in nums:
            if i in hesh:
                hesh[i] += 1
            else:
                hesh[i] = 1
        for i in hesh:
            if hesh[i] > len(nums) // 2:
                return i
print(Solution().majorityElement([3,2,3]))

