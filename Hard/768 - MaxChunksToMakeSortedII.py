# link to the problem - https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.

# link to submission - https://leetcode.com/submissions/detail/758934870/

from collections import defaultdict

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedArr = sorted(arr)

        posMap = defaultdict(list)
        for i in range(len(sortedArr)):
            posMap[sortedArr[i]].append(i)

        idx = len(arr) - 1
        cnt = 0
        for i in range(len(arr) - 1, -1, -1):
            idx = min(idx, posMap[arr[i]][-1])
            posMap[arr[i]].pop()
            if i == idx:
                cnt += 1
                idx -= 1
        return cnt