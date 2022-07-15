# link to the problem - https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# link to submission - https://leetcode.com/submissions/detail/747559648/

class Solution:
    def minRemoveToMakeValid(self, s) :
        stack=[]
        split_str=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if len(stack) !=0:
                    stack.pop()
                else:
                    split_str[i]=""
        for i in stack:
            split_str[i]=""
        return '' .join(split_str)