# link to the problem - https://leetcode.com/problems/counting-words-with-a-given-prefix/

# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

# link to submission - https://leetcode.com/submissions/detail/694391296/

class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        for i in range(len(words)):
            try:
                if words[i].index(pref)==0:
                    count+=1
            except:
                pass
        return count