#link to the problem - https://leetcode.com/problems/concatenation-of-array/

#GGiven a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
#A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

#link to submission - https://leetcode.com/submissions/detail/684734681/

class Solution(object):
    def getConcatenation(self, nums):
        new_list=[0]*2*len(nums)
        for i in range(len(nums)):
            new_list[i]=nums[i]
            new_list[len(nums)+i]=nums[i]
        return new_list
