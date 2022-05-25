# link to the problem - https://leetcode.com/problems/first-unique-character-in-a-string/

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# link to submission - https://leetcode.com/submissions/detail/707039314/

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1