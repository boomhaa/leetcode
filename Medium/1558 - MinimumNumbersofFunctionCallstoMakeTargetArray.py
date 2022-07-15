# link to the problem - https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

# You are given an integer array nums. You have an integer array arr of the same length with all values set to 0 initially. You also have the following modify function:
# You want to use the modify function to covert arr to nums using the minimum number of calls.
# Return the minimum number of function calls to make nums from arr.
# The test cases are generated so that the answer fits in a 32-bit signed integer.

# link to submission - https://leetcode.com/submissions/detail/747642214/

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        if max(nums) == 0:
            return 0
        while max(nums) != 0:
            for i in range(n):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    count += 1
            if max(nums)>0:
                for i in range(n):
                    nums[i] //= 2
                count += 1
        return count