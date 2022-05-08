# link to the problem - https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

# You are given an integer array nums with the following properties:
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

# link to submission - https://leetcode.com/submissions/detail/695558488/

class Solution:
    def repeatedNTimes(self, A):
        dic = {}
        for i in A:
            if i not in dic:
                dic[i] = 1
            else:
                return i