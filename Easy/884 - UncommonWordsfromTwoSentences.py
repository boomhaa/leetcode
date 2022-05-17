# link to the problem - https://leetcode.com/problems/uncommon-words-from-two-sentences/

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# link to submission - https://leetcode.com/submissions/detail/701539548/

class Solution(object):
    def uncommonFromSentences(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1
        return [word for word in count if count[word] == 1]