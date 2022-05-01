# link to the problem - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.
# There is one laser beam between any two security devices if both conditions are met:
# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.
# Return the total number of laser beams in the bank.

# link to submission - https://leetcode.com/submissions/detail/691068905/

class Solution(object):
    def numberOfBeams(self, bank):
        new_list=[]
        answer=0
        for i in range(len(bank)):
            count=0
            for j in range(len(bank[i])):
                if bank[i][j]=="1":
                    count+=1
            if count!=0:
                new_list.append(count)
        if len(new_list)!=1:
            for i in range(1,len(new_list)):
                answer+=new_list[i-1]*new_list[i]
            return answer
        return 0

