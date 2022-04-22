#link to the problem - https://leetcode.com/problems/happy-number/

#Write an algorithm to determine if a number n is happy.
#A happy number is a number defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.

#link to submission - https://leetcode.com/submissions/detail/684639979/

class Solution(object):
    def isHappy(self, n):
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.sumOfSquare(n)
            if n==1:
                return True
        return False
    def sumOfSquare(self,n):
        summ=0
        while n:
            summ+=(n%10)**2
            n//=10
        return summ

