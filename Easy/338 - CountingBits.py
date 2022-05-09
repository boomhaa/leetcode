# link to the problem - https://leetcode.com/problems/counting-bits/

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# link to submission - https://leetcode.com/submissions/detail/696019287/

class Solution(object):
    def countBits(self, n):
        answer=[]
        for i in range(n+1):
            answer.append(i.bit_count())
        return answer

