# link to the problem - https://leetcode.com/problems/find-and-replace-pattern/

# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

# link to submission - https://leetcode.com/submissions/detail/740692530/

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        answer=[]
        for word in words:
            p={}
            flag=True
            for x,y in zip(word,pattern):
                if p.setdefault(x,y)!=y:
                    flag=False
                    break
            if flag and len(p.values())==len(set(p.values())):
                answer.append(word)
        return answer

