"""
https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
"""

class MyInefficientSolution: #Time complexity O(n^2), Space complexity O(n)
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        q = deque(intervals)
        count = 0

        while q:
            count += 1
            prevLeft, prevRight = q.popleft()
            for _ in range(len(q)):
                curLeft, curRight = q.popleft()

                if prevLeft <= curLeft <= prevRight:
                    q.append([curLeft, curRight])
                else:
                    prevLeft, prevRight = curLeft, curRight

        return count


class EfficientSolution: #Time complexity O(nlogn), Space complexity O(n)
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = []
        end = []

        for i, j in intervals:
            start.append(i)
            end.append(j)

        start.sort()
        end.sort()

        i, j = 0, 0
        res = 0
        groups = 0

        while i < len(start):
            if start[i] <= end[j]:
                groups += 1
                i += 1
            else:
                groups -= 1
                j += 1
            res = max(res, groups)

        return res
