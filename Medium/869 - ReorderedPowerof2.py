# link to the problem - https://leetcode.com/problems/reordered-power-of-2/

# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
# Return true if and only if we can do this so that the resulting number is a power of two.

# link to submission - https://leetcode.com/submissions/detail/757118989/

import itertools

class Solution(object):
    def reorderedPowerOf2(self, N):
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))