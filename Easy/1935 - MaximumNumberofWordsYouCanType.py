# link to the problem - https://leetcode.com/problems/maximum-number-of-words-you-can-type/

# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard

# link to submission - https://leetcode.com/submissions/detail/702210488/

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        text=text.split()
        count=0
        for word in text :
            g=False
            for i in brokenLetters:
                if i in word:
                    g=True
                    break
            if not g:
                count+=1
        return count
