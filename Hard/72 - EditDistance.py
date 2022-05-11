# link to the problem - https://leetcode.com/problems/edit-distance/

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# link to submission - https://leetcode.com/submissions/detail/697514174/

from collections import Counter

class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        d = [[-1 for _ in range(n+1)] for _ in range(m+1)]


        for i in range(m+1):
            d[i][0] = i
        for j in range(n+1):
            d[0][j] = j


        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j]= min(
                        d[i-1][j]+1,  # deletion
                        d[i][j-1]+1,  # insertion
                        d[i-1][j-1]+1  # substitution
                    )

        return d[-1][-1]