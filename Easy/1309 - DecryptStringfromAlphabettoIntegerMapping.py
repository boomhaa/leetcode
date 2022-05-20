# link to the problem - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
# The test cases are generated so that a unique mapping will always exist.

# link to submission - https://leetcode.com/submissions/detail/693558990/

class Solution:
    def freqAlphabets(self, s):
        def get(s):
            return chr(ord('a') + int(s) - 1)

        i, n = 0, len(s)
        res = []
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                res.append(get(s[i: i + 2]))
                i += 3
            else:
                res.append(get(s[i]))
                i += 1
        return ''.join(res)