# link to the problem - https://leetcode.com/problems/number-complement/

# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

# link to submission - https://leetcode.com/submissions/detail/739111250/

class Solution:
    def findComplement(self, num: int) -> int:
        new = ''
        for i in bin(num)[2:]:
            if i == '1':
                new += '0'
            elif i == '0':
                new += '1'
        return int(new, 2)