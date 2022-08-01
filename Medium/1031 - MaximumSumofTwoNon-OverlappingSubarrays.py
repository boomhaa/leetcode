# link to the problem - https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

# Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.
# A subarray is a contiguous part of an array.

# link to submission - https://leetcode.com/submissions/detail/762091245/

class Solution(object):

    def maxSumTwoNoOverlap(self, A, L, M):
        max_final  = max_sum3 = max_sum2 = 0

        length = len(A)
        i = 0
        arr = A
        while i + L < length + 1:
            sum1 = sum(arr[i:i + L])
            print(sum1)
            max_sum2 = max_sum3 = 0
            if i >= M:
                j = 0
                while j + M < i:
                    sum2 = sum(arr[j:j + M])
                    max_sum2 = max(max_sum2, sum2)
                    j += 1
            k = i + L
            if k + M < length + 1:
                while k + M < len(A) + 1:
                    sum3 = sum(arr[k:k + M])
                    max_sum3 = max(max_sum3, sum3)
                    k += 1

            max_res = max(max_sum2, max_sum3)
            print(max_res)

            max_final = max(max_final, max_res + sum1)
            i += 1
        return max_final
