# link to the problem - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

# Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.

# link to submission - https://leetcode.com/submissions/detail/757009324/

from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = num / 3
        if not n % 1:
            return [int(n) - 1, int(n), int(n) + 1]
        return []
