# link to the problem - https://leetcode.com/problems/permutation-sequence/

# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# link to submission - https://leetcode.com/submissions/detail/729176836/

from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(list(permutations("123456789"[:n],n))[k-1])