# link to the problem - https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

# You are given an array of strings words (0-indexed).
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
# Return true if you can make every string in words equal using any number of operations, and false otherwise.

# link to submission - https://leetcode.com/submissions/detail/728319472/

from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        res = {}
        countWords = 0
        for w in words:
            for c in w:
                res[c] = 1 + res.get(c, 0)
            countWords += 1
        for i in res.values():
            if i % countWords != 0:
                return False
        return True
