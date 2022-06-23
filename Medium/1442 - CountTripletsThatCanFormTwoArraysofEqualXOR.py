# link to the problem - https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

# Given an array of integers arr.
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
# Let's define a and b as follows:
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
# Return the number of triplets (i, j and k) Where a == b.

# link to submission - https://leetcode.com/submissions/detail/729052569/

from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, x: List[int]) -> int:
        xors=defaultdict(int)
        l=len(x)
        for i in range(l):
            a=0
            for j in range(i,l):
                a^=x[j]
                xors[i,a]+=1
        ans=0
        for i in range(l):
            a=0
            for j in range(i,l-1):
                a^=x[j]
                ans+=xors[j+1,a]
        return ans