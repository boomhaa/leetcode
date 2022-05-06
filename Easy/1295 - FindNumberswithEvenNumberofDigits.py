# link to the problem - https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# Given an array nums of integers, return how many of them contain an even number of digits.

# link to submission - https://leetcode.com/submissions/detail/694401051/

class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count