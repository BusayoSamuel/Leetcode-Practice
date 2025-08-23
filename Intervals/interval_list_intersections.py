"""
https://leetcode.com/problems/interval-list-intersections/description/
"""

class MySolution: #Time complexity 0(m+n), Space complexity 0(m+n)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            startA, endA = firstList[i]
            startB, endB = secondList[j]

            start = max(startA, startB)
            end = min(endA, endB)

            if start <= end:
                res.append([start, end])

            if endA < endB:
                i += 1
            else:
                j += 1

        return res
