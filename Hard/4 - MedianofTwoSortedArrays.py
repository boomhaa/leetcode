# link to the problem - https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# link to submission - https://leetcode.com/submissions/detail/728232710/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer=nums1+nums2
        mer.sort()
        mid=int(len(mer)/2)-1
        if(len(mer)%2==0):
            ans=(mer[mid]+mer[mid+1])/2
        else:
            ans=mer[mid+1]
        return ans