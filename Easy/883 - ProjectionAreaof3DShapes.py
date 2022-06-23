# link to the problem - https://leetcode.com/problems/projection-area-of-3d-shapes/

# You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).
# We view the projection of these cubes onto the xy, yz, and zx planes.
# A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
# Return the total area of all three projections.

# link to submission - https://leetcode.com/submissions/detail/729078297/

class Solution:
    def projectionArea(self, grid):
        N = len(grid)
        ans = 0

        for i in range(N):
            best_row = 0
            best_col = 0
            for j in range(N):
                if grid[i][j]: ans += 1
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ans += best_row + best_col

        return ans