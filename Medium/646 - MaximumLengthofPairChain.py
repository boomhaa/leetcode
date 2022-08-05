# link to the problem - https://leetcode.com/problems/maximum-length-of-pair-chain/

# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

# link to submission - https://leetcode.com/submissions/detail/765659423/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def returne(e):
            return e[1]

        pairs.sort(key=returne)
        ans = [pairs[0]]
        for c in range(1, len(pairs)):
            if pairs[c][0] > ans[-1][1]:
                ans.append(pairs[c])

        return len(ans)