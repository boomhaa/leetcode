# link to the problem - https://leetcode.com/problems/hand-of-straights/

# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

# link to submission - https://leetcode.com/submissions/detail/764821147/

from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        while counter:
            n = groupSize
            start = min(counter.keys())
            while n:
                if start not in counter:
                    return False
                counter[start] -= 1
                if not counter[start]:
                    del counter[start]
                start += 1
                n -= 1
        return True