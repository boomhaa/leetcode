# link to the problem - https://leetcode.com/problems/angle-between-hands-of-a-clock/

# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
# Answers within 10^-5 of the actual value will be accepted as correct.

# link to submission - https://leetcode.com/submissions/detail/741621381/

class Solution:
    def angleClock(self, h: int, m: int) -> float:
        return min(abs(6*m - (30*h + 0.5*m )), 360-abs(6*m - (30*h + 0.5*m )))