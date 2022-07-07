# link to the problem - https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

# The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.
# The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.
# You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.
# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

# link to submission - https://leetcode.com/submissions/detail/740801352/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = [1] * n
        k -= n

        for i in range(len(s) - 1, -1, -1):
            if s[i] + k > 26:
                k -= 25
                s[i] = 26
            else:
                s[i] += k
                break

        return ''.join([chr(ord('a') + c - 1) for c in s])
