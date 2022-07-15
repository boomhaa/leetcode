# link to the problem - https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# link to submission - https://leetcode.com/submissions/detail/747615494/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic= {}
        for i in strs:
            if "".join(sorted(list(i))) not in dic:
                dic["".join(sorted(list(i)))] = [i]
            else:
                dic["".join(sorted(list(i)))].append(i)
        return list(dic.values())