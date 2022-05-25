# link to the problem - https://leetcode.com/problems/valid-perfect-square/

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.

# link to submission - https://leetcode.com/submissions/detail/707031757/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            if i**2==num:
                return True
            elif i**2>num:
                return False