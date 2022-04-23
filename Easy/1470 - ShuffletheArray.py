#link to the problem - https://leetcode.com/problems/shuffle-the-array/

#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].

#link to submission - https://leetcode.com/submissions/detail/686080105/

class Solution(object):
    def shuffle(self, nums, n):
        new_list=[]
        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[n+i])
        return new_list