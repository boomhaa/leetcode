# link to the problem - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# link to submission - https://leetcode.com/submissions/detail/694402341/

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s):
        counter = Counter(s)
        cnt = -1
        for c, times in counter.items():
            if cnt == -1:
                cnt = times
            elif cnt != times:
                return False
        return True