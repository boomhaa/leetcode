#link to the problem - https://leetcode.com/problems/roman-to-integer/

#description - Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#I can be placed before V (5) and X (10) to make 4 and 9.
#X can be placed before L (50) and C (100) to make 40 and 90.
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.

class Solution(object):
    def romanToInt(self, s):
        i=0
        count=0
        while i<len(s):
            if s[i]=="I":
                if i<len(s)-1 and s[i+1]=="V":
                    count+=4
                    i+=2
                elif i<len(s)-1 and s[i+1]=="X":
                    count+=9
                    i+=2
                else:
                    count+=1
                    i+=1
            elif s[i]=='V':
                count+=5
                i+=1
            elif s[i]=="X":
                if i<len(s)-1 and s[i+1]=="L":
                    count+=40
                    i+=2
                elif i<len(s)-1 and s[i+1]=="C":
                    count+=90
                    i+=2
                else:
                    count+=10
                    i+=1
            elif s[i] == 'L':
                count += 50
                i += 1
            elif s[i]=="C":
                if i<len(s)-1 and s[i+1]=="D":
                    count+=400
                    i+=2
                elif i<len(s)-1 and s[i+1]=="M":
                    count+=900
                    i+=2
                else:
                    count+=100
                    i+=1
            elif s[i] == 'D':
                count += 500
                i += 1
            elif s[i] == 'M':
                count += 1000
                i += 1
        return count
