# link to the problem - https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# link to submission - https://leetcode.com/submissions/detail/765670269/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = ""
            col = ""
            box = ""
            for j in range(9):

                if board[i][j] != ".":
                    if board[i][j] not in row:
                        row += board[i][j]
                    else:
                        print(row)
                        return False

                if board[j][i] != ".":
                    if board[j][i] not in col:
                        col += board[j][i]
                    else:
                        return False

                bi = (i//3)*3 + j//3
                bj = (i%3)*3 + j%3
                if board[bi][bj] != ".":
                    if board[bi][bj] not in box:
                        box += board[bi][bj]
                    else:
                        return False
        return True