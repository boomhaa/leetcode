# link to the problem - https://leetcode.com/problems/shuffle-string/

# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

# link to submission - https://leetcode.com/submissions/detail/687337725/

class Solution(object):
    def restoreString(self, s, indices):
        answer=['']*len(indices)
        for i in range(len(indices)):
            answer[indices[i]]=s[i]
        return ''.join(answer)
