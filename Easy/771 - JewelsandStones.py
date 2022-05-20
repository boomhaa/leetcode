#link to the problem - https://leetcode.com/problems/jewels-and-stones/

#You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#Letters are case sensitive, so "a" is considered a different type of stone from "A".

#link to submission - https://leetcode.com/submissions/detail/686210081/

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count_of_my_jewels=0
        for i in range(len(jewels)):
            count_of_my_jewels+=stones.count(jewels[i])
        return count_of_my_jewels