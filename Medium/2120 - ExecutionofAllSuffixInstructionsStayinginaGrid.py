# link to the problem - https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

# There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).
# You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).
# The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:
# The next instruction will move the robot off the grid.
# There are no more instructions left to execute.
# Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.

# link to submission - https://leetcode.com/submissions/detail/700860561/

class Solution(object):
    def executeInstructions(self, n, startPos, s):
        answer=[]

        for i in range(len(s)):
            count=0
            x=startPos[0]
            y=startPos[1]
            for j in range(i,len(s)):
                if s[j]=="R":
                    y+=1
                elif s[j]=="L":
                    y-=1
                elif s[j]=="U":
                    x-=1
                else:
                    x+=1
                if x>=n or y>=n or x<0 or y<0:
                    break
                else:
                    count+=1
            answer.append(count)
        return answer
