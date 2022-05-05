# link to the problem - https://leetcode.com/problems/reverse-prefix-of-word/

# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

# link to submission - https://leetcode.com/submissions/detail/693577358/

class Solution:
    def reversePrefix(self, word, ch):
        index_of_prefics = word.find(ch)
        return word if index_of_prefics == -1 else word[0:index_of_prefics + 1][::-1] + word[index_of_prefics + 1:]
