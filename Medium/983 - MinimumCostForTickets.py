# link to the problem - https://leetcode.com/problems/minimum-cost-for-tickets/

# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
# Train tickets are sold in three different ways:
# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

# link to submission - https://leetcode.com/submissions/detail/747639059/

from collections import deque
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        dp7 = deque()
        dp30 = deque()
        res = 0
        for day in days:
            while dp7 and dp7[0][0] <= day - 7:
                dp7.popleft()
            while dp30 and dp30[0][0] <= day - 30:
                dp30.popleft()
            dp7.append((day, res + cost[1]))
            dp30.append((day, res + cost[2]))
            res = min(res + cost[0], dp7[0][1], dp30[0][1])
        return res
