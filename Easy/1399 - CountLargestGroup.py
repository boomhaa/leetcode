# link to the problem - https://leetcode.com/problems/count-largest-group/

# You are given an integer n.
# Each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.

# link to submission - https://leetcode.com/submissions/detail/729164679/

from collections import Counter

class Solution:
    def digsum(self,n):
        sum1=0
        while n>0:
            sum1+=n%10
            n//=10
        return sum1

    def countLargestGroup(self, n: int) -> int:
        ans=[]
        for i in range(1,n+1):
            ans.append(self.digsum(i))
        ans=Counter(ans)
        maxi=max(ans.values())
        count=0
        for i in ans:
            if ans[i]==maxi:
                count+=1
        return count