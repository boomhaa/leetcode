# link to the problem - https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

# You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].
# Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

# link to submission - https://leetcode.com/submissions/detail/741592495/

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if ((s1.count('x')+s2.count('x'))%2==1) or (s1.count('y')+s2.count('y')%2==1):
            return -1
        cnt1 = 0
        cnt2 = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i]=='x':
                    cnt1+=1
                else:
                    cnt2+=1
        ans = (cnt1)//2 + cnt2//2
        if cnt1%2==1 and cnt2%2==1:
            ans += 2
        return ans