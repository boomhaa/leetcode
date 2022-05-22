# link to the problem - https://leetcode.com/problems/count-prefixes-of-a-given-string/

# You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.
# Return the number of strings in words that are a prefix of s.
# A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.

# link to submission - https://leetcode.com/submissions/detail/704854780/

class Solution(object):
    def countPrefixes(self, words, s):
        count=0
        for i in words:
            if i in s:
                if s.index(i)==0:
                    count+=1


        return count
