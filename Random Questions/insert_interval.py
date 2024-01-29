"""
https://leetcode.com/problems/insert-interval/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:

            if interval[1] < newInterval[0]: #if the new interval is beyond this range
                res.append(interval)
            elif interval[0] > newInterval[1]: #if the new interval is before this range
                res.append(newInterval)
                newInterval = interval
            else: #This means the newInterval is within range
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        res.append(newInterval) #need to add the last newInterval, newInterval is always updated and ends up being beyond the range of everyone else
        return res