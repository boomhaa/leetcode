# link to the problem - https://leetcode.com/problems/rotated-digits/

# An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.
# A number is valid if each digit remains a digit after rotation. For example:
# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].

# link to submission - https://leetcode.com/submissions/detail/764777783/

class Solution:
    def rotatedDigits(self, n: int) -> int:
        a=['2','5','6','9']
        g={}
        g['0']='0'
        g['1']='1'
        g['2']='5'
        g['3']='-1'
        g['4']='-1'
        g['5']='2'
        g['6']='9'
        g['7']='-1'
        g['8']='8'
        g['9']='6'
        c=0
        for i in range(n+1):
            l=list(str(i).strip())
            p=""
            fl=0
            for j in l:
                if g[j]=='-1':
                    fl=-1
                    break
                else:
                    p=p+g[j]
            if fl==0 and p!=str(i):
                c=c+1
        return c