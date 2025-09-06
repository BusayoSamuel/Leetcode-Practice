"""
https://leetcode.com/problems/remove-covered-intervals/description/
"""

class Solution: #Time complexity O(nlogn), Space complexity O(n)
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prevStart, prevEnd = res[-1]
            curStart, curEnd = intervals[i]

            if curStart == prevStart and prevEnd < curEnd:
                res.pop()
                res.append([curStart, curEnd])
            elif curEnd > prevEnd:
                res.append([curStart, curEnd])
            else:
                continue

        return len(res)

  class Solution: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 1
        prevL, prevR = intervals[0][0], intervals[0][1]
        for l, r in intervals:
            if prevL <= l and prevR >= r:
                continue
            res += 1
            prevL, prevR = l, r

        return res
