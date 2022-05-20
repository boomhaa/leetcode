# link to the problem - https://leetcode.com/problems/count-good-triplets/

# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.

# link to submission - https://leetcode.com/submissions/detail/692907195/

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        n=len(arr)
        cnt=0
        for i in range(n):
            for j in range(i+1,n):
                t1=abs(arr[i]-arr[j])
                if(t1<=a):
                    for k in range(j+1,n):
                        t2=abs(arr[j]-arr[k])
                        t3=abs(arr[i]-arr[k])
                        if(t2<=b and t3<=c):
                            cnt+=1
        return cnt