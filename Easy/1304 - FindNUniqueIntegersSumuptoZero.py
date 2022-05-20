# link to the problem - https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

# Given an integer n, return any array containing n unique integers such that they add up to 0.

# link to submission - https://leetcode.com/submissions/detail/694405532/

class Solution:
    def sumZero(self, n):
        ans=[]
        for i in range(1,n//2+1):
            ans.append(i)
            ans.append(-i)
        if n % 2 !=0:
            ans.append(0)
        return ans