# link to the problem - https://leetcode.com/problems/minimum-suffix-flips/

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

# link to submission - https://leetcode.com/submissions/detail/740728801/

from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        smaller = {}
        bigger = {}
        ans = 0
        for i, num in enumerate(rating):
            for j in range(i + 1, len(rating)):
                if num < rating[j]:
                    bigger[num] = bigger.get(num, []) + [rating[j]]
                else:
                    smaller[num] = smaller.get(num, []) + [rating[j]]
        for i, num in enumerate(rating):
            for key in bigger.get(num, []):
                ans += len(bigger.get(key, []))
            for key in smaller.get(num, []):
                ans += len(smaller.get(key, []))
        return ans