# link to the problem - https://leetcode.com/problems/closest-divisors/

# Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.
# Return the two integers in any order.

# link to submission - https://leetcode.com/submissions/detail/762068994/

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(int((num+2)**0.5), 0, -1):
            if not (num+1)%i:
                return (i, (num+1)//i)
            if not (num+2)%i:
                return (i, (num+2)//i)