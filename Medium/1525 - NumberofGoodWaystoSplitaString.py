# link to the problem - https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

# You are given a string s.
# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.
# Return the number of good splits you can make in s.

# link to submission - https://leetcode.com/submissions/detail/704046707/

class Solution:
    def numSplits(self, s):
        n = len(s)
        ans = 0
        seen = set()
        prefix = [0] * n
        suffix = [0] * n

        for i in range(n):
          seen.add(s[i])
          prefix[i] = len(seen)

        seen.clear()

        for i in reversed(range(n)):
          seen.add(s[i])
          suffix[i] = len(seen)

        for i in range(n - 1):
          if prefix[i] == suffix[i + 1]:
            ans += 1

        return ans