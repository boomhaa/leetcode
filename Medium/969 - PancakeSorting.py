# link to the problem - https://leetcode.com/problems/pancake-sorting/

# Given an array of integers arr, sort the array by performing a series of pancake flips.
# In one pancake flip we do the following steps:
# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.
# Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

# link to submission - https://leetcode.com/submissions/detail/707429746/

class Solution(object):
    def pancakeSort(self, arr):
        def flip(subarray, k):
            i=0
            while i<k//2:
                subarray[i],subarray[k-i-1]=subarray[k-i-1],subarray[i]
                i+=1

        value_for_sorting=len(arr)
        answer=[]
        while value_for_sorting>0:
            index=arr.index(value_for_sorting)
            if index!=value_for_sorting-1:
                if index!=0:
                    answer.append(index+1)
                    flip(arr,index+1)
                answer.append(value_for_sorting)
                flip(arr, value_for_sorting)
            value_for_sorting-=1
        return answer