# link to the problem - https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

# TYou have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. You are given two 0-indexed integer arrays plantTime and growTime, of length n each:
# plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting exactly one seed. You do not have to work on planting the same seed on consecutive days, but the planting of a seed is not complete until you have worked plantTime[i] days on planting it in total.
# growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last day of its growth, the flower blooms and stays bloomed forever.
# From the beginning of day 0, you can plant the seeds in any order.
# Return the earliest possible day where all seeds are blooming.

# link to submission - https://leetcode.com/submissions/detail/695999023/

class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        order = list(range(len(growTime)))
        order.sort(key=lambda x: growTime[x], reverse=True)
        result = curr = 0
        for i in order:
            curr += plantTime[i]
            result = max(result, curr+growTime[i])
        return result
