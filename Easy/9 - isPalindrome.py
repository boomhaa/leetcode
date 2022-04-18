#link to the problem - https://leetcode.com/problems/palindrome-number/

#description - Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            x1=x
            x2=0
            while x1>0:
                x2=x2*10+x1%10
                x1//=10
            if x2==x:
                return True
            return False
