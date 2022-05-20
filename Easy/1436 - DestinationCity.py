# link to the problem - https://leetcode.com/problems/destination-city/

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

# link to submission - https://leetcode.com/submissions/detail/694385049/

class Solution:
    def destCity(self, paths):
        d={}
        for path in paths:
            d[path[0]]=path[1]
        des=paths[0][0]
        while(des in d):
            des=d[des]
        return des