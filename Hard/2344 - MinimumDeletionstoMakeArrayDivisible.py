# link to the problem - https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

# You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.
# Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.
# Note that an integer x divides y if y % x == 0.

# link to submission - https://leetcode.com/submissions/detail/765702980/

from math import gcd
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        len_nums = len(nums)
        gcd_number = numsDivide[0]
        for num in numsDivide:
            gcd_number = gcd(gcd_number, num)
        nums.sort(reverse = True)
        while nums:
            if not(gcd_number % nums.pop()):
                return len_nums - len(nums) - 1
        return -1