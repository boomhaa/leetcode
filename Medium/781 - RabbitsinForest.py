# link to the problem - https://leetcode.com/problems/rabbits-in-forest/

# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
# Given the array answers, return the minimum number of rabbits that could be in the forest.

# link to submission - https://leetcode.com/submissions/detail/765683276/s

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {i: 0 for i in answers}
        for i in answers:
            dic[i] += 1

        res = 0
        for i, n in dic.items():
            if dic[i] % (i + 1) == 0:
                dic[i] //= (i + 1)
            else:
                dic[i] = dic[i] // (i + 1) + 1
            res += dic[i] * (i + 1)
        return res