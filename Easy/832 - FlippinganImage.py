# link to the problem - https://leetcode.com/problems/flipping-an-image/

# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].

# link to submission - https://leetcode.com/submissions/detail/692938765/

class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in range((len(row)+1)/2):
                row[i], row[len(row)-i-1] = row[len(row)-i-1]^1, row[i]^1
        return A