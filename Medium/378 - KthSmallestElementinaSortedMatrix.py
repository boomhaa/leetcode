# link to the problem - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).

# link to submission - https://leetcode.com/submissions/detail/757159351/

class Solution(object):
    def kthSmallest(self, matrix, k):
        sol=matrix[0]
        for i in matrix[1:]:
            sol+=i
        sol.sort()
        return sol[k-1]