# link to the problem - https://leetcode.com/problems/steps-to-make-array-non-decreasing/

# You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.
# Return the number of steps performed until nums becomes a non-decreasing array.

# link to submission - https://leetcode.com/submissions/detail/734213600/

from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        st = []
        ans = 0
        for i in nums:
            t = 0
            while st and st[-1][0] <= i:
                t = max(t, st.pop()[1])
            x = 0
            if st:
                x = t+1
            st.append([i, x])
            ans = max(ans, x)
        return ans