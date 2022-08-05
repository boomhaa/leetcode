# link to the problem - https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.
# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

# link to submission - https://leetcode.com/submissions/detail/765681789/

from collections import Counter
from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        v = Counter(tasks)
        total = 0
        if 1 in v.values():
            return -1

        for v in v.values():
            if v % 3 == 0:
                total += v // 3
            else:
                total += (v // 3) + 1

        return total