# link to the problem - https://leetcode.com/problems/positions-of-large-groups/

# In a string s of lowercase letters, these letters form consecutive groups of the same character.
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
# A group is considered large if it has 3 or more characters.
# Return the intervals of every large group sorted in increasing order by start index.

# link to submission - https://leetcode.com/submissions/detail/708998038/

class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans