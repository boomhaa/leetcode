# link to the problem - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

# link to submission - https://leetcode.com/submissions/detail/689996832/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        string1=''
        string2=''
        for i in range(len(word1)):
            string1+=word1[i]
        for i in range(len(word2)):
            string2+=word2[i]
        if string2==string1:
            return True
        return False