# link to the problem - https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# link to submission - https://leetcode.com/submissions/detail/707028921/

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        answer=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                answer.append(nums2[j])
                i+=1
                j+=1
        return answer
