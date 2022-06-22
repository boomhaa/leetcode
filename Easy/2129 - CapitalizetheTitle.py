# link to the problem - https://leetcode.com/problems/capitalize-the-title/

# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:
# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

# link to submission - https://leetcode.com/submissions/detail/728297454/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split()
        for i in range(len(title)):
            if len(title[i])>2:
                title[i]=title[i][:1].upper() + title[i][1:].lower()
            else:
                title[i]=title[i].lower()
        return ' '.join(title)