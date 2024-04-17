#link to the problem - https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

#Given two strings s and t, determine if they are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character while preserving the order of characters.
#No two characters may map to the same character, but a character may map to itself.

#link to submission - https://leetcode.com/problems/isomorphic-strings/submissions/1235155918/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphic_s = dict()
        isomorphic_t = dict()
        length = len(s)
        for elem in range(length):
            if s[elem] not in isomorphic_s:
                isomorphic_s[s[elem]] = t[elem]
            else:
                if isomorphic_s[s[elem]] != t[elem]:
                    return False
            if t[elem] not in isomorphic_t:
                isomorphic_t[t[elem]] = s[elem]
            else:
                if isomorphic_t[t[elem]] != s[elem]:
                    return False
        return True

