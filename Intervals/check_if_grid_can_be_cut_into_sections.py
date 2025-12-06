"""
https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [[r[0], r[2]] for r in rectangles]
        y = [[r[1], r[3]] for r in rectangles]
        x.sort()
        y.sort()

        def count_overlaps(intervals):
            count = 0
            prev_end = -1

            for start, end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)
                
            return count

        return max(count_overlaps(x), count_overlaps(y)) >= 3
