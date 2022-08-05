# link to the problem - https://leetcode.com/problems/gray-code/

# An n-bit gray code sequence is a sequence of 2n integers where:
# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

# link to submission - https://leetcode.com/submissions/detail/765679238/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        l = ['0','1']
        if n == 1:
            return [0,1]
        for i in range(2,n+1):
            l_0 = l
            l_1 = l[::-1]
            for i in range(len(l_0)):
                l_0[i] = '0' + l_0[i]
            for j in range(len(l_1)):
                l_1[j] = '1' + l_1[j]
            l = l_0 + l_1
        res = []
        b = 0
        for i in l:
            res.append(int(i,2))
        return res