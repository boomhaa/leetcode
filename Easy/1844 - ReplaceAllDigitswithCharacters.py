# link to the problem - https://leetcode.com/problems/replace-all-digits-with-characters/

# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

# link to submission - https://leetcode.com/submissions/detail/692933501/

class Solution(object):
    def replaceDigits(self, s):
        for i in range(1,len(s),2):
            s=s.replace(s[i],chr(ord(s[i-1])+int(s[i])),1)
        return s
