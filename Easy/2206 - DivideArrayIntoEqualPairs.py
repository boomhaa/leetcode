# link to the problem - https://leetcode.com/problems/divide-array-into-equal-pairs/

# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

# link to submission - https://leetcode.com/submissions/detail/695536128/

class Solution(object):
    def divideArray(self, nums):
        nums.sort()
        can=True
        for i in range(0,len(nums),2):
            if nums[i]!=nums[i+1]:
                can=False
                break
        return can