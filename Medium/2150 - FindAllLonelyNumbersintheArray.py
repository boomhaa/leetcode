# link to the problem - https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

# You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.
# Return all lonely numbers in nums. You may return the answer in any order.

# link to submission - https://leetcode.com/submissions/detail/757153132/

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        possibly_lonely = set()
        for num in nums:
            if num in seen:
                if num in possibly_lonely:
                    possibly_lonely.remove(num)
                continue
            seen.add(num)
            possibly_lonely.add(num)

        for num in possibly_lonely:
            if num - 1 not in seen and num + 1 not in seen:
                ans.append(num)
        return ans