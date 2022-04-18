#link to the problem - https://leetcode.com/problems/length-of-last-word/

#description - Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])