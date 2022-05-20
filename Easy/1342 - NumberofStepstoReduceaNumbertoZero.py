# link to the problem - https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# link to submission - https://leetcode.com/submissions/detail/688522733/

class Solution(object):
    def numberOfSteps(self, num):
        count=0
        while num>0:
            if num%2==0:
                num//=2
            else:
                num-=1
            count+=1
        return count