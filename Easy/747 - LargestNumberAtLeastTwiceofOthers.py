# link to the problem - https://leetcode.com/problems/largest-number-at-least-twice-of-others/

# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

# link to submission - https://leetcode.com/submissions/detail/708994454/

class Solution:
    def dominantIndex(self, nums):
        m = 0
        for i in range(len(nums)):
            if nums[i] >= m:
                m = nums[i]
                m_index = i
        for i in range(len(nums)):
            if 2 * nums[i] > m and i != m_index:
                return -1
        return m_index