# link to the problem - https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# link to submission - https://leetcode.com/submissions/detail/696019923/

class Solution(object):
    def kWeakestRows(self, mat, k):
        res = []
        for i,row in enumerate(mat):
            res.append((row.count(1),i))
        res.sort(key=lambda x:x[0])
        return[x[1] for x in res[:k]]