# link to the problem - https://leetcode.com/problems/implement-magic-dictionary/

# Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.
# Implement the MagicDictionary class:
# MagicDictionary() Initializes the object.
# void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
# bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.

# link to submission - https://leetcode.com/submissions/detail/764816281/

class MagicDictionary:

    def __init__(self):
        self.dic = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.dic[i] = 1

    def search(self, searchWord: str) -> bool:
        pre = ""
        for index in range(len(searchWord)):
            for i in range(97, 123):
                if chr(i) != searchWord[index]:
                    if (pre + chr(i) + searchWord[index + 1::]) in self.dic:
                        return True
            pre += searchWord[index]
        return False
