"""Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9]. """

class MyCalendar:
    def __init__(self):
        self.calendar = [] # list of intervals [(10,20), (20,30)]

    def book(self, start: int, end: int) -> bool:
        s1, e2 = start, end
        for s1, e1 in self.calendar:
            if s1 < e2 and s2 < e1: # apply demorgan law on e2 <= s1 or e1 <= s2
                return False
        self.calendar.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

"""Intuition

When booking a new event [start, end), check if every current event conflicts
with the new event. If none of them do, we can book the event.

Algorithm

We will maintain a list of interval events (not necessarily sorted). Evidently,
two events [s1, e1) and [s2, e2) do not conflict if and only if one of them
starts after the other one ends: either e1 <= s2 OR e2 <= s1. By De Morgan's laws,
this means the events conflict when s1 < e2 AND s2 < e1.

Complexity Analysis

Time Complexity: O(N^2), where N is the number of events booked.
For each new event, we process every previous event to decide whether
the new event can be booked. This leads to O(N^2) complexity.

Space Complexity: O(N), the size of the calendar."""
