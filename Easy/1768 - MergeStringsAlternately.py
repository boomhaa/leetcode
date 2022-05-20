# link to the problem - https://leetcode.com/problems/merge-strings-alternately/

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# link to submission - https://leetcode.com/submissions/detail/695554211/

class Solution:
    def mergeAlternately(self, word1,word2):
        i, m, n = 0, len(word1), len(word2)
        res = []
        while i < m or i < n:
            if i < m:
                res.append(word1[i])
            if i < n:
                res.append(word2[i])
            i += 1
        return ''.join(res)