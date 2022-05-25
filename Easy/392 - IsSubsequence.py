# link to the problem - https://leetcode.com/problems/is-subsequence/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# link to submission - https://leetcode.com/submissions/detail/707046529/

class Solution:
    def isSubsequence(self, s, t):
        ls = len(s)
        if ls == 0:
            return True
        i = 0

        for c in t:
            if c == s[i]:
                i += 1
                if i == ls:
                    return True
        return False