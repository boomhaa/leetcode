# link to the problem - https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

# Given a string s. In one step you can insert any character at any index of the string.
# Return the minimum number of steps to make s palindrome.
# A Palindrome String is one that reads the same backward as well as forward.

# link to submission - https://leetcode.com/submissions/detail/727370785/

class Solution(object):
    def minInsertions(self, s):
        n = len(s)
        dp = [[0 for c in range(n)] for r in range(n)]
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):
                if s[start] != s[end]:
                    dp[start][end] = 1 + min(dp[start][end-1], dp[start+1][end])
                else:
                    dp[start][end] = dp[start+1][end-1]
        return dp[0][n-1]