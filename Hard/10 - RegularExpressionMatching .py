# link to the problem - https://leetcode.com/problems/regular-expression-matching/

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# link to submission - https://leetcode.com/submissions/detail/694319621/

class Solution(object):
    def isMatch(self,s,p):
        rows, columns = (len(s), len(p))
        # Base conditions
        if rows == 0 and columns == 0:
            return True
        if columns == 0:
            return False
        # DP array
        dp = [[False for j in range(columns + 1)] for i in range(rows + 1)]
        # Since empty string and empty pattern are a match
        dp[0][0] = True
        # Deals with patterns containing *
        for i in range(2, columns + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        # For remaining characters
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif j > 1 and p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[rows][columns]
