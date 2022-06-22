# link to the problem - https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

# Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
# Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.

# link to submission - https://leetcode.com/submissions/detail/726760808/

class Solution(object):
    def removeOccurrences(self, s, part):
        while part in s:
            s = s.replace(part, "", 1)

        return s