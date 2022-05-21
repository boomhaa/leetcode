# link to the problem - https://leetcode.com/problems/reverse-vowels-of-a-string/

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

# link to submission - https://leetcode.com/submissions/detail/704115179/

class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        vowels=["a","o","u","i","e","A","O","U","I","E"]
        left=0
        right=len(s)-1
        while left<right:
            if s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
            else:
                s[left], s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)
print(Solution().reverseVowels("aA"))