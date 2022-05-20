# link to the problem - https://leetcode.com/problems/maximum-product-of-three-numbers/

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# link to submission - https://leetcode.com/submissions/detail/689737833/

class Solution(object):
    def maximumProduct(self, nums):
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        max1, max2, max3 = -1001, -1001, -1001
        min1, min2 = 1001, 1001

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, max1 * min1 * min2)