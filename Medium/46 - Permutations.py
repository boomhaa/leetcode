# link to the problem - https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# link to submission - https://leetcode.com/submissions/detail/704011714/

class Solution(object):
    def permute(self, nums):
        result=[]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

    
