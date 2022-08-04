# link to the problem - https://leetcode.com/problems/replace-elements-in-an-array/

# You are given a 0-indexed array nums that consists of n distinct positive integers. Apply m operations to this array, where in the ith operation you replace the number operations[i][0] with operations[i][1].
# It is guaranteed that in the ith operation:
# operations[i][0] exists in nums.
# operations[i][1] does not exist in nums.
# Return the array obtained after applying all the operations.

# link to submission - https://leetcode.com/submissions/detail/764760855/

class Solution(object):
    def arrayChange(self, nums, operations):
        index_dict = {}
        for i in range(len(nums)):
            index_dict[nums[i]] = i

        for item in operations:
            index = index_dict.get(item[0])
            if index >= 0:
                nums[index] = item[1]
                index_dict[item[1]] = index

        return nums