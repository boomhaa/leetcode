# link to the problem - https://leetcode.com/problems/maximum-score-from-removing-stones/

# You are playing a solitaire game with three piles of stones of sizes a, b and c respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).
# Given three integers a, b,and c, return the maximum score you can get.

# link to submission - https://leetcode.com/submissions/detail/747555785/

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        x = sorted([a, b, c])
        ans = 0
        while (x[1]):
            ans += 1
            x[1] -= 1
            x[2] -= 1
            x.sort()
        return ans
