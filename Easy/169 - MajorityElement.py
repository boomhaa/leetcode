#link to the problem - https://leetcode.com/problems/majority-element/

#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.

#link to submission - https://leetcode.com/submissions/detail/684633918/

class Solution(object):
    def majorityElement(self, nums):
        heshtable = {}
        for i in nums:
            if i in heshtable:
                heshtable[i] += 1
            else:
                heshtable[i] = 1
        for i in heshtable:
            if heshtable[i] > len(nums) // 2:
                return i
print(Solution().majorityElement([3,2,3]))

