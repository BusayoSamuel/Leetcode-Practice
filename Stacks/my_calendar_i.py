"""
https://leetcode.com/problems/my-calendar-i/description/
"""

class MyCalendar: 

    def __init__(self):
        self.schedule = []
        

    def book(self, start: int, end: int) -> bool: #Time complexity O(n), Space complexity O(n)
        if not self.schedule:
            self.schedule.append([start, end])
            return True
        else:
            for interval in self.schedule:
                if interval[0] <= start < interval[1]:
                    return False
                
                if interval[0] < end <= interval[1]:
                    return False

                if start <= interval[0] and end >= interval[1]:
                    return False
                    
            self.schedule.append([start, end])
            return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)