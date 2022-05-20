# link to the problem - https://leetcode.com/problems/maximum-product-of-three-numbers/

# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# link to submission - https://leetcode.com/submissions/detail/689987793/

class Solution(object):
    def countKDifference(self, nums, k):
        count_f_pairs=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    count_f_pairs+=1
        return count_f_pairs