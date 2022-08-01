# link to the problem - https://leetcode.com/problems/flip-string-to-monotone-increasing/

# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0
# Return the minimum number of flips to make s monotone increasing.

# link to submission - https://leetcode.com/submissions/detail/762087556/

class Solution(object):
    def minFlipsMonoIncr(self, S):
        P = [0]
        for x in S:
            P.append(P[-1] + int(x))

        return min(P[j] + len(S)-j-(P[-1]-P[j])
                   for j in range(len(P)))