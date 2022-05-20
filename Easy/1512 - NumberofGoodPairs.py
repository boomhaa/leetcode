#link to the problem - https://leetcode.com/problems/number-of-good-pairs/

#Given an array of integers nums, return the number of good pairs.
#A pair (i, j) is called good if nums[i] == nums[j] and i < j.

#link to submission - https://leetcode.com/submissions/detail/686204258/

class Solution(object):
    def numIdenticalPairs(self, nums):
        new_dict=dict()
        count_of_pairs=0
        for i in range(len(nums)):
            if nums[i] in new_dict:
                new_dict[nums[i]]+=1
                count_of_pairs+=new_dict[nums[i]]-1
            else:
                new_dict[nums[i]]=1
        return count_of_pairs