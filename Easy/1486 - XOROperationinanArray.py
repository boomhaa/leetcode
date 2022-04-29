# link to the problem - https://leetcode.com/problems/xor-operation-in-an-array/

# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

# link to submission - https://leetcode.com/submissions/detail/689724080/

class Solution(object):
    def xorOperation(self, n, start):
        result=0
        for i in range(n):
            result^=start+2*i
        return result