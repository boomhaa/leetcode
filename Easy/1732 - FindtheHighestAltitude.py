# link to the problem - https://leetcode.com/problems/find-the-highest-altitude/

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points iand i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# link to submission - https://leetcode.com/submissions/detail/693548827/

class Solution(object):
    def largestAltitude(self, gain):
        road=[0]
        for i in range(len(gain)):
            road.append(road[i]+gain[i])
        return max(road)
