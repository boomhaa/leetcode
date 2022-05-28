# link to the problem - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
# Note that the letters wrap around.
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

# link to submission - https://leetcode.com/submissions/detail/708976136/

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand