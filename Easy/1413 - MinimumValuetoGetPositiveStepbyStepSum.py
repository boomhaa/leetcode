# link to the problem - https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# link to submission - https://leetcode.com/submissions/detail/697575546/

class Solution:
    def minStartValue(self, nums):
        start_value = 1
        while True:
            total = start_value
            is_valid = True
            for num in nums:
                total += num
                if total < 1:
                    is_valid = False
                    break
            if is_valid:
                return start_value
            else:
                start_value += 1