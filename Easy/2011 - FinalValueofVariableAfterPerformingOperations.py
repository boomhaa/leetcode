#link to the problem - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

#There is a programming language with only four operations and one variable X:
#++X and X++ increments the value of the variable X by 1.
#--X and X-- decrements the value of the variable X by 1.
#Initially, the value of X is 0.
#Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

#link to submission - https://leetcode.com/submissions/detail/685498755/

class Solution(object):
    def finalValueAfterOperations(self, operations):
        sum=0
        for i in range(len(operations)):
            if operations[i][0]=='-' or operations[i][-1]=='-':
                sum-=1
            else:
                sum+=1
        return sum