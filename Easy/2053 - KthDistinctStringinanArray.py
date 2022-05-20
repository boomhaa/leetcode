# link to the problem - https://leetcode.com/problems/kth-distinct-string-in-an-array/

# A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.

# link to submission - https://leetcode.com/submissions/detail/696670213/

from collections import Counter

class Solution:
    def kthDistinct(self, arr, k):
        counter = Counter(arr)
        for v in arr:
            if counter[v] == 1:
                k -= 1
                if k == 0:
                    return v
        return ''