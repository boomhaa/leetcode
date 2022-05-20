# link to the problem - https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

# Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
# A substring is a contiguous sequence of characters within a string.

# link to submission - https://leetcode.com/submissions/detail/692941632/

class Solution(object):
    def numOfStrings(self, patterns, word):
        return sum(1 for p in patterns if p in word)