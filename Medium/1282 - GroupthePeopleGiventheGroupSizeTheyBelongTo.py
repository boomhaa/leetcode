# link to the problem - https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
# Return a list of groups such that each person i is in a group of size groupSizes[i].
# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

# link to submission - https://leetcode.com/submissions/detail/690019914/

class Solution(object):
    def groupThePeople(self, groupSizes):
        ans, group, next_group = [], [], []
        for i, j in enumerate(groupSizes):
            group.append((j, i))
        group.sort()
        for length, index in group:
            next_group.append(index)
            if len(next_group) == length:
                ans.append(next_group)
                next_group = []
        return ans
