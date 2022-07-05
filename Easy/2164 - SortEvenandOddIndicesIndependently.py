# link to the problem - https://leetcode.com/problems/sort-even-and-odd-indices-independently/

# You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:
# Sort the values at odd indices of nums in non-increasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
# Sort the values at even indices of nums in non-decreasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
# Return the array formed after rearranging the values of nums.

# link to submission - https://leetcode.com/submissions/detail/739125291/

class Solution(object):
    def sortEvenOdd(self, nums):
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd=sorted(odd, reverse=True)
        even.sort()
        new=[]
        for i in range(len(nums)//2):
            new.append(even[i])
            new.append(odd[i])
        if len(nums)%2==1:
            new.append(even[-1])
        return new