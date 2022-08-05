# link to the problem - https://leetcode.com/problems/robot-bounded-in-circle/

# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
# The north direction is the positive direction of the y-axis.
# The south direction is the negative direction of the y-axis.
# The east direction is the positive direction of the x-axis.
# The west direction is the negative direction of the x-axis.
# The robot can receive one of three instructions:
# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

# link to submission - https://leetcode.com/submissions/detail/765687419/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        def move(s, direction):
            if direction == "N":
                s[1] += 1
            elif direction == "E":
                s[0] += 1
            elif direction == "W":
                s[0] -= 1
            else:
                s[1] -= 1

        def get_directionl(curr_dir):
            if curr_dir == "N":
                return "W"
            elif curr_dir == "E":
                return "N"
            elif curr_dir == "W":
                return "S"
            else:
                return "E"

        def get_directionr(curr_dir):
            if curr_dir == "N":
                return "E"
            elif curr_dir == "E":
                return "S"
            elif curr_dir == "W":
                return "N"
            else:
                return "W"

        s = [0, 0]
        d = "N"
        for i in instructions:
            if i == "G":
                move(s, d)

            elif i == "L":
                d = get_directionl(d)
            else:
                d = get_directionr(d)
        return (s[0] == 0 and s[1] == 0) or d != "N"
