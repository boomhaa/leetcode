# link to the problem - https://leetcode.com/problems/most-common-word/

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# link to submission - https://leetcode.com/submissions/detail/710550659/

from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized_str.split()
        word_count = {}
        banned_words = set(banned)

        for word in words:
            if word not in banned_words:
                word_count[word] = word_count.get(word, 0) + 1
        wordu = ""
        max_word = -1
        for wordq in words:
            if wordq not in banned_words:
                if max_word < word_count[wordq]:
                    wordu = wordq
                    max_word = word_count[wordq]
        return wordu
