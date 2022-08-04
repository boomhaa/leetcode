# link to the problem - https://leetcode.com/problems/grumpy-bookstore-owner/

# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.

# link to submission - https://leetcode.com/submissions/detail/764797533/

class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        i = 0
        j = 0
        n = len(customers)
        sumLocal = 0
        sumGlobal = 0
        while j < minutes:
            if grumpy[j] == 1: sumLocal += customers[j]
            j += 1
        sumGlobal = max(sumLocal, sumGlobal)
        while j < n:
            if grumpy[j] == 1:
                sumLocal += customers[j]
            if grumpy[i] == 1:
                sumLocal -= customers[i]
            sumGlobal = max(sumLocal, sumGlobal)
            i += 1
            j += 1
        return sum([customers[i] for i in range(n) if grumpy[i] == 0]) + sumGlobal
