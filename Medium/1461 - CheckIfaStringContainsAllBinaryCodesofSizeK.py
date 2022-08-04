# link to the problem - https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

# link to submission - https://leetcode.com/submissions/detail/764806681/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set([s[i:i+k] for i in range(len(s)-k+1)])) == 2**k