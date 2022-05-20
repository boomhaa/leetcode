# link to the problem - https://leetcode.com/problems/sum-of-unique-elements/

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

# link to submission - https://leetcode.com/submissions/detail/695557521/

class Solution:
    def sumOfUnique(self, nums):
        s = 0
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
                s+=i
            elif i in d:
                if d[i] == 1:
                    s-=i
                    d[i]+=1
        return s