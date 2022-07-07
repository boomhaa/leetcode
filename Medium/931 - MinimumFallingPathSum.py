# link to the problem - https://leetcode.com/problems/minimum-falling-path-sum/

# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

# link to submission - https://leetcode.com/submissions/detail/740769205/

from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        dp = [[float('inf')]*c for _ in range(r)]
        for j in range(c):
            dp[0][j] = matrix[0][j]
        for i in range(1,r):
            for j in range(c):
                dp[i][j] = matrix[i][j] + dp[i-1][j]
                if j-1>=0:
                    dp[i][j] = min((matrix[i][j]+dp[i-1][j-1]),dp[i][j])
                if j+1<c:
                    dp[i][j] = min((matrix[i][j]+dp[i-1][j+1]),dp[i][j])
        return min(dp[r-1])