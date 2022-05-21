# link to the problem - https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# link to submission - https://leetcode.com/submissions/detail/704076030/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        check = set()
        for i in range(len(nums)):
            if i > k:
                check.remove(nums[i - k - 1])
            if nums[i] in check:
                return True
            else:
                check.add(nums[i])
        return False