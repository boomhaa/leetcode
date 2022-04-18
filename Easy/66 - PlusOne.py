#link to the problem - https://leetcode.com/problems/plus-one/

#description - You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
#The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.

class Solution(object):
    def plusOne(self, digits):
        number=0
        for i in range(len(digits)):
            number=number*10+digits[i]
        number+=1
        new_list=[]
        while number>0:
            new_list=[number%10]+new_list
            number//=10
        return new_list
