# link to the problem - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
# Note:
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

# link to submission - https://leetcode.com/submissions/detail/740736253/

from typing import List
from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=[x for (x,y) in matches]
        losers=[y for (x,y) in matches]
        perfect_winners=list(set(winners)-set(losers))
        C=Counter(losers)
        one_lost=[loser for loser in C if C[loser]==1]
        return [sorted(perfect_winners), sorted(one_lost)]