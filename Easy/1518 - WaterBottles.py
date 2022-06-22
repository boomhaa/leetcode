# link to the problem - https://leetcode.com/problems/water-bottles/

# There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

# link to submission - https://leetcode.com/submissions/detail/728281161/

class Solution:
    def numWaterBottles(self, numB: int, numE: int) -> int:
        drank = numB
        exch, empty = 0, numB

        while empty >= numE:

            exch, rem = divmod(empty, numE)
            drank += exch
            empty = exch + rem


        return drank