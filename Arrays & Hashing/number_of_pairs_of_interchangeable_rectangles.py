"""
https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(1)
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rectangles = list(map((lambda x: x[0]/x[1]), rectangles))
        counts = Counter(rectangles)
        res = 0

        for count in counts.values():
            res += math.comb(count, 2)

        return res


class Solution: #Same complexity as above
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        for w, h in rectangles:
            count[w / h] = 1 + count.get(w / h, 0)

        res = 0
        for c in count.values():
            if c > 1:
                res += (c * (c - 1)) // 2
        return res
        
