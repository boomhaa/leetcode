# link to the problem - https://leetcode.com/problems/number-of-provinces/

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# link to submission - https://leetcode.com/submissions/detail/765707454/

import collections

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        deque = collections.deque()
        usedcity = set()
        province = 0
        for firstcity in range(n):
            if firstcity in usedcity:
                continue
            deque.append(firstcity)
            while deque:
                city = deque.popleft()
                if city in usedcity:
                    continue
                usedcity.add(city)
                for connectedcity in range(n):
                    if isConnected[city][connectedcity] == 1:
                        deque.append(connectedcity)
            province += 1

        return province