# link to the problem - https://leetcode.com/problems/task-scheduler/

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# link to submission - https://leetcode.com/submissions/detail/765689086/

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ret = Counter(tasks)
        maxfreq = max(ret.values())
        count = 0
        for val in ret.values():
            if val == maxfreq:
                count += 1
        return max(maxfreq + (maxfreq - 1) * n + count - 1, len(tasks))
