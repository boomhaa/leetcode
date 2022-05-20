# link to the problem - https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# link to submission - https://leetcode.com/submissions/detail/700885486/

class Solution(object):
    def subsets(self, nums):
        subsets = [[]]
        nums.sort()
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets