# link to the problem - https://leetcode.com/problems/rotate-string/

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

# link to submission - https://leetcode.com/submissions/detail/708996207/

class Solution(object):
    def rotateString(self, s, goal):
        if len(s)==len(goal) and goal in s+s:
            return True
        return False