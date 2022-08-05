# link to the problem - https://leetcode.com/problems/adding-spaces-to-a-string/

# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.
# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.

# link to submission - https://leetcode.com/submissions/detail/765668035/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        ptr = 0
        for i in range(len(s)):

            if ptr < len(spaces) and spaces[ptr] == i:
                result.append(' ')
                ptr += 1

            result.append(s[i])

        return ''.join(result)