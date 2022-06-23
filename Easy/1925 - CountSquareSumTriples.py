# link to the problem - https://leetcode.com/problems/count-square-sum-triples/

# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

# link to submission - https://leetcode.com/submissions/detail/729105316/

class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                summ=i*i+j*j
                t=int(summ**0.5)
                if t*t==summ and t<=n:
                    count+=1
        return count