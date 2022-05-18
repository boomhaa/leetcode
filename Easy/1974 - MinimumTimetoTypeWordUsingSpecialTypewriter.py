# link to the problem - https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.
# Each second, you may perform one of the following operations:
# Move the pointer one character counterclockwise or clockwise.
# Type the character the pointer is currently on.
# Given a string word, return the minimum number of seconds to type out the characters in word.

# link to submission - https://leetcode.com/submissions/detail/702207896/

class Solution:
    def minTimeToType(self, word):
        s=0
        now='a'
        for i in range(len(word)):
            move=abs(ord(word[i])-ord(now))
            if move > 13:
                move= 26 -move
            s+=(move+1)
            now=word[i]
        return s