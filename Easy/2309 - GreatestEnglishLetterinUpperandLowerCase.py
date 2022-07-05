# link to the problem - https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
# An English letter b is greater than another letter a if b appears after a in the English alphabet.

# link to submission - https://leetcode.com/submissions/detail/734853317/

class Solution(object):
    def greatestLetter(self, s):
        res = ""

        for i in s:
            if (i.islower() and i.upper() in s) or (i.isupper() and i.lower() in s):
                res = max(res, i.upper())

        return res