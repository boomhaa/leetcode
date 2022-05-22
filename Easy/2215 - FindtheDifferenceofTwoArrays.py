# link to the problem - https://leetcode.com/problems/find-the-difference-of-two-arrays/

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

# link to submission - https://leetcode.com/submissions/detail/704862236/

class Solution(object):
    def findDifference(self, nums1, nums2):
        a = []
        for c in nums1:
            if c not in nums2 and c not in a:
                a.append(c)
        b = []
        for c in nums2:
            if c not in nums1 and c not in b:
                b.append(c)
        return [a, b]
