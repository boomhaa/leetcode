# link to the problem - https://leetcode.com/problems/candy/

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# link to submission - https://leetcode.com/submissions/detail/710568902/

class Solution(object):
    def candy(self, ratings):
        sum_temp = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                sum_temp[i] = sum_temp[i-1] + 1

        for i in range(1, len(ratings)):
            if ratings[len(ratings)-i-1] > ratings[len(ratings)-i]:
                sum_temp[len(ratings)-i-1] = max(sum_temp[len(ratings)-i] + 1, sum_temp[len(ratings)-i-1])

        return sum(sum_temp)