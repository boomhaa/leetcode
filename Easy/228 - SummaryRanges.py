# link to the problem - https://leetcode.com/problems/summary-ranges/

# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

# link to submission - https://leetcode.com/submissions/detail/704078471/
class Solution():
    def summaryRanges(self,nums):
        start_index = 0
        result = []

        for i in range(len(nums)):

            if i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                continue

            if start_index == i:
                result.append(str(nums[start_index]))
            else:
                result.append(str(nums[start_index]) + "->" + str(nums[i]))

            start_index = i + 1

        return result