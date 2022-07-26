# link to the problem - https://leetcode.com/problems/sum-of-even-numbers-after-queries/

# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].
# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.
# Return an integer array answer where answer[i] is the answer to the ith query.

# link to submission - https://leetcode.com/submissions/detail/757129318/

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0:
                S -= A[k]
            A[k] += x
            if A[k] % 2 == 0:
                S += A[k]
            ans.append(S)
        return ans

        return ans