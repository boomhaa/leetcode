# link to the problem - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# A parentheses string is valid if and only if:
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# link to submission - https://leetcode.com/submissions/detail/696922548/

class Solution(object):
    def minAddToMakeValid(self, s):
        ans = bal = 0
        for symbol in s:
            bal += 1 if symbol == '(' else -1

            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
