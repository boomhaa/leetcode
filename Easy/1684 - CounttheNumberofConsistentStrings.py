# link to the problem - https://leetcode.com/problems/count-the-number-of-consistent-strings/

# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

# link to submission - https://leetcode.com/submissions/detail/690003686/

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        not_in_allowed=0
        for word in words:
            for element in word:
                if element not in allowed:
                    not_in_allowed+=1
                    break
        return len(words)-not_in_allowed