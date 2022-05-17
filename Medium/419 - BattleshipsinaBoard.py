# link to the problem - https://leetcode.com/problems/battleships-in-a-board/

# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

# link to submission - https://leetcode.com/submissions/detail/700885486/

class Solution(object):
    def countBattleships(self, board):
        row, col = len(board), len(board[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    flag = 1

                    if j >= 1 and board[i][j - 1] == 'X':
                        flag = 0
                    if i >= 1 and board[i - 1][j] == 'X':
                        flag = 0
                    count += flag

        return count