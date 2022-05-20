# link to the problem - https://leetcode.com/problems/rings-and-rods/

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# link to submission - https://leetcode.com/submissions/detail/690011441/

class Solution(object):
    def checkIfPangram(self, sentence):
        new_list=[]
        for i in range(len(sentence)):
            if sentence[i] not in new_list:
                new_list.append(sentence[i])
        if len(new_list)==26:
            return True
        return False