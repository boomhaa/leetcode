# link to the problem - https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

# link to submission - https://leetcode.com/submissions/detail/728316472/

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for num in nums:
            if num == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        return True