# link to the problem - https://leetcode.com/problems/count-common-words-with-one-occurrence/

# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

# link to submission - https://leetcode.com/submissions/detail/703501924/

from collections import Counter

class Solution:
    def countWords(self, words1, words2):
        w1 = Counter(words1)
        w2 = Counter(words2)
        op = set()
        for a in w1:
            if w1[a] == 1 and w2[a] == 1:
                op.add(a)
        for a in w2:
            if w1[a] == 1 and w2[a] == 1:
                op.add(a)
        return len(op)