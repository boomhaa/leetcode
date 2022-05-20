# link to the problem - https://leetcode.com/problems/di-string-match/

# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

# link to submission - https://leetcode.com/submissions/detail/695541999/

class Solution(object):
    def diStringMatch(self, s):
        answer=[0]*(len(s)+1)
        l=0
        r=len(s)
        for i in range(len(s)):
            if s[i]=="I":
                answer[i]=l
                l+=1
            else:
                answer[i]=r
                r-=1
        answer[-1]=l
        return answer