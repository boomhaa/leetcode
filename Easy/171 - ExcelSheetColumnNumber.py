# link to the problem - https://leetcode.com/problems/excel-sheet-column-number/

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# link to submission - https://leetcode.com/submissions/detail/727430347/

class Solution(object):
    def titleToNumber(self, columnTitle):
        num=0
        for c in columnTitle:
            num=num*26+ord(c)-ord("A")+1
        return num