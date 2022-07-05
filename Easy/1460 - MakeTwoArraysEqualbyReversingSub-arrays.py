# link to the problem - https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

# You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.
# Return true if you can make arr equal to target or false otherwise.

# link to submission - https://leetcode.com/submissions/detail/739107898/

class Solution(object):
    def canBeEqual(self, target, arr):
        d1 = dict()
        d2 = dict()
        for i in target:
            d1[i] = d1.get(i, 0) + 1
        for i in arr:
            d2[i] = d2.get(i, 0) + 1
        return d1==d2