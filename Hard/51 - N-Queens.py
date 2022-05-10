# link to the problem - https://leetcode.com/problems/n-queens/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# link to submission - https://leetcode.com/submissions/detail/696917276/

class Solution(object):
    def solveNQueens(self, n):

        cols=set()
        posDiag=set()
        negDiagn=set()
        res=[]
        board=[["."]*n for _ in range(n)]

        def making(row):

            if row==n:
                copy=["".join(rows) for rows in board]
                res.append(copy)
                return

            for col in range(n):
                if col in cols or (row+col) in posDiag or (row-col) in negDiagn:
                    continue
                cols.add(col)
                posDiag.add(row+col)
                negDiagn.add(row-col)
                board[row][col] = "Q"

                making(row+1)

                cols.remove(col)
                posDiag.remove(row+col)
                negDiagn.remove(row - col)
                board[row][col]="."
        making(0)
        return res
