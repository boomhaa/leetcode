# link to the problem - https://leetcode.com/problems/rings-and-rods/

# There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.
# You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:
# The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
# The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.
# Return the number of rods that have all three colors of rings on them.

# link to submission - https://leetcode.com/submissions/detail/690009844/

class Solution(object):
    def countPoints(self, rings):
        colors_of_labels={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        for i in range(1,len(rings),2):
            if rings[i-1] not in colors_of_labels[int(rings[i])]:
                colors_of_labels[int(rings[i])].append(rings[i-1])
        count_of_labels=0
        for i in range(10):
            if len(colors_of_labels[i])==3:
                count_of_labels+=1
        return count_of_labels
