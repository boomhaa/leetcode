# link to the problem - https://leetcode.com/problems/remove-outermost-parentheses/

# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# link to submission - https://leetcode.com/submissions/detail/692934404/

class Solution(object):
    def removeOuterParentheses(self, S):
        target =''
        count, i = 1, 1
        while i< len(S):
            count += 1 if S[i]=="(" else -1
            if count == 0:
                i += 2
                count += 1
                continue
            target += S[i]
            i += 1
        return target