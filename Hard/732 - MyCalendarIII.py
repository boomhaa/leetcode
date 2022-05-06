# link to the problem - https://leetcode.com/problems/my-calendar-iii/

# A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)
# You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.
# Implement the MyCalendarThree class:
# MyCalendarThree() Initializes the object.
# int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar

# link to submission - https://leetcode.com/submissions/detail/694358446/

from collections import Counter


class MyCalendarThree(object):

    def __init__(self):
        self.delta = Counter()

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1

        ans = active = 0

        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans:
                ans = active
        return ans
