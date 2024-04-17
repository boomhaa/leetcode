#link to the problem - https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
#using the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.

#link to submission - https://leetcode.com/problems/ransom-note/submissions/1235143872/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ramsom = dict()
        counter_magazine = dict()

        for elem in ransomNote:
            counter_ramsom[elem] = counter_ramsom.get(elem, 0) + 1
        for elem in magazine:
            counter_magazine[elem] = counter_magazine.get(elem, 0) + 1
        for elem in counter_ramsom:
            if counter_magazine.get(elem,0)<counter_ramsom[elem]:
                return False
        return True