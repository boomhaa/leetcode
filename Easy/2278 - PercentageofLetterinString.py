# link to the problem - https://leetcode.com/problems/percentage-of-letter-in-string/

# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

# link to submission - https://leetcode.com/submissions/detail/704857844/

class Solution(object):
    def percentageLetter(self, s, letter):
        count=0
        for i in s:
            if i == letter:
                count+=1
        return int(count/len(s)*100)