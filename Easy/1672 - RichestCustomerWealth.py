#link to the problem - https://leetcode.com/problems/richest-customer-wealth/

#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i-th customer has in the j-th bank. Return the wealth that the richest customer has.
#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

#link to submission - https://leetcode.com/submissions/detail/685492055/

class Solution(object):
    def maximumWealth(self, accounts):
        new_list=[]
        for i in range(len(accounts)):
            new_list.append(sum(accounts[i]))
        return max(new_list)