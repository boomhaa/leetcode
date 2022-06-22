# link to the problem - https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

# You are given a string s consisting only of lowercase English letters.
# In one move, you can select any two adjacent characters of s and swap them.
# Return the minimum number of moves needed to make s a palindrome.
# Note that the input will be generated such that s can always be converted to a palindrome.

# link to submission - https://leetcode.com/submissions/detail/727377061/

class Solution:
    def minMovesToMakePalindrome(self, s):
        n=len(s)
        s=list(s)
        l,r=0,n-1
        ans=0
        while l<r:
            ll,rr=l,r
            while s[ll]!=s[rr]:
                rr-=1
            if ll==rr:
                s[rr],s[rr+1]=s[rr+1],s[rr]
                ans+=1
                continue
            else:
                while rr<r:
                    s[rr],s[rr+1]=s[rr+1],s[rr]
                    rr+=1
                    ans+=1
            l+=1
            r-=1
        return ans