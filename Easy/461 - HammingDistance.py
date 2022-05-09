# link to the problem - https://leetcode.com/problems/hamming-distance/

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

# link to submission - https://leetcode.com/submissions/detail/696012798/

class Solution:
    def hammingDistance(self, x, y):
        return bin(x ^ y)[2:].count('1')