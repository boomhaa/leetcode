# link to the problem - https://leetcode.com/problems/my-calendar-i/

# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
# Implement the MyCalendar class:
# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

# link to submission - https://leetcode.com/submissions/detail/764763808/

class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True