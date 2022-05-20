# link to the problem - https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

# link to submission - https://leetcode.com/submissions/detail/693515363/

class Solution(object):
    def firstPalindrome(self, words):
        flag = False
        answer=''
        for word in words:
            for i in range(len(word)//2):
                if word[i]!=word[-1-i]:
                    flag=True
                    break
            if not flag:
                answer=word
                break
            flag = False
        if not flag:
            return answer