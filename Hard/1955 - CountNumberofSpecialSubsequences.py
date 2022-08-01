# link to the problem - https://leetcode.com/problems/count-number-of-special-subsequences/

# A sequence is special if it consists of a positive number of 0s, followed by a positive number of 1s, then a positive number of 2s.
# For example, [0,1,2] and [0,0,1,1,1,2] are special.
# In contrast, [2,1,0], [1], and [0,1,2,0] are not special.
# Given an array nums (consisting of only integers 0, 1, and 2), return the number of different subsequences that are special. Since the answer may be very large, return it modulo 109 + 7.
# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. Two subsequences are different if the set of indices chosen are different.

# link to submission - https://leetcode.com/submissions/detail/759614981/

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:

        zero = 0
        zeroone = 0
        zeroonewo = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero = 2 * zero + 1
            elif nums[i] == 1:
                zeroone = 2 * zeroone + zero
            elif nums[i] == 2:
                zeroonewo = 2 * zeroonewo + zeroone
        return (zeroonewo) % (10 ** 9 + 7)