# link to the problem - https://leetcode.com/problems/custom-sort-string/

# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.

# link to submission - https://leetcode.com/submissions/detail/727421796/

from collections import Counter

class Solution(object):
    def customSortString(self, S, T):
        result = ''
        count = Counter(T)
        for c in S:
            if c in count:
                result += c * count[c]
                count[c] = 0
        for c in count:
            result += c * count[c]
        return result
