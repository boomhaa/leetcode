# link to the problem - https://leetcode.com/problems/number-of-segments-in-a-string/

# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.

# link to submission - https://leetcode.com/submissions/detail/707530395/

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())