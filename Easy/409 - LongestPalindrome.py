# link to the problem - https://leetcode.com/problems/longest-palindrome/

# GGiven a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# link to submission - https://leetcode.com/submissions/detail/707048097/

class Solution(object):
    def longestPalindrome(self, s):
        sl = []
        res = 0
        for i in s:
            if i in sl:
                sl.remove(i)
                res += 2
            else:
                sl.append(i)
        return res if not sl else res + 1