# link to the problem - https://leetcode.com/problems/n-th-tribonacci-number/

# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

# link to submission - https://leetcode.com/submissions/detail/701542087/

class Solution:
    def tribonacci(self, n: int) -> int:
        temp={0:0,1:1,2:1}
        if n in temp:
            return temp[n]
        rst=[0]*(n+1)
        rst[0],rst[1],rst[2]=0,1,1
        for i in range(3,n+1):
            rst[i]=rst[i-1]+rst[i-2]+rst[i-3]
        return rst[n]