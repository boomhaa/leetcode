#link to the problem - https://leetcode.com/problems/valid-parentheses/

#description - Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        brackets=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                brackets.append(s[i])
            elif (s[i]==")" or s[i]=="]" or s[i]=="}") and i==0:
                return False
            elif s[i]==")" and len(brackets)!=0 and brackets[-1]=="(":
                brackets.pop()
            elif s[i] == "]" and len(brackets)!=0 and brackets[-1] == "[":
                brackets.pop()
            elif s[i] == "}" and len(brackets)!=0 and brackets[-1] == "{":
                brackets.pop()
            else:
                return False
        if len(brackets)==0:
            return True
        return False
