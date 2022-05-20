# link to the problem - https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

# Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
# The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.

# link to submission - https://leetcode.com/submissions/detail/694394747/

class Solution:
    def generateTheString(self, n):
        return 'a'*(n - 1) + ('a' if n % 2 else 'b')