# link to the problem - https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# link to submission - https://leetcode.com/submissions/detail/692940954/

class Solution(object):
    def reverseWords(self, s):
        return " ".join(map(lambda x:x[::-1],s.split()))
