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
