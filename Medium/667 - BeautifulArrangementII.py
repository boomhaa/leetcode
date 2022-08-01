# link to the problem - https://leetcode.com/problems/beautiful-arrangement-ii/

# Given two integers n and k, construct a list answer that contains n different positive integers ranging from 1 to n and obeys the following requirement:
# Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
# Return the list answer. If there multiple valid answers, return any of them.

# link to submission - https://leetcode.com/submissions/detail/762071212/

class Solution(object):
    class Solution(object):
        def constructArray(self, n: int, k: int) -> List[int]:
            m = n - k
            ans = list(range(1, m))
            while 1:
                if m <= n:
                    ans.append(m)
                    m += 1
                else:
                    break
                if m <= n:
                    ans.append(n)
                    n -= 1
                else:
                    break

            return ans