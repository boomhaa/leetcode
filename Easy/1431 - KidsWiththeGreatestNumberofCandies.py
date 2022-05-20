#link to the problem - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

#There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
#Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
#Note that multiple kids can have the greatest number of candies.

#link to submission - https://leetcode.com/submissions/detail/686207363/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        answer=[]
        for i in range(len(candies)):
            candies_of_kid=candies[i]
            candies[i]+=extraCandies
            if max(candies)==candies_of_kid+extraCandies:
                answer.append(True)
            else:
                answer.append(False)
            candies[i]-=extraCandies
        return answer