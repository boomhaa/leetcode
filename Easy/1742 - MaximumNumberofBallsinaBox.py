# link to the problem - https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

# You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
# Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.
# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

# link to submission - https://leetcode.com/submissions/detail/696659282/

class Solution:
    def countBalls(self, lowLimit, highLimit):
        sum1 =0
        balls = [0]*(highLimit+2)
        for i in range(lowLimit,highLimit+1):
            while i >= 10:
                sum1 += i%10
                i = i//10
            sum1+=i
            balls[sum1]+=1
            sum1=0
        return max(balls)