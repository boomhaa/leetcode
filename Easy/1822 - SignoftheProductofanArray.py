# link to the problem - https://leetcode.com/problems/sign-of-the-product-of-an-array/

# There is a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).

# link to submission - https://leetcode.com/submissions/detail/729153954/

from typing import List

def signFunc(product):
    if product==0:
        return 0
    if product<0:
        return -1
    return 1

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product=1
        for i in nums:
            product*=i
        return signFunc(product)