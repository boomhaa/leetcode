# link to the problem - https://leetcode.com/problems/longest-happy-string/

# A string s is called happy if it satisfies the following conditions:
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
# A substring is a contiguous sequence of characters within a string.

# link to submission - https://leetcode.com/submissions/detail/764762435/

from heapq import heappop,heapify, heappush

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        map = {'a': a, 'b': b, 'c': c}
        heap = []
        for key, val in map.items():
            if val != 0:
                heap.append((-val, key))
        heapify(heap)
        ans = ''
        while heap:
            count, char = heappop(heap)

            if len(ans) > 1 and ans[-1] == ans[-2] == char:
                if heap:
                    count2, char2 = heappop(heap)
                    heappush(heap, (count, char))
                    ans += char2
                    if count2 != -1:
                        heappush(heap, (count2 + 1, char2))
            else:
                ans += char
                if count != -1:
                    heappush(heap, (count + 1, char))
        return (ans)