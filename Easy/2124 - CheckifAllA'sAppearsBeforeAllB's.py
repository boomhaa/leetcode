# link to the problem - https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

# Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

# link to submission - https://leetcode.com/submissions/detail/701503052/

class Solution(object):
    def checkString(self, s):
        b_flag=0
        for i in s:
            if i=="a" and b_flag==1:
                return False
            if i=="b":
                b_flag=1
        return True
