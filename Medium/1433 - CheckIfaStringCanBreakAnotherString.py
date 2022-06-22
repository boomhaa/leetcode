# link to the problem - https://leetcode.com/problems/check-if-a-string-can-break-another-string/

# Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.
# A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

# link to submission - https://leetcode.com/submissions/detail/728334459/

class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        s1=sorted(s1)
        s2 = sorted(s2)
        count1=count2=0
        for i in range(len(s1)):
            if s1[i]>s2[i]:
                count1+=1
            if s1[i]<s2[i]:
                count2+=1
            if count2!=0 and count1!=0:
                return False
        return True