# link to the problem - https://leetcode.com/problems/stone-game-iv/

# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
# Also, if a player cannot make a move, he/she loses the game.
# Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

# link to submission - https://leetcode.com/submissions/detail/699111063/

class Solution:
    def winnerSquareGame(self, n):
        def dfs(remain):
            if remain == 0:
                return False

            sqrt_root = int(remain**0.5)
            for i in range(1, sqrt_root+1):
                if not dfs(remain - i*i):
                    return True

            return False

        return dfs(n)
