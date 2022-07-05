# link to the problem - https://leetcode.com/problems/two-out-of-three/

# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

# link to submission - https://leetcode.com/submissions/detail/739099177/

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        hash_m={}
        nums1=set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        for i in nums1:
            hash_m[i]=1
        for i in nums2:
            hash_m[i]=hash_m.get(i,0)+1
        for i in nums3:
            if i in hash_m:
                hash_m[i]+=1
        ans=[i for i in hash_m if hash_m[i]>=2]
        return ans