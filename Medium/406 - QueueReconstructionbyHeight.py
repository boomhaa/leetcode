# link to the problem - https://leetcode.com/problems/queue-reconstruction-by-height/

# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
# Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

# link to submission - https://leetcode.com/submissions/detail/740715373/

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (x[0], x[1]))
        ans = [-1 for i in range(len(people))]
        for p in people:
            count = p[1]
            i = 0
            while count != 0:
                if ans[i] == -1:
                    count -= 1
                else:
                    if ans[i][0] >= p[0]:
                        count -= 1
                i += 1
            place_item = (ans.index(-1, i, len(ans)))
            ans[place_item] = p
        return ans
