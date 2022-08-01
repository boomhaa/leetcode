# link to the problem - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# link to submission - https://leetcode.com/submissions/detail/759806013/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        currentOnes = 0
        prevOnes = 0
        maxCount = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                currentOnes += 1

            else:
                maxCount = max(maxCount, currentOnes + prevOnes)
                prevOnes = currentOnes
                currentOnes = 0
        maxCount = max(maxCount, currentOnes + prevOnes)
        return maxCount - 1 if maxCount == len(nums) else maxCount