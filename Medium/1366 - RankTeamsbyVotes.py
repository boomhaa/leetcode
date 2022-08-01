# link to the problem - https://leetcode.com/problems/rank-teams-by-votes/

# In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.
# Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.

# link to submission - https://leetcode.com/submissions/detail/762134912/

class Solution(object):
    def rankTeams(self, votes):
        count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}

        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1

        return "".join(sorted(votes[0], key=lambda x: count[x]))
