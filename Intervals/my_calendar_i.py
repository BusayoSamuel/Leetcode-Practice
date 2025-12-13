"""
https://leetcode.com/problems/my-calendar-i/description/
"""

class MyCalendar: #Time complexity O(n), Space complexity O(n)

    def __init__(self):
        self.bookings = []
        
    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if start <= startTime < end or start < endTime <= end or startTime <= start < end <= endTime:
                return False
        self.bookings.append([startTime, endTime])
        return True


class MyCalendar: #Same complexity as above

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.events:
            if startTime < end and start < endTime:
                return False

        self.events.append((startTime, endTime))
        return True
