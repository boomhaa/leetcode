# link to the problem - https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

# The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
# The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.
# For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
# You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.
# Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

# link to submission - https://leetcode.com/submissions/detail/696665510/

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        return self.to_num(firstWord) + self.to_num(secondWord) == self.to_num(targetWord)

    def to_num(self, string):
        ans = 0
        for char in string:
            ans *= 10
            ans += ord(char) - 97
        return int(ans)