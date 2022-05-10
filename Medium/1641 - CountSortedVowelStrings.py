# link to the problem - https://leetcode.com/problems/count-sorted-vowel-strings/

# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

# link to submission - https://leetcode.com/submissions/detail/696927734/

class Solution:
    def countVowelStrings(self, n):
        cnt = [1] * 5
        for i in range(2, n + 1):
            for j in range(3, -1, -1):
                cnt[j] += cnt[j + 1]
        return sum(cnt)