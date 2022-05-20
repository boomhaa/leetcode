# link to the problem - https://leetcode.com/problems/finding-the-users-active-minutes/

# You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.
# Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.
# The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.
# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.
# Return the array answer as described above.

# link to submission - https://leetcode.com/submissions/detail/693588393/

class Solution(object):
    def findingUsersActiveMinutes(self,logs, k):
        dict = {}
        for item in logs:
            id = item[0]
            minute = item[1]
            if id not in dict.keys():
                dict[id]=[]
                dict[id].append(minute)
            else:
                dict[id].append(minute)
        nums = [0 for _ in range(k)]
        for id in dict.keys():
            num = len(set(dict[id]))
            nums[num - 1] = nums[num - 1] + 1
        return nums