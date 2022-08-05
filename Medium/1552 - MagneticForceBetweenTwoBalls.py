# link to the problem - https://leetcode.com/problems/magnetic-force-between-two-balls/

# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
# Given the integer array position and the integer m. Return the required force.

# link to submission - https://leetcode.com/submissions/detail/765648060/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def isValid(force):
            start = position[0]
            count = 1
            while (count < m):
                start += force
                i = bisect_left(position, start)
                if (i == n):
                    return False
                start = position[i]
                count += 1
            return True

        i = 1
        j = position[n - 1] - position[0]
        while (i <= j):
            mid = i + (j - i) // 2
            x = isValid(mid)
            if (x):
                i = mid + 1
                ans = mid
            else:
                j = mid - 1
        return ans
