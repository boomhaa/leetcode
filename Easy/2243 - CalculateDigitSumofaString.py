# link to the problem - https://leetcode.com/problems/calculate-digit-sum-of-a-string/

# You are given a string s consisting of digits and an integer k.
# A round can be completed if the length of s is greater than k. In one round, do the following:
# Divide s into consecutive groups of size k such that the first k characters are in the first group, the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.
# Replace each group of s with a string representing the sum of all its digits. For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.
# Merge consecutive groups together to form a new string. If the length of the string is greater than k, repeat from step 1.
# Return s after all rounds have been completed.

# link to submission - https://leetcode.com/submissions/detail/734848431/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            l = []
            for i in range(0, len(s), k):
                cur = s[i:i + k]
                x = 0
                for char in cur:
                    x += int(char)
                l.append(str(x))

            s = "".join(l)

        return s