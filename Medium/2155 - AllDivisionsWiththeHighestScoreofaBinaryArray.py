# link to the problem - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

# You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:
# numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).
# If i == 0, numsleft is empty, while numsright has all the elements of nums.
# If i == n, numsleft has all the elements of nums, while numsright is empty.
# The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.
# Return all distinct indices that have the highest possible division score. You may return the answer in any order.

# link to submission - https://leetcode.com/submissions/detail/756993704/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        maxx=0
        m=[]
        one=nums.count(1)
        zero=0
        m.append(one)
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one-=1
            m.append(zero+one)
        maxx=max(m)
        return [i for i in range(len(m)) if m[i]==maxx]