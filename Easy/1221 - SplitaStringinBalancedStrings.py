# link to the problem - https://leetcode.com/problems/split-a-string-in-balanced-strings/

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it in the maximum amount of balanced strings.
# Return the maximum amount of split balanced strings.

# link to submission - https://leetcode.com/submissions/detail/688554100/

class Solution(object):
    def balancedStringSplit(self, s):
        left_char=0
        right_char=0
        answer=0
        if len(s)==1:
            return 0
        else:
            for char in s:
                if char=="L":
                    left_char+=1
                else:
                    right_char+=1
                if left_char==right_char:
                    answer+=1
            return answer