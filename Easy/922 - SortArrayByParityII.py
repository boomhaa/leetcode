# link to the problem - https://leetcode.com/problems/sort-array-by-parity-ii/

# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

# link to submission - https://leetcode.com/submissions/detail/703485117/

class Solution(object):
    def sortArrayByParityII(self, nums):
        odd=[]
        even=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        answer=[]
        for i in range(len(even)):
            answer.append(even[i])
            answer.append(odd[i])
        return answer
