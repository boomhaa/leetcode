# link to the problem - https://leetcode.com/problems/minimum-absolute-difference/

# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

# link to submission - https://leetcode.com/submissions/detail/697571523/

class Solution:
    def minimumAbsDifference(self, arr):
        # Sort the original array
        arr.sort()
        answer = []
        min_pair_diff = 10**10
        for i in range(len(arr) - 1):
            min_pair_diff = min(min_pair_diff, arr[i + 1] - arr[i])

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_pair_diff:
                answer.append([arr[i], arr[i + 1]])
        return answer