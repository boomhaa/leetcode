# link to the problem - https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

# You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.
# You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.
# For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.
# Return an array answer, where answer[j] is the answer to the jth query.

# link to submission - https://leetcode.com/submissions/detail/688561834/

class Solution(object):
    def countPoints(self, points, queries):
        new_list=[]
        for i in range(len(queries)):
            count=0
            for j in range(len(points)):
                if (points[j][0]-queries[i][0])**2+(points[j][1]-queries[i][1])**2<=(queries[i][2])**2:
                    count+=1
            new_list.append(count)
        return new_list