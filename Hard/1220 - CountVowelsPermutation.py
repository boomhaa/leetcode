# link to the problem - https://leetcode.com/problems/count-vowels-permutation/

# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.

# link to submission - https://leetcode.com/submissions/detail/696641013/

class Solution(object):
    def countVowelPermutation(self, n):
        previous_permutation = [1] * 5
        graph = {
            0: (1,),
            1: (0, 2),
            2: (0, 1, 3, 4),
            3: (2, 4),
            4: (0,),
        }
        for _ in range(n - 1):
            next_permutation=[0]*5
            for node in range(5):
                for neighbour in graph[node]:
                    next_permutation[neighbour]+=previous_permutation[node]
            previous_permutation=next_permutation
        return sum(previous_permutation)%(10**9+7)
