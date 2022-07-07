# link to the problem - https://leetcode.com/problems/reduce-array-size-to-the-half/

# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.
# Return the minimum size of the set so that at least half of the integers of the array are removed.

# link to submission - https://leetcode.com/submissions/detail/740739356/

from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = {}
        n = len(arr)
        m = n / 2
        cnt = 0
        for num in arr:
            dic[num] = 1 + dic.get(num, 0)
        for i in reversed(sorted(dic.values())):
            n -= i
            cnt += 1
            if n <= m:
                return cnt