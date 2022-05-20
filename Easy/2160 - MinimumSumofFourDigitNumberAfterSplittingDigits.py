#link to the problem - https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

#You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
#For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
#Return the minimum possible sum of new1 and new2.

#link to submission - https://leetcode.com/submissions/detail/686091930/

class Solution(object):
    def minimumSum(self, num):
        new_list=[]
        first=num%10
        second=num%100//10
        third=num%1000//100
        fourth=num//1000
        new_list.append(first)
        new_list.append(second)
        new_list.append(third)
        new_list.append(fourth)
        new_list.sort()
        return new_list[0]*10+new_list[3]+new_list[1]*10+new_list[2]
