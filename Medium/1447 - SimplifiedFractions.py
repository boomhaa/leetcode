# link to the problem - https://leetcode.com/problems/simplified-fractions/

# Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. You can return the answer in any order.

# link to submission - https://leetcode.com/submissions/detail/747635598/

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            # here a is greater than b
            while b:
                a, b = b, a % b
            return a

        fractions = []
        if n > 1:
            for dr in range(2, n + 1):
                for nr in range(1, dr):
                    if gcd(dr, nr) == 1:
                        frac = str(nr) + '/' + str(dr)
                        fractions.append(frac)

        return fractions