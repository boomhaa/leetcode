# link to the problem - https://leetcode.com/problems/increasing-decreasing-string/

# You are given a string s. Reorder the string using the following algorithm:
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
# Return the result string after sorting s with this algorithm.

# link to submission - https://leetcode.com/submissions/detail/693587021/
import collections

class Solution:
    def sortString(self, s):
        cnt, res = collections.Counter(s), []
        st = sorted(cnt.keys())

        while len(res) < len(s):
            for c in st:
                if cnt[c]:
                    res.append(c)
                    cnt[c] -= 1

            for c in st[::-1]:
                if cnt[c]:
                    res.append(c)
                    cnt[c] -= 1
        return ''.join(res)
