# link to the problem - https://leetcode.com/problems/construct-k-palindrome-strings/

# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

# link to submission - https://leetcode.com/submissions/detail/741594723/

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s)>=k and sum(i%2 for i in Counter(s).values())<=k