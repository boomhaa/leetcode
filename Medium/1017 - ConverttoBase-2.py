# link to the problem - https://leetcode.com/problems/convert-to-base-2/

# Given an integer n, return a binary string representing its representation in base -2.
# Note that the returned string should not have leading zeros unless the string is "0".

# link to submission - https://leetcode.com/submissions/detail/757135446/

class Solution:
    def baseNeg2(self, n: int) -> str:
        ans = ""
        while n != 0:
            if n%-2 != 0 :
                ans = '1' + ans
                n = (n-1)//-2
            else:
                ans = '0' + ans
                n = n//-2
        return ans if ans !="" else '0'