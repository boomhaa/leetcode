# link to the problem - https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# link to submission - https://leetcode.com/submissions/detail/741565694/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            a = min(height[l], height[r]) * (r-l)
            res = max(a, res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res