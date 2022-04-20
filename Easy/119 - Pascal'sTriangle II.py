#link to the problem - https://leetcode.com/problems/pascals-triangle-ii/

#Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution(object):
    def getRow(self, rowIndex):
        new_list = [[1]]
        for i in range(2, rowIndex + 2):
            if i == 2:
                new_list.append([1, 1])
            else:
                new_list2 = [1]
                for j in range(len(new_list[-1]) - 1):
                    new_list2.append(new_list[-1][j] + new_list[-1][j + 1])
                new_list2.append(1)
                new_list.append(new_list2)
