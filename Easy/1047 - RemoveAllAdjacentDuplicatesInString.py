# link to the problem - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

# link to submission - https://leetcode.com/submissions/detail/704859146/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)