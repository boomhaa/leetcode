# link to the problem - https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

# ou are given two strings s and t. In one step, you can append any character to either s or t.
# Return the minimum number of steps to make s and t anagrams of each other.
# An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# link to submission - https://leetcode.com/submissions/detail/727411111/

from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        s1=Counter(s)
        t1=Counter(t)
        return sum((s1-t1).values())+sum((t1-s1).values())
