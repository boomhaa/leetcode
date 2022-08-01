# link to the problem - https://leetcode.com/problems/best-sightseeing-pair/

# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.

# link to submission - https://leetcode.com/submissions/detail/762095771/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left_max_vals = [float('-inf') for _ in range(len(values))]
        right_max_vals = [float('-inf') for _ in range(len(values))]

        for i in range(1, len(values)):
            left_max_vals[i] = max(left_max_vals[i - 1] - 1, values[i - 1] - 1)

        for i in range(len(values) - 2, -1, -1):
            right_max_vals[i] = max(right_max_vals[i + 1] - 1, values[i + 1] - 1)

        max_pair = float('-inf')
        for i in range(len(values)):
            max_pair = max(max_pair, values[i] + max(left_max_vals[i], right_max_vals[i]))
        return max_pair