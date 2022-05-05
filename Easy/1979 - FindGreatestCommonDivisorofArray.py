# link to the problem - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# link to submission - https://leetcode.com/submissions/detail/693580970/

class Solution(object):
    def nod(self,num1,num2):
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 %= num2
            else:
                num2 %= num1
        return num1 or num2

    def findGCD(self, nums):
        num1=max(nums)
        num2=min(nums)
        return Solution().nod(num1,num2)
