# link to the problem - https://leetcode.com/problems/consecutive-characters/

# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Given a string s, return the power of s.

# link to submission - https://leetcode.com/submissions/detail/705446482/

class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        previous = None
        for c in s:
            if c == previous:
                count += 1
            else:
                previous = c
                count = 1
            max_count = max(max_count, count)
        return max_count