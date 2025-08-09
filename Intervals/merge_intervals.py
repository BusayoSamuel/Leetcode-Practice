"""
https://leetcode.com/problems/merge-intervals/description/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            bStart, bEnd = intervals[i]
            aStart, aEnd = res[-1]

            if aStart <= bStart <= aEnd:
                res.pop()
                res.append([min(aStart, bStart), max(aEnd, bEnd)])
            else:
                res.append(intervals[i])

        return res


class Solution: #Same complexity as above
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

        
