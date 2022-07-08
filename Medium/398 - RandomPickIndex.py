# link to the problem - https://leetcode.com/problems/random-pick-index/

# Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
# Implement the Solution class:
# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

# link to submission - https://leetcode.com/submissions/detail/741634565/

from random import randint
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.indexes={}
        self.nums=nums
        for i in range(len(nums)):
            self.indexes[nums[i]]=self.indexes.get(nums[i],[])
            y=self.indexes[nums[i]]
            y.append(i)
            self.indexes[nums[i]]=y
    def pick(self, target: int) -> int:
        return self.indexes[target][randint(0,len(self.indexes[target])-1)]
