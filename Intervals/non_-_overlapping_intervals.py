"""
https://leetcode.com/problems/non-overlapping-intervals/description/
"""

class Solution: #Time complexity O(2^n), Space complexity O(n)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = len(intervals)

        def dfs(i, prev, count):
            nonlocal res

            if i >= len(intervals):
                res = min(res, count)
                return

            start, end = intervals[i]
            prevstart, prevend = prev

            if prevstart <= start < prevend:
                dfs(i + 1, intervals[i], count + 1)
            else:
                dfs(i + 1, intervals[i], count)

            dfs(i + 1, prev, count + 1)


        dfs(0, [-math.inf, -math.inf], 0 )
        return res

class BetterSolution: #Time complexity O(nlogn), Space complexity O(n)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
