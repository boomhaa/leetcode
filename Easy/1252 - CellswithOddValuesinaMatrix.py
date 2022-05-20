# link to the problem - https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
# For each location indices[i], do both of the following:
# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

# link to submission - https://leetcode.com/submissions/detail/693566728/

class Solution(object):
    def oddCells(self, m, n, indices):
        matrix=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(indices)):
            for j in range(n):
                matrix[indices[i][0]][j]+=1
            for j in range(m):
                matrix[j][indices[i][1]]+=1
        count_odd_numbers=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]%2==1:
                    count_odd_numbers+=1
        return count_odd_numbers
