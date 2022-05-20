# link to the problem - https://leetcode.com/problems/rearrange-array-elements-by-sign/

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should rearrange the elements of nums such that the modified array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

# link to submission - https://leetcode.com/submissions/detail/692894013/

class Solution(object):
    def rearrangeArray(self, nums):
        positive_integers,negative_integers=[],[]
        for elem in nums:
            if elem>=0:
                positive_integers.append(elem)
            else:
                negative_integers.append(elem)
        result=[]
        for i in range(len(positive_integers)):
            result.append(positive_integers[i])
            result.append(negative_integers[i])
        return result
