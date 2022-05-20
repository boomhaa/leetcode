#link to the problem - https://leetcode.com/problems/pascals-triangle/

#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution(object):
    def generate(self, numRows):
        new_list=[[1]]
        for i in range(2,numRows+1):
            if i==2:
                new_list.append([1,1])
            else:
                new_list2=[1]
                for j in range(len(new_list[-1])-1):
                    new_list2.append(new_list[-1][j]+new_list[-1][j+1])
                new_list2.append(1)
                new_list.append(new_list2)
        return new_list
