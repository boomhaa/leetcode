# link to the problem - https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

# You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.
# You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.
# Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
# Return the number of rectangles that can make a square with a side length of maxLen.

# link to submission - https://leetcode.com/submissions/detail/693557684/

class Solution(object):
    def countGoodRectangles(self, rectangles):
        maxLens=[]
        for i in rectangles:
            maxLens.append(min(i))
        maxlen=max(maxLens)
        count=0
        for i in maxLens:
            if i==maxlen:
                count+=1
        return count