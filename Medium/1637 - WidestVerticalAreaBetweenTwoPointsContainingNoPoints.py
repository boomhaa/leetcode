# link to the problem - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.

# link to submission - https://leetcode.com/submissions/detail/690024903/

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        list_x=[coordinates[0] for coordinates in points]
        list_x.sort()
        answer=0
        for i in range(1,len(list_x)):
            answer=max(answer, list_x[i]-list_x[i-1])
        return answer