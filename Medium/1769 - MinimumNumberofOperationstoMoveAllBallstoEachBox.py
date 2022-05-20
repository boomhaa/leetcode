# link to the problem - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
# Each answer[i] is calculated considering the initial state of the boxes.

# link to submission - https://leetcode.com/submissions/detail/689703768/

class Solution(object):
    def minOperations(self, boxes):
        new_list=[0]*len(boxes)
        for i in range(len(boxes)):
            if boxes[i]=="1":
                for j in range(len(boxes)):
                    new_list[j]+=abs(i-j)
        return new_list
