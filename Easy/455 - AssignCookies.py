# link to the problem - https://leetcode.com/problems/assign-cookies/

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

# link to submission - https://leetcode.com/submissions/detail/707553598/

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ret = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ret += 1
                i += 1
                j += 1
            else:
                j += 1

        return ret
