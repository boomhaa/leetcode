# link to the problem - https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

# We have n chips, where the position of the ith chip is position[i].
# We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:
# position[i] + 2 or position[i] - 2 with cost = 0.
# position[i] + 1 or position[i] - 1 with cost = 1.
# Return the minimum cost needed to move all the chips to the same position.

# link to submission - https://leetcode.com/submissions/detail/696022633/

class Solution:
    def minCostToMoveChips(self, position):
        even_cnt = 0
        odd_cnt = 0
        for i in position:
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return min(even_cnt, odd_cnt)