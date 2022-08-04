# link to the problem - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

# link to submission - https://leetcode.com/submissions/detail/764808202/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            bouquet = 0
            flower = 0

            for b in bloomDay:
                if b > day and 0 < flower < k:
                    flower = 0
                if b <= day:
                    flower += 1
                if flower == k:
                    bouquet += 1
                    flower = 0
            return bouquet >= m

        if m * k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return high
