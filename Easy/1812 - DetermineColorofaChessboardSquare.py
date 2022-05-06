# link to the problem - https://leetcode.com/problems/determine-color-of-a-chessboard-square/

# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
# Return true if the square is white, and false if the square is black.
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

# link to submission - https://leetcode.com/submissions/detail/694387053/

class Solution(object):
    def squareIsWhite(self, coordinates):
        x = coordinates[0]
        y = coordinates[1]
        if ((ord(x)-ord('a')+1)+int(y)) % 2 != 0:
            return True
        return False