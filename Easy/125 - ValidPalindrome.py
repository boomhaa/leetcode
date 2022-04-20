#link to the problem - https://leetcode.com/problems/valid-palindrome/

#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
#Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        new_string=''
        for i in s:
            if i.isalpha() or i.isdigit():
                new_string+=i
        new_string=new_string.lower()
        if len(new_string)==0:
            return True
        else:
            if new_string==new_string[::-1]:
                return True
            return False
print(Solution().isPalindrome("0P"))