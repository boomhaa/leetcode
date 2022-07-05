# link to the problem - https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

# You are given a 0-indexed string num of length n consisting of digits.
# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

# link to submission - https://leetcode.com/submissions/detail/739090988/

class Solution(object):
    def digitCount(self, num):
        values=dict()
        times=dict()
        for i in range(len(num)):
            values[i]=int(num[i])
            times[int(num[i])]=times.get(int(num[i]),0)+1
        for i in range(len(values)):
            time=times.get(i,0)
            if values[i]!=time:
                return False
        return True