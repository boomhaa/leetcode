# link to the problem - https://leetcode.com/problems/guess-number-higher-or-lower/

# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# link to submission - https://leetcode.com/submissions/detail/707037020/

class Solution:
    def guessNumber(self, n: int) -> int:
        middle=n//2
        left=0
        right=n
        while left<=right:
            if guess(middle)==0:
                return middle
            elif guess(middle)==-1:
                right=middle-1
                middle=(right+left)//2
            else:
                left=middle+1
                middle = (right + left) // 2