# link to the problem - https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

# You are given an m x n binary matrix matrix.
# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
# Return the maximum number of rows that have all values equal after some number of flips.

# link to submission - https://leetcode.com/submissions/detail/741636736/

from typing import List
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        h = defaultdict(int)
        for row in matrix:
            x, y = [], []
            for j, cell in enumerate(row):
                if cell == 1:
                    x.append(j)
                if cell == 0:
                    y.append(j)
            h[tuple(x)] += 1
            h[tuple(y)] += 1
        if h:
            return max(h.values())
        return 0