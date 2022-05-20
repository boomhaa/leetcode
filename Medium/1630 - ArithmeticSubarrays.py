# link to the problem - https://leetcode.com/problems/arithmetic-subarrays/

# A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.
# You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.
# Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

# link to submission - https://leetcode.com/submissions/detail/695530002/

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        answer=[]
        for i in range(len(l)):
            subarray=[]
            for j in range(l[i],r[i]+1):
                subarray.append(nums[j])
            subarray.sort()
            is_arithmetic_progress=True
            b=subarray[1]-subarray[0]
            for j in range(1,len(subarray)-1):
                if subarray[j+1]-subarray[j]!=b:
                    is_arithmetic_progress=False
                    break
            answer.append(is_arithmetic_progress)
        return answer
