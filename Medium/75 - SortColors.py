# link to the problem - https://leetcode.com/problems/sort-colors/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# link to submission - https://leetcode.com/submissions/detail/765657719/

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        a, b, c = 0, 0, 0

        for i in nums:
            if i == 0:
                a += 1
            elif i == 1:
                b += 1
            else:
                c += 1
        for i in range(len(nums)):
            if i < a:
                nums[i] = 0
            elif i < a + b:
                nums[i] = 1
            else:
                nums[i] = 2