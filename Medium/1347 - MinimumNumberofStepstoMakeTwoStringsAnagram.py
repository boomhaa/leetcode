# link to the problem - https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# link to submission - https://leetcode.com/submissions/detail/696932519/

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        return sum(max(0, c2[k] - c1.get(k, 0)) for k in c2)