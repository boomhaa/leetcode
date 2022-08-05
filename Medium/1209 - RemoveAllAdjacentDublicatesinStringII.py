# link to the problem - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

# link to submission - https://leetcode.com/submissions/detail/765678207/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1
            else:
                stack.append([letter, 1])
            if stack[-1][1] == k:
                stack.pop()

        mystr = ""
        for letter, count in stack:
            mystr += (letter * count)

        return mystr