# link to the problem - https://leetcode.com/problems/create-target-array-in-the-given-order/

# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
# It is guaranteed that the insertion operations will be valid.

# link to submission - https://leetcode.com/submissions/detail/688547766/

class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(len(nums)):
            if len(target)==index[i]:
                target.append(nums[i])
            else:
                target=target[:index[i]]+[nums[i]]+target[index[i]:]
        return target