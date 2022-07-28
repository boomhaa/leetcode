# link to the problem - https://leetcode.com/problems/maximum-product-of-word-lengths/

# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

# link to submission - https://leetcode.com/submissions/detail/757910821/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_set = [set(w) for w in words]
        res = 0
        dic = {i: v for i, v in enumerate(words_set)}
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(dic[i].intersection(dic[j])) == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res