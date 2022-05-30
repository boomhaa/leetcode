# link to the problem - https://leetcode.com/problems/single-number-iii/

# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

# link to submission - https://leetcode.com/submissions/detail/710525360/

class Solution(object):
    def singleNumber(self, nums):
        ditc=dict()
        for i in nums:
            ditc[i]=ditc.get(i,0)+1
        answer=[]
        for i in nums:
            if ditc[i]==1:
                answer.append(i)
        return answer