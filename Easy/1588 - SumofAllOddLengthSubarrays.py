# link to the problem - https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
# A subarray is a contiguous subsequence of the array.
# Return the sum of all odd-length subarrays of arr.

# link to submission - https://leetcode.com/submissions/detail/689735312/

class Solution:
    def sumOddLengthSubarrays(self, arr):
        sum_of_all_odd_subarrays = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                if (j - i) % 2 != 0:
                    sum_of_all_odd_subarrays+= sum(arr[i:j])

        return sum_of_all_odd_subarrays
