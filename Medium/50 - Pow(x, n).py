# link to the problem - https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# link to submission - https://leetcode.com/submissions/detail/753586496/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1/x

        else:
            if n < -1:
                x = 1 / x
                n = abs(n)
            if n%2==0:
                return self.myPow(x*x,n//2)
            else:
                return self.myPow(x,n-1)*x
