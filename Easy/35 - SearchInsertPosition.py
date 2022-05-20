#link to the problem - https://leetcode.com/problems/implement-strstr/

#description - Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        middle=(left+right)//2
        while left<=right:
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                left=middle+1
                middle=(left+right)//2
            else:
                right=middle-1
                middle=(left+right)//2
        return middle+1
