# link to the problem - https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

# Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.

# link to submission - https://leetcode.com/submissions/detail/734198538/

from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        boundary = [nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
        low, high = min(boundary), max(boundary)
        while low + 1 < high:
            mid = low + (high - low) // 2
            if self.countSmallerOrEqual(mid, nums1, nums2) >= k:
                high = mid
            else:
                low = mid + 1
        if self.countSmallerOrEqual(low, nums1, nums2) >= k:
            return low
        else:
            return high

    def countSmallerOrEqual(self, m, nums1, nums2):
        l1, l2 = len(nums1), len(nums2)
        ans = 0
        if m >= 0:
            j1, j2 = l2 - 1, l2 - 1
            for i in range(l1):
                if nums1[i] < 0:
                    while j1 >= 0 and nums2[j1] >= m / nums1[i]:
                        j1 -= 1
                    ans += l2 - j1 - 1
                elif nums1[i] > 0:
                    while j2 >= 0 and nums2[j2] > m / nums1[i]:
                        j2 -= 1
                    ans += j2 + 1
                else:
                    ans += l2
        else:
            j1, j2 = 0, 0
            for i in range(l1):
                if nums1[i] < 0:
                    while j1 < l2 and nums2[j1] < m / nums1[i]:
                        j1 += 1
                    ans += l2 - j1
                elif nums1[i] > 0:
                    while j2 < l2 and nums2[j2] <= m / nums1[i]:
                        j2 += 1
                    ans += j2
        return ans
