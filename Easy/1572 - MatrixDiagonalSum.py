# link to the problem - https://leetcode.com/problems/matrix-diagonal-sum/

# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

# link to submission - https://leetcode.com/submissions/detail/693527232/

class Solution(object):
    def diagonalSum(self, mat):
        sum=0
        j=0
        for i in range(len(mat)):
            sum+=mat[i][j]
            sum+=mat[i][-1-j]
            j+=1
        if len(mat)%2==1:
            sum-=mat[len(mat)//2][len(mat)//2]
        return sum