# link to the problem - https://leetcode.com/problems/minimum-suffix-flips/

# You are given a 0-indexed binary string target of length n. You have another binary string s of length n that is initially set to all zeros. You want to make s equal to target.
# In one operation, you can pick an index i where 0 <= i < n and flip all bits in the inclusive range [i, n - 1]. Flip means changing '0' to '1' and '1' to '0'.
# Return the minimum number of operations needed to make s equal to target.

# link to submission - https://leetcode.com/submissions/detail/740722659/

class Solution:
    def minFlips(self, target: str) -> int:
        count=0
        prev="0"
        for i in target:
            if i!=prev:
                prev=i
                count+=1
        return count