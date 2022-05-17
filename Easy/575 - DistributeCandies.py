# link to the problem - https://leetcode.com/problems/distribute-candies/

# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.
# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

# link to submission - https://leetcode.com/submissions/detail/701538112/

class Solution:
    def distributeCandies(self, candyType):
        candyType.sort()
        unique_candies = 1
        for i in range(1, len(candyType)):
            if candyType[i] != candyType[i - 1]:
                unique_candies += 1
            if unique_candies == len(candyType) // 2:
                break
        return min(unique_candies, len(candyType) // 2)