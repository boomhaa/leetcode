# link to the problem - https://leetcode.com/problems/optimal-division/

# You are given an integer array nums. The adjacent integers in nums will perform the float division.
# For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
# However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.
# Return the corresponding expression that has the maximum value in string format.
# Note: your expression should not contain redundant parenthesis.

# link to submission - https://leetcode.com/submissions/detail/762082871/

class Solution(object):
    def optimalDivision(self, nums):
        list_length = len(nums)

        if list_length == 1:
            return str(nums[0])
        elif list_length == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            res = str(nums[0]) + '/(' + str(nums[1])
            for i in range(2, list_length):
                res += '/' + str(nums[i])
            res += ')'
            return res
