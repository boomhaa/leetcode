# link to the problem - https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
# In one move, you can increment n - 1 elements of the array by 1.

# link to submission - https://leetcode.com/submissions/detail/765692827/

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)