# link to the problem - https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

# Given two integer arrays startTime and endTime and given an integer queryTime.
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

# link to submission - https://leetcode.com/submissions/detail/694408599/

class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        count, n = 0, len(startTime)
        for i in range(n):
            count += startTime[i] <= queryTime <= endTime[i]
        return count