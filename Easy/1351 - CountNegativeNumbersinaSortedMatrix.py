# link to the problem - https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# link to submission - https://leetcode.com/submissions/detail/696008989/

class Solution:
    def countNegatives(self, grid):
        r, c, res = len(grid), len(grid[0]), 0
        m, n = r - 1, 0

        while m >= 0 and n < c:
            if grid[m][n] < 0:
                res += c - n
                m -= 1
            else:
                n += 1
        return res