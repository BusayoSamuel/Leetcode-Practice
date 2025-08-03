"""

"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key= lambda x: x[0])
        res = []
        
        def merge(prev, cur):
            prevstart, prevend = prev
            curstart, curend = cur

            if prevstart <= curstart <= prevend <= curend:
                return [prevstart, curend]
            elif prevstart <= curstart <= curend <= prevend:
                return [prevstart, prevend]

        for interval in intervals:
            start, end = interval

            if res and res[-1][0] <= start <= res[-1][1]:
                start, end = merge(res[-1], interval)
                res.pop()
        
            res.append([start, end])

        return res

class Solution: #Time complexity O(n), Space complexity O(1)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #covers the case of inserting interval at the start as well as middle
                res.append(newInterval) 
                return res + intervals[i:] 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: #interval is merged into newInterval
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval) #covers the case of inserting interval at the end
        return res
