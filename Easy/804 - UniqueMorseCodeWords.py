# link to the problem - https://leetcode.com/problems/unique-morse-code-words/

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

# link to submission - https://leetcode.com/submissions/detail/692927664/

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        result=set()
        CODE = {'a': '.-', 'b': '-...', 'c': '-.-.',
                'd': '-..', 'e': '.', 'f': '..-.',
                'g': '--.', 'h': '....', 'i': '..',
                'j': '.---', 'k': '-.-', 'l': '.-..',
                'm': '--', 'n': '-.', 'o': '---',
                'p': '.--.', 'q': '--.-', 'r': '.-.',
                's': '...', 't': '-', 'u': '..-',
                'v': '...-', 'w': '.--', 'x': '-..-',
                'y': '-.--', 'z': '--..'}
        for word in words:
            string=""
            for simvol in word:
                string+=CODE[simvol]
            result.add(string)
        return len(result)
