# link to the problem - https://leetcode.com/problems/sort-characters-by-frequency/

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# link to submission - https://leetcode.com/submissions/detail/740766998/

class Solution:
    def frequencySort(self, s: str) -> str:
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            num = dic1.setdefault(s[i], 0)
            dic1[s[i]] = num + 1
        for k,v in dic1.items():
            if v not in dic2:
                dic2[v] = [k]
            else:
                value = dic2[v]
                value.append(k)
                dic2[v] = value
        res = []
        nums = list(dic2.keys())
        nums.sort(reverse=True)
        for num in nums:
            arr = dic2[num] * num
            arr.sort()
            res.extend(arr)
        return ''.join(res)
