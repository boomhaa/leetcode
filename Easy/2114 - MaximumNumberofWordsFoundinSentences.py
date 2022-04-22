#link to the problem - https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

#A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#You are given an array of strings sentences, where each sentences[i] represents a single sentence.
#Return the maximum number of words that appear in a single sentence.

#link to submission - https://leetcode.com/submissions/detail/685502552/

class Solution(object):
    def mostWordsFound(self, sentences):
        new_list=[]
        for i in range(len(sentences)):
            new_list.append(len(sentences[i].split()))
        return max(new_list)