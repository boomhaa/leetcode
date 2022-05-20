# link to the problem - https://leetcode.com/problems/determine-if-string-halves-are-alike/

# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.

# link to submission - https://leetcode.com/submissions/detail/693572191/

class Solution:
    def halvesAreAlike(self, s):
        first = s[:len(s) // 2]
        second = s[len(s) // 2:]
        vowel = "aeiouAEIOU"
        first_count, second_count = 0, 0
        for letter in first:
            if letter in vowel:
                first_count += 1
        for letter in second:
            if letter in vowel:
                second_count += 1
        return first_count == second_count