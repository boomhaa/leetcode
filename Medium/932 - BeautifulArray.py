# link to the problem - https://leetcode.com/problems/beautiful-array/

# An array nums of length n is beautiful if:
# nums is a permutation of the integers in the range [1, n].
# For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
# Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

# link to submission - https://leetcode.com/submissions/detail/747617054/

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            res = []
            for el in ans:
                if 2 * el - 1 <= n:
                    res.append(el * 2 - 1)

            for el in ans:
                if 2 * el <= n:
                    res.append(el * 2)

            ans = res
        return ans
