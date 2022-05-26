# link to the problem - https://leetcode.com/problems/third-maximum-number/

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# link to submission - https://leetcode.com/submissions/detail/707516402/

class Solution:
    def thirdMax(self, nums):
        fst, scd, trd = float('-inf'), float('-inf'), float('-inf')

        for num in nums:
            if num > fst:
                fst, scd, trd = num, fst, scd
            elif num == fst:
                continue
            elif num > scd:
                scd, trd = num, scd
            elif num == scd:
                continue
            elif num > trd:
                trd = num
            else:
                continue

        if trd > float('-inf'):
            return trd
        else:
            return fst
