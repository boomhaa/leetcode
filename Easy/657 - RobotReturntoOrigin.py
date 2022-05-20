# link to the problem - https://leetcode.com/problems/robot-return-to-origin/

# There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

# link to submission - https://leetcode.com/submissions/detail/695561517/

class Solution(object):
    def judgeCircle(self, moves):
        x=0
        y=0
        for i in moves:
            if i=="U":
                y+=1
            elif i=="D":
                y-=1
            elif i=="L":
                x-=1
            else:
                x+=1
        if x==y==0:
            return True
        return False