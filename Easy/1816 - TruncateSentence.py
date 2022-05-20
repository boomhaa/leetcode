# link to the problem - https://leetcode.com/problems/truncate-sentence/

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).
# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence sand an integer k. You want to truncate s such that it contains only the first k words. Return s after truncating it.

# link to submission - https://leetcode.com/submissions/detail/691070911/

class Solution(object):
    def truncateSentence(self, s, k):
        s=" ".join(s.split()[:k])
        return s