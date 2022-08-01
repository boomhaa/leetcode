# link to the problem - https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

# You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

# link to submission - https://leetcode.com/submissions/detail/762108834/

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            n = 0
            for j in range(i, len(nums)):
                n += nums[j]
                sums.append(n)
        sums.sort()

        res = 0
        for i in range(left - 1, right):
            res = (res + sums[i]) % (10 ** 9 + 7)

        return res